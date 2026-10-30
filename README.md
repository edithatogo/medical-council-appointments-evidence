# Medical Council appointments: documentary evidence

Version 1.0.0. This is a bounded documentary record of the 2026 Medical Council appointments, not a complete account of every government record or a finding of unlawfulness.

Start with `data/events.csv` for the dated sequence, `data/catalogue.json` for source identities and access limitations, and `data/legal-matrix.json` for legal propositions, missing facts and claim boundaries. Catalogue entries include sources considered but not used to support an appointment inference. Original public URLs and retained-version hashes distinguish sources from the researchers’ annotations. Hashes identify locally retained versions; the linked live page may change.

Three exact official Supreme Court judgments are included on the source-specific basis recorded in `data/redistributed-files.json`. No manuscript, private correspondence or private repository history is included. Other originals remain identifiable through source links and retained-version hashes unless separately qualified for redistribution. Cite the versioned GitHub release and commit; no DOI is claimed.

## Reading the process models

The BPMN and Mermaid files are non-executable explanatory models. Sequence arrows show an administrative sequence, not proof that one event caused the next. Ministerial selection, APH consideration, legal appointment and Council election of its chair are different acts. The actual APH minute, lodged paper version and Love-specific completed appointment instrument were not located in this bounded search. Missing records do not establish that an act did not occur.

The fairness model is conditional: whether a response opportunity was legally required depends on the facts and applicable law. It also includes proposed safeguards, which are not assertions that they were existing duties. The powers model distinguishes legislation in force, proposed legislation and the authors’ recommendations. The chronology cannot establish the reason for the reversal.

## Verification

Create a local Python 3.15.1 environment, then run `.venv/bin/python scripts/verify.py`. This verifies archive file hashes, not source accuracy or publication rights. `provenance.json` uses the archive-govt-nz manifest interface. The GitHub release identifies the published commit. Publication readback receipts are maintained separately from this immutable payload.

Existing Hansard datasets are contextual resources, not destinations for these appointment records. This dedicated repository separates appointment evidence from those existing collections.

The catalogue accounts for 119 public source groups, including three metadata-only entries with unresolved original URLs. One private-correspondence source group is excluded without publishing its identifying details. These counts concern source groups, not numbers of files or fully reviewed documents.

`data/claim-source-map.json` gives short research labels and evidence boundaries, without reproducing unpublished manuscript text. `models/argument.png` presents the argument visually; its links denote support or qualification rather than causal effects.

Five qualified text derivatives accompany the three judgment PDFs: four legislative documents and the Smylie article text. These are extracted text, not originals or facsimiles. Selection boundaries, omitted images and external files, source hashes, URLs and attribution are recorded in `data/text-derivatives.json`. A full CC BY 4.0 legal code accompanies the article derivative. Three additional legal-context sources are catalogued as S118–S120, without implying they prove wrongdoing in the appointment process.

## Reusing this work

Original catalogue annotations and explanatory diagrams are CC BY 4.0; project-owned scripts are Apache-2.0. Third-party sources retain their own rights. See RIGHTS.md and the per-source register. Provenance uses the existing [archive-govt-nz](https://github.com/edithatogo/archive-govt-nz) manifest interface. This archive contains research materials, not a manuscript preprint or journal correspondence.
