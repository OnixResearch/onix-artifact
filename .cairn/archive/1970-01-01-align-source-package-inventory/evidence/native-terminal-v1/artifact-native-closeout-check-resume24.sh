#!/usr/bin/env bash
set -Eeuo pipefail
read -r ARTIFACT_CLOSEOUT_PUEUE_ID < /home/brittonr/mantle-cairn-finish/runs/artifact-native-closeout-resume24/pueue-id
export ARTIFACT_CLOSEOUT_PUEUE_ID
exec python3 /home/brittonr/mantle-cairn-finish/bin/jobs/artifact-native-closeout-check-resume24.py
