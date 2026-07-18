# Release evidence

A release candidate is admitted only when the checked repository/release Nickel exports are fresh, both packages pass host and Wasm no-std checks, positive and negative Rust tests pass, Clippy and formatting pass, Cairn lifecycle validation passes, authority audits find no forbidden shell dependencies, source provenance is complete, and the immutable Git revision is recorded.

Passing these checks proves bounded source, contract, build, and fixture facts only. It does not prove cryptographic library correctness, trust-root correctness, revocation freshness, consumer adapter correctness, artifact truth, authorization, or product release eligibility.
