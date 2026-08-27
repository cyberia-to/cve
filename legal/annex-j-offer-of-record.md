---
tags: cyber valley, cyberia, legal, dzin
alias: annex j, offer of record
crystal-type: measure
crystal-domain: socio
crystal-size: article
icon: "📌"
---

# Annex J — Offer of Record

Annexed to [[land-rights-agreement]]. Per [2.1.2](/cyber-valley/cve/legal/land-rights-agreement#2-part-a-base-grant-hak-sewa-all-holders): "the version of the product page and price schedule on which the Holder relied is annexed as Annex J, identified by commit hash and date. Later amendment of those pages alters neither this deed nor that annex." The product pages are the estate's own repository (`cyber-valley/strategy/`), version-controlled; this annex freezes the exact commit a given Holder relied on.

## Mechanism

At signing, the Landowner records: the file(s) that made up the product page and price schedule shown to the Holder, the git commit hash of the repository at the moment the Holder was shown it, the commit date, and the specific figures the Holder relied on (price per *are*, wave, instrument). This entry does not change afterward, regardless of what the pages say later.

## Worked example — the format, not an executed entry

| field | value |
|---|---|
| Files | `strategy/README.md`, `strategy/annual-leasehold.md` |
| Commit | `d2b33e1c6b504b18142e083be85638439ebd529e` |
| Date | 2026-08-27 |
| What the Holder was shown | Instrument B (annual leasehold): 30% down, balance in equal instalments over the Term at a fixed 3% real over Indonesian CPI |
| Binding vs informational | The instalment mechanic and the 3% real rate are commitments — [2.1.2] says they "change only through this deed and the decision record." Wave pricing, KPI figures and the pricer widget's live output are current-state information and are not frozen by this entry. |

This row is illustrative of the format only; no Holder has relied on it and no lease has been signed against it. A real Annex J entry is created at the moment a specific Holder is shown a specific page, not before.

## What is frozen and what is not

[2.1.2] draws this line for every entry: commitments freeze (renewal by right, the area revenue charge, the assignment regime, the non-disturbance covenant, and — as of this deed — the fixed-rate, non-indexed deferred balance under [[hak-sewa-deed]] §3.2); statements of current state do not (wave-release status, indicative pricing not yet quoted to a specific Holder, the pricer widget's output before a specific number is agreed). Where it is unclear which side of that line a given statement falls on, the Landowner resolves it in the Holder's favour at the time of signing, not afterward.
