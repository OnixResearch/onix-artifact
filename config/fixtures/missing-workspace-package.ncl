let Contracts = import "../contracts.ncl" in
let Repository = import "../repository.ncl" in
(Repository & {
  packages | force = ["artifact-auth-core", "artifact-auth-ed25519", "artifact-transfer-core"],
}) | Contracts.Repository
