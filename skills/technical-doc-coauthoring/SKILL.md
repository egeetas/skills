---
name: technical-doc-coauthoring
description: Coauthor substantial technical specs, RFCs, ADRs, proposals, runbooks, or engineering guides through context gathering, drafting, and reader validation.
---

# Technical Document Coauthoring

Create a document that works for readers who do not share the authors' conversation context. Match an existing template and repository documentation style when present.

## Gather Context

Resolve the document type, audience, intended decision or action, scope, constraints, owners, and source material. Let the user provide shorthand or an unstructured context dump. Ask only the highest-value questions needed to close gaps around goals, alternatives, architecture, risks, rollout, and success criteria.

Separate verified facts, decisions, proposals, assumptions, and open questions. Cite source files, issues, discussions, or external references where readers will need provenance.

## Structure and Draft

Propose a compact structure suited to the document rather than forcing one template on every task. For an RFC without an established repository format, start from [the RFC template](assets/rfc-template.md). For each consequential section:

1. identify what a reader must learn or decide;
2. surface missing evidence and meaningful alternatives;
3. draft in plain, direct language with explicit contracts and trade-offs;
4. incorporate feedback through focused edits;
5. remove duplication, filler, and unexplained jargon.

For technical decisions, cover rejected alternatives, compatibility, security, failure modes, migration, observability, rollout, rollback, and ownership in proportion to risk. Leave summaries until the core argument is stable.

## Reader Validation

For a substantial or high-impact document, use one or more fresh subagents when available to test it without conversation context. Give each only the document and a realistic reader question or review role. Check whether they can identify the decision, prerequisites, workflows, risks, and next actions; also ask for ambiguities, contradictions, and unstated assumptions.

Validate and deduplicate their observations before revising. Use [the reader-test rubric](references/reader-test-rubric.md) to keep reviews comparable. If subagents are unavailable, provide the checklist for the user to run in a fresh Codex task.

Finish with a full coherence pass and verify factual claims, links, code examples, commands, terminology, and document-specific formatting. Report unresolved questions and validation limits.
