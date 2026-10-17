let Contracts = import "../contracts.ncl" in
let Repository = import "../repository.ncl" in
# Keep all other admitted fields valid; reject the old grant for current source.
((std.record.remove "license" Repository) & {
  license = "MIT OR Apache-2.0",
}) | Contracts.Repository
