let OwnedPackageCount = 2 in
let OwnedPackages = std.contract.from_predicate (fun value =>
  std.is_array value
  && std.array.length value == OwnedPackageCount
  && std.array.elem "artifact-auth-core" value
  && std.array.elem "artifact-auth-ed25519" value
) in
let SourceContract = {
  consumer | String,
  revision | String,
  role | String,
} in
let RepositoryContract = {
  name | String,
  repository | String,
  license | String,
  packages | OwnedPackages,
  schemas | Array String,
  source_cohort | Array SourceContract,
  release_checks | Array String,
  non_claims | Array String,
} in
{
  Repository = RepositoryContract,
  Source = SourceContract,
}
