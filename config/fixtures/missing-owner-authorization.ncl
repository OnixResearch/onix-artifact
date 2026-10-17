let Contracts = import "../contracts.ncl" in
{
  name = "artifact-auth",
  repository = "https://github.com/OnixResearch/artifact-auth",
  license = "AGPL-3.0-or-later",
  packages = ["artifact-auth-core", "artifact-auth-ed25519"],
  schemas = [],
  source_cohort = [],
  release_checks = [],
  non_claims = [],
} | Contracts.Repository
