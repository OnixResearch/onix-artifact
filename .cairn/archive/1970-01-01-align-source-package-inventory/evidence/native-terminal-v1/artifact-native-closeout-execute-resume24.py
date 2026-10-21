#!/usr/bin/env python3
import json
from pathlib import Path
import subprocess
import time

base = Path('/home/brittonr/mantle-cairn-finish')
source = base / 'xrepo/artifact-published-5f3962d7-resume23-v3'
run = base / 'runs/artifact-native-closeout-resume24'
cairn = '/nix/store/xcmnmrk9nd8ssz0snbg4kdg6vlfcqrgm-cairn-0.1.0/bin/cairn'
policy = str(source / 'cairn-policy/generated/cairn-policy.json')
active = source / '.cairn/changes/align-source-package-inventory'
records = json.loads((run / 'results.json').read_text())
def execute(label, args):
    started = time.monotonic()
    with (run / (label + '.stdout')).open('xb') as out, (run / (label + '.stderr')).open('xb') as err:
        result = subprocess.run(args, cwd=source, stdout=out, stderr=err)
    records.append(dict(label=label, command=args, cwd=str(source), exit=result.returncode, elapsed_s=time.monotonic()-started))
    (run / 'results.json').write_text(json.dumps(records, indent=2)+'\n')
    print(json.dumps(records[-1]), flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    return json.loads((run / (label + '.stdout')).read_text())
def native(command, execute_flag=False):
    return [cairn, command, 'align-source-package-inventory', '--root', str(source), '--policy', policy] + (['--execute'] if execute_flag else [])
def retain(evidence):
    for path in run.iterdir():
        (evidence / path.name).write_bytes(path.read_bytes())
preview = json.loads((run / 'native-sync-preview.stdout').read_text())
assert not preview['blocked'] and preview['reasons'] == []
documents = preview['merge_preflight']['documents']
assert len(documents) == 1 and documents[0]['destination'] == '.cairn/specs/artifact-workspace/spec.md'
assert documents[0]['operations'] == [{'block_hash': '3b9f5fe5388beed63ee64bbe37c442330c331066ec3f8949562676b25e7d8237', 'heading': '### Requirement: Source-package inventory is complete', 'kind': 'added', 'requirement_id': 'artifact_workspace.source_inventory.complete'}]
assert documents[0]['changed']
sync = execute('native-sync-execute', native('sync', True))
assert sync['mutated'] and not sync['blocked']
post_sync = execute('native-post-sync-preview', native('sync'))
assert not post_sync['blocked'] and all(not doc['changed'] for doc in post_sync['merge_preflight']['documents'])
preview = execute('native-post-sync-archive-preview', native('archive'))
assert not preview['blocked'] and preview['reasons'] == []
assert [action['kind'] for action in preview['actions']] == ['archive_change']
retain(active / 'evidence/native-terminal-v1')
result = execute('native-archive-execute', native('archive', True))
assert result['mutated'] and not result['blocked']
assert not active.exists()
archives = list((source / '.cairn/archive').glob('*-align-source-package-inventory'))
assert len(archives) == 1
archive = archives[0]
(run / 'archive-path.txt').write_text(str(archive)+'\n')
retain(archive / 'evidence/native-terminal-v1')
print('archive=' + str(archive))
