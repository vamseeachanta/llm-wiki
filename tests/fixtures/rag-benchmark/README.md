# llm-wiki RAG benchmark fixtures

This directory contains the v1 public-safe, repo-local question set for issue #78.

Rules:

- Use JSON only for the v1 fixture to avoid non-stdlib dependencies.
- Cite committed repo-relative paths only.
- Do not include private mounts, client/vendor content, copied standards text, raw solver models, or secrets.
- Every question needs expected paths, required citations, required facts, and unacceptable-answer criteria.
- Update `fixture_version` whenever questions or expected paths change.
