#!/usr/bin/env python3
from pathlib import Path
source = Path('/home/brittonr/mantle-cairn-finish/xrepo/artifact-published-5f3962d7-resume23-v3')
readme = source / 'README.md'
text = readme.read_text()
old = '.cairn/changes/align-source-package-inventory/evidence/'
new = '.cairn/archive/1970-01-01-align-source-package-inventory/evidence/'
assert text.count(old) == 2
text = text.replace(old, new)
old_claim = 'consumer migration, anonymous acquisition, lifecycle archive or release eligibility.'
new_claim = ('consumer migration, anonymous acquisition or release eligibility. Native sync\n'
             'accepted the complete source-package inventory, and native archive moved the\n'
             'change to the tool-selected `1970-01-01-align-source-package-inventory` path.\n'
             'Terminal command receipts and post-archive validation are retained in\n'
             '[`native-terminal-v1`](.cairn/archive/1970-01-01-align-source-package-inventory/evidence/native-terminal-v1/complete.json).\n'
             'The archive path is the native tool output, not a claim about execution date.')
assert text.count(old_claim) == 1
readme.write_text(text.replace(old_claim, new_claim))
flake = source / 'flake.nix'
text = flake.read_text()
old_comment = '            # The source-inventory delta is not an accepted requirement until native sync.'
new_comment = ('            # r[impl artifact_workspace.source_inventory.complete]\n'
               '            # r[verify artifact_workspace.source_inventory.complete]')
assert text.count(old_comment) == 1
flake.write_text(text.replace(old_comment, new_comment))
