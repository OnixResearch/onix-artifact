# Cairn policy provenance

The local lifecycle policy was initialized from Cairn revision `cc4639be24475d80844b091cdec605eb2fef9ff0` and given artifact-auth evidence roots in Cairn's required `cairn-default` traceability profile. The release flake uses the latest published compatible Cairn revision `cf5c4a5c10361ca20a13addf14954407d6857028` until the newer local Cairn commits are published.

Runtime validation consumes `generated/cairn-policy.json`. Refresh it only with `cairn policy export` from the pinned or explicitly reviewed Cairn provider, then run lifecycle validation and traceability coverage.
