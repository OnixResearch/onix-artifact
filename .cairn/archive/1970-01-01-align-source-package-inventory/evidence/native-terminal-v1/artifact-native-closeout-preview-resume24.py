#!/usr/bin/env python3
import json
import os
from pathlib import Path
import subprocess
import time

base = Path('/home/brittonr/mantle-cairn-finish')
source = base / 'xrepo/artifact-published-5f3962d7-resume23-v3'
run = base / 'runs/artifact-native-closeout-resume24'
run.mkdir(exist_ok=False)
cairn = '/nix/store/xcmnmrk9nd8ssz0snbg4kdg6vlfcqrgm-cairn-0.1.0/bin/cairn'
policy = str(source / 'cairn-policy/generated/cairn-policy.json')
records = []
def execute(label, args):
    started = time.monotonic()
    with (run / (label + '.stdout')).open('xb') as out, (run / (label + '.stderr')).open('xb') as err:
        result = subprocess.run(args, cwd=source, stdout=out, stderr=err)
    records.append(dict(label=label, command=args, cwd=str(source), exit=result.returncode, elapsed_s=time.monotonic()-started))
    (run / 'results.json').write_text(json.dumps(records, indent=2)+'\n')
    print(json.dumps(records[-1]), flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    return (run / (label + '.stdout')).read_text()
assert execute('starting-head', ['git', 'rev-parse', 'HEAD']).strip() == '3993c1e547a8a9833869c3e5dacce55f87399264'
for label, command in [('native-sync-preview', 'sync'), ('native-archive-preview', 'archive')]:
    execute(label, [cairn, command, 'align-source-package-inventory', '--root', str(source), '--policy', policy])
evidence = source / '.cairn/changes/align-source-package-inventory/evidence/native-terminal-v1'
evidence.mkdir(exist_ok=False)
for path in run.iterdir():
    (evidence / path.name).write_bytes(path.read_bytes())
