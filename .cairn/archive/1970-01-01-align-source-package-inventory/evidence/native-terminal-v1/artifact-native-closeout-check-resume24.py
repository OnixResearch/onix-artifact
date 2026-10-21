#!/usr/bin/env python3
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time
import tomllib

base = Path('/home/brittonr/mantle-cairn-finish')
source = base / 'xrepo/artifact-published-5f3962d7-resume23-v3'
run = base / 'runs/artifact-native-closeout-resume24'
archive = Path((run / 'archive-path.txt').read_text().strip())
evidence = archive / 'evidence/native-terminal-v1'
cairn = '/nix/store/xcmnmrk9nd8ssz0snbg4kdg6vlfcqrgm-cairn-0.1.0/bin/cairn'
nix = '/nix/store/kgwqirnzhflf9vmrkzgqz16z2bry397z-nix-2.34.8/bin/nix'
policy = str(source / 'cairn-policy/generated/cairn-policy.json')
records = json.loads((run / 'results.json').read_text())
def execute(label, args):
    started = time.monotonic()
    with (run / (label + '.stdout')).open('xb') as out, (run / (label + '.stderr')).open('xb') as err:
        result = subprocess.run(args, cwd=source, stdout=out, stderr=err)
    record = dict(label=label, command=args, cwd=str(source), exit=result.returncode, elapsed_s=time.monotonic()-started)
    records.append(record)
    (run / 'results.json').write_text(json.dumps(records, indent=2)+'\n')
    for name in [label + '.stdout', label + '.stderr', 'results.json']:
        (evidence / name).write_bytes((run / name).read_bytes())
    print(json.dumps(record), flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    return (run / (label + '.stdout')).read_text()

# Capture immutable byte identities of exactly the maintained pre-check source.
entries = []
for path in sorted(source.rglob('*')):
    if not path.is_file() or '.git' in path.relative_to(source).parts or evidence in path.parents:
        continue
    digest = subprocess.check_output(['b3sum', '--no-names', '--', str(path)], text=True).strip()
    entries.append(dict(path=str(path.relative_to(source)), blake3=digest))
by_path = {entry['path']: entry['blake3'] for entry in entries}
published = json.loads((archive / 'evidence/published-source-v1/source.json').read_text())
allowed_differences = {'README.md', 'flake.nix', '.cairn/specs/artifact-workspace/spec.md', '.cairn/changes/align-source-package-inventory/tasks.md'}
for entry in published['entries']:
    old_path = entry['path']
    path = old_path.replace('.cairn/changes/align-source-package-inventory/', str(archive.relative_to(source)) + '/')
    if old_path not in allowed_differences:
        assert by_path[path] == entry['blake3'], 'protected published source drift: ' + path
# Original checked-in evidence remains byte-for-byte identical after the native move.
for path in archive.rglob('*'):
    if not path.is_file() or evidence in path.parents:
        continue
    relative = str(path.relative_to(archive))
    original_path = '.cairn/changes/align-source-package-inventory/' + relative
    original = subprocess.run(['git', 'show', '3993c1e547a8a9833869c3e5dacce55f87399264:' + original_path], cwd=source, capture_output=True, check=True).stdout
    assert path.read_bytes() == original, 'historical evidence drift: ' + relative
assert not (source / '.cairn/changes/align-source-package-inventory').exists()
assert by_path['.cairn/specs/artifact-workspace/spec.md'] == '56bbbdbbfeff33601cd9f4fd974a8b70d1c0df491a1656f83347b7cf57436293'
workspace = tomllib.loads((source / 'Cargo.toml').read_text())['workspace']
names = [tomllib.loads((source / member / 'Cargo.toml').read_text())['package']['name'] for member in workspace['members']]
repository = json.loads((source / 'config/repository.json').read_text())
release = json.loads((source / 'release/profile.json').read_text())
assert len(names) == 4 and len(set(names)) == 4
assert sorted(names) == sorted(repository['packages']) == sorted(release['packages'])
assert workspace['package']['license'] == 'AGPL-3.0-or-later' and workspace['package']['publish'] is False
readme = (source / 'README.md').read_text()
assert '.cairn/changes/align-source-package-inventory' not in readme
for target in re.findall(r'\]\((\.cairn/archive/1970-01-01-align-source-package-inventory/[^)]+)\)', readme):
    if target.endswith('/native-terminal-v1/complete.json'):
        continue
    assert (source / target).is_file(), target
source_record = dict(base_revision='3993c1e547a8a9833869c3e5dacce55f87399264', implementation_revision=published['revision'], entries=entries, published_source_protected_bytes_unchanged=True, original_change_and_evidence_bytes_unchanged=True, accepted_spec_blake3=by_path['.cairn/specs/artifact-workspace/spec.md'], packages=names, package_license_policy_unchanged=True, required_inventory_complete=True, maintained_archive_links_resolve=True)
(run / 'post-archive-source.json').write_text(json.dumps(source_record, indent=2)+'\n')
(evidence / 'post-archive-source.json').write_bytes((run / 'post-archive-source.json').read_bytes())
validation = json.loads(execute('post-archive-native-validate', [cairn, 'validate', '--root', str(source), '--policy', policy]))
assert validation['valid'] is True
coverage = json.loads(execute('post-archive-traceability-coverage', [cairn, 'traceability', 'coverage', '--root', str(source), '--policy', policy, '--json']))
execute('post-archive-owner-lifecycle-and-inventory-checks', [nix, 'build', '--no-link', '--no-write-lock-file', '-L', 'path:' + str(source) + '#checks.x86_64-linux.cairn-validation', 'path:' + str(source) + '#checks.x86_64-linux.nickel-contracts'])
complete = dict(base_revision=source_record['base_revision'], implementation_revision=published['revision'], archive_path=str(archive.relative_to(source)), native_sync_executed=True, native_sync_satisfied_after_execute=True, native_archive_executed=True, post_archive_valid=validation['valid'], required_source_inventory_complete=True, source_package_license_policy_unchanged=True, prior_transcripts_preserved=True, evidence_source='post-archive-source.json', records=records, pueue_id=os.environ['ARTIFACT_CLOSEOUT_PUEUE_ID'], reused_full_owner_checks='../published-source-v1/published-owner-flake-check.stderr', full_owner_check_reuse_reason='Published implementation, Cargo/Nix locks, package inventories, licenses and policy bytes are unchanged; only accepted-spec sync, native archive, maintained references and traceability comments changed. Re-executed the affected owner lifecycle/traceability and inventory checks; no repeated product tests.', non_claims=['Archive and validation do not prove semantic correctness, consumer migration, anonymous acquisition, trust authority or release eligibility.', '1970-01-01 is the native tool-selected archive prefix, not an execution-date claim.', 'Affected owner checks executed only for x86_64-linux; no aarch64-linux execution is claimed.'])
(run / 'complete.json').write_text(json.dumps(complete, indent=2)+'\n')
(evidence / 'complete.json').write_bytes((run / 'complete.json').read_bytes())
