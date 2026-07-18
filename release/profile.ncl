let Repository = import "../config/repository.ncl" in
{
  schema = "artifact-auth.release-profile.v1",
  project = Repository.name,
  repository = Repository.repository,
  license = Repository.license,
  packages = Repository.packages,
  required_checks = Repository.release_checks,
  source_cohort = Repository.source_cohort,
  distribution = {
    channel = "immutable-git-revision",
    crates_io = false,
    sibling_paths = false,
    floating_revisions = false,
  },
  claim_boundary = Repository.non_claims,
}
