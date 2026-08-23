---
tags: cyber valley, cyberia, legal, audit
alias: land rights audit, leasehold agreement audit
crystal-type: pattern
crystal-domain: cyberia
icon: "🔍"
---
# Audit of the land rights agreement v0.3

Date: 2026-08-13 · subject: `cyber-valley/cve/legal/land-rights-agreement.md` (v0.3, commit fdb8ab2 of 2026-08-11)

Label scheme: B for blockers, M for mismatches against the strategy and the zoning, C for contradictions inside the sources themselves.

## What was taken as the standard

| layer | document | reconciliation |
|---|---|---|
| development charter | `cyber-valley/strategy/README.md` v2.0, August 2026 | reconciled |
| land use rules | `cyber-valley/policies/zoning system.md` (alias: land usage policy) plus six policy pages | reconciled |
| public product promises | `hak sewa`, `leasehold upfront`, `annual leasehold`, `hak pakai`, `hak milik`, `joint venture` | reconciled |
| indexation | `cyberia/protocol/century-index.md`, theses T1–T8 | reconciled |
| constitutional layer | `cyberia/foundation/`: manifesto, org, architecture, strategy | partly reconciled |
| the "new charter" from the Cyberia legal compliance chat | — | not received |

The `Cyberia legal compliance` chat is not reachable from here: `ListAgents` sees no reachable session, and no document under that name exists in Google Drive or in the granted `~/cyber` folders. The audit below is built on what is in the repository. If that chat holds a charter text differing from strategy v2.0, send it as a file or as text and sections 2 and 3 will be re-run and updated.

## Verdict

The document is good as a skeleton and honest where it touches Indonesian law: bilingual execution, notarial form, anti-nominee, subordination to the HGB term, PBG in the name of the title holder, the BAST chain, the Licence Event regime. Those are the strong parts and they should be kept.

As a contract template it is not ready, and the principal problem is one of stitching rather than of law: the charter and the product pages promise the buyer things the agreement does not contain, and in three cases promise the exact opposite of what the agreement says. While those three contradictions live, any executed counterpart is written evidence of a divergence between the advertising and the deal.

Count: 3 blockers, 9 mismatches against the charter and the zoning, 4 internal contradictions between sources, 11 missing clauses, 5 missing instruments.

---

## 1. Blockers — nothing is signed or sold until these are cleared

### B1. "registered lease" against §2.2

The product pages and the charter tell the buyer he receives a registered right:

- `leasehold upfront`: "registered 25y term + extension pre-agreed"
- strategy §6.1, instrument A: "Full payment at signing, registered lease (25y + pre-agreed extensions)"

Agreement §2.2 says the opposite, and says it correctly: hak sewa is a contractual right, it is not registered at BPN and does not appear on the certificate.

One of the two statements is false, and the false one is what is printed on the shopfront. For a buyer paying 100% up front, the difference between a registered right and a contract with a PT PMA is the whole difference. Fix: remove the word registered from pages A and B and from strategy §6.1, keep the formulation of the `hak sewa` page ("it is a right, not a title"), and move this into the recitals of the agreement rather than leaving it at §2.2 in the middle of the text.

### B2. "locked on day one" against the mechanics of the century index

`annual leasehold`: "the rest is a fixed yearly rent for 25 years — locked on day one, not renegotiated at market"; annex B: "rent path still fixed at signing". The calculator draws a smooth curve at CX 6% and land 3%.

Century index §2 and §4: the payment is a fixed set of quantities rather than a number; the rate is recomputed annually on TWAP, with a collar of +35% / −15% in satoshi and a double floor. A single year can produce +35%.

What is fixed is the formula and the quantities qᵢ, not the amount. The page sells predictability of the payment, the specification sells predictability of the rule. Fix: say on the page what the thing is — quantities are fixed, the amount is not; the amount moves with the basket, and the annual step is bounded by a collar of +35/−15 — and show the historical path from the backtest in the calculator (1.00 → 1.80 → 1.00 → 2.16 → 4.07 → 3.54) rather than only a smooth exponential. In the agreement: a separate article on what exactly is fixed, plus one worked invoice in the annex, as T1 requires.

### B3. hak pakai: two incompatible constructions

- agreement §3.2: conversion from the underlying title into the Holder's name, a term of 30 + 20 + 30, requiring `pemecahan` of the plot out of the master title. This is hak pakai atas tanah — the plot leaves the PT PMA.
- the `hak pakai` page: "applies to built assets — a finished, certified villa — not raw land; the underlying parcel stays with PT PMA".

The plot cannot both separate and remain. Until one is chosen, instrument D cannot be sold: this is precisely the case where the buyer pays 100% on conversion and receives something other than what he understood. Fix: choose the construction, describe it on the page in the same words as in §3, and rewrite the §3.3 trade-offs to match.

---

## 2. Mismatches against the charter (strategy v2.0)

### M1. The century index is not an operative clause

Charter, stream 4: rent is indexed through CX. Pages A and B: "extension pre-agreed and priced on the century index — the renewal cost is fixed by the index at signing, never renegotiated at market".

The agreement mentions CX once in §2.3 by reference, while §2.4 sends the renewal price to "the formula in Schedule E" and itself warns that "to be agreed" is the principal defect of Bali leases. Schedule E is empty. As it stands the agreement contains exactly the defect it warns against.

Fix: Schedule E becomes the CX annex under T1 (weights, t₀ prices, quantities qᵢ, fix sources with fallbacks, collar, floor, one worked invoice), plus the migration into the body of the agreement of T5 (the tenant's right to recompute within 30 days, the recomputation prevailing), T6 (settlement in IDR at JISDOR on the invoice date, [[uu 7-2011 mata uang|UU 7/2011]]), T7 (the annex surviving assignment, sublease and succession), T8 (the computation from public fixes prevailing over the on-chain fix). Renewal formula: L(T) = L₀ · I(T)/I(t₀).

### M2. The zoning code is not a covenant

Pages A, B and E say the zoning code runs with the land as a covenant — footprint caps, species density, pollution policies. For hak milik, "as recorded covenants".

Agreement §7 describes the Design Code as Schedule C and mentions the policy stack in a single ⚠ remark. Not one number from `zoning system` appears in the agreement.

The numbers that must reach Schedule C, because they determine what a person can build at all:

- building footprint at most 10% of the plot, ×2 across two storeys
- light balance: absorbers 1–10%, water bodies 1–10%, transparent surfaces 2–10%, lawn or ground cover ≤5%, grasses and shrubs ≥30%, dwarf trees and canopy ≥40%, totalling 100%
- biodiversity: 20 plant species per hectare
- sound: 55 dB(A) day / 40 night at the boundary of a residential zone, 45/35 in forest and conservation zones, silence in the window 05:00–07:00, 48 hours' notice to neighbours within 300 m
- water: PPR pipes only, greywater to BOD < 30 mg/l, blackwater to closed composting or a biodigester, a 15 m buffer around any source
- light: 2200 K and warmer, full cut-off upward, non-essential lighting off by 23:00, 0 lux at the conservation buffer
- air: no open burning of synthetics, a diesel generator only as backup for at most 4 h/day, zero-VOC finishes
- soil: an unconditional ban on synthetic pesticides, herbicides and mineral fertilisers; bare soil for no longer than 30 days; biochar from 0.5 t/ha/year in food zones

Separately: the duty to publish to the cyberia ledger — quarterly monitoring of discharges and an annual soil analysis for the plot. This is a Holder obligation, it has a cost, and it should carry consequences for non-performance. The agreement does not contain it at all.

### M3. The 10% footprint — per plot or per district?

`zoning system` does not say over what area the 10% and the 40% canopy are measured. On a 500 m² plot that is 50 m² of footprint, 100 m² across two storeys, plus a requirement of 40% under canopy on the same plot. For the buyer this is the single most important number in the whole deal — it determines what he can build at all.

This is a blocking decision ahead of Schedule C: per plot (strict, honest, easily verified) or per district on a zone average (softer for the buyer, but then a quota accounting mechanism is needed, along with a bar on the first builders exhausting it). Until it is decided, the Design Code cannot be written.

### M4. Build obligation: reversion is promised, and absent from the agreement

Charter, risk register: "Build obligations + reversion clauses on all early-phase sales". Page A: "reversion if nothing stands in 2–3 years". Strategy §6.2, wave 1: "A + build obligation".

Agreement §6: commence within 12 months, complete within 36, remedy "[escalating holding charge / Landowner's option to repurchase]". Reversion is not selected, the bracket is open, and 36 months is wider than the promised 2–3 years.

### M5. The estate economics are absent from the operative clauses

Charter §8 sets out five recurring streams. Not one of them appears in the agreement as an obligation:

| stream | in the charter | in the agreement |
|---|---|---|
| tariffs for energy, water, connectivity, waste | §8.1 | absent |
| share of revenue of a business on the plot (participation rent) | §8.2 | absent |
| share of sublet | §8.3 | §2.6, by reference in brackets |
| indexed rent | §8.4 | §2.3, by reference |
| the lease right "free" in exchange for 2 and 3 | §8.5 | absent |

For the sublet share the agreement points at the `hak sewa` page (10%, or 5% in a self-sufficient district, plus a settlement fee of 1–3%). A reference to a wiki page is not a contractual obligation. Definitions are needed: what revenue means, who certifies net exporter status for energy, water and food and how, how often the status is reviewed, whether there is an appeal, audit rights, reporting deadlines, and the consequences of understatement.

### M6. Zones Z1–Z8 do not exist in the agreement

The charter builds everything on zones with different instruments and different terms: Z3 — near-zero rent plus participation rent after break-even, deed restrictions and reversion on a change of use; Z5 — land for equity, lease ×0.2 for 2–5% equity, expiring options; Z6 — annual rent plus participation in farm revenue; Z4 — a slot as a 25-year micro-asset.

The agreement is one universal residential lease. Schedule G ("permitted-use matrix by Holder class and track") is a stub. One document cannot be stretched across all of this: a base deed plus zonal annexes is needed.

### M7. The car-free core is not disclosed

Charter §5: "The core is car-free. Vehicles stop at the Z4 mobility hub on the perimeter". This is a fundamental restriction on use: a person buys a plot that cannot be driven to. The agreement says nothing about access, parking, construction logistics and removal, or rights to e-mobility and the shuttle.

### M8. The PT PMA ↔ Cyberia DAO bridge is not laid

Charter §10 calls DAO-side representations of PT PMA lease registry entries "the single most important legal engineering task of phase 0–1". Tokenisation: parking slots first, then derivatives of residential leases. The agreement contains neither a register of leases, nor a clause on the on-chain representation of the right, nor a rule of priority where the register and the on-chain entry diverge — even though such a rule already exists for CX (T8) and can be taken as the model.

### M9. The long-term land model against §10 of the agreement

Charter §10: "Buildings and use-rights trade; the land itself does not", trending towards a community land trust. Agreement §10 leaves the fate of Improvements open: (a) demolition, (b) transfer to the Landowner free of charge, (c) transfer against compensation.

Variant (b) contradicts the charter's thesis: if the value of the buildings belongs to the Holders, a free transfer at the end of the term expropriates it. Related to B2: the promise of "extension pre-agreed" is economically the answer — under guaranteed renewal the question of the end of term barely arises; but if the master title is not renewed, the question arises instantly and there is no answer.

---

## 3. Contradictions inside the sources themselves

These must be cleared before the agreement is amended, or the agreement will inherit the fork.

### C1. "The lease right — free" against the wave curve

Charter §8, stream 5: "Entry costs nothing as such: the right to hold a lease is granted in exchange for 2 and 3. The estate earns from the city's activity, not from gatekeeping the door".

Charter §6.2: wave 1 — ×0.4 per are, wave 2 — ×0.7, wave 3 — ×1.0–1.3, reserve ×2+. Page A: 100% payment at signing. Page B: a 30% deposit plus 25 years of rent.

Entry costs money, and a good deal of it. Stream 5 as currently worded is untrue about its own product. Either it describes a future state and must be marked as such, or it should be removed.

### C2. Sublet: rails or a management company

- `hak sewa`: the estate's share is "not a management commission"; the estate provides rails and permission, 10%/5% plus 1–3%, roughly 11–13% in total.
- charter §6.1: "All leases include sublease rights through the estate management company, enabling a rental pool for absentee owners".

Through a management company is precisely a management commission. Choose one.

### C3. Plot size

- agreement §4.3: plots of 500–600 m², to stay within the simplified route for conversion to hak milik.
- charter §5: "plots of 5–15 are", that is 500–1500 m².
- charter §13, open item 1: 5 are against 10 are — undecided, "gates Wave 1 marketing".

A plot above 600 m² takes an Indonesian buyer out of the simplified route and requires a constatering report. Add the declaration of no more than 5 parcels or 5,000 m² in aggregate. The decision on the grain is simultaneously a decision on whether instrument E works at all.

### C4. Settlement in USDT

`hak sewa`: the marketplace "settles in USDT". Century index T6 honestly fixes the opposite for rent: [[uu 7-2011 mata uang|UU 7/2011]] requires settlement in rupiah at JISDOR.

A sublet of land inside Indonesia between parties on Indonesian territory is a payment obligation in a jurisdiction where a crypto asset is not a means of payment. The product is described so that its settlement layer conflicts with currency law. A fork is needed: either USDT is a unit of account only with mandatory settlement in IDR, or settlement is moved outside the perimeter, in which case it must be stated honestly who the party is and where.

Adjacent, and of the same class: the `hak sewa` page sells re-letting of land on an "hour, day, week" horizon through a marketplace. A short horizon with occupation is accommodation rather than a lease of bare land: licensing, Buleleng regional requirements, local accommodation tax. §2.6 says "Holder must operate under the applicable accommodation licensing" and stops there. Between a sublet right sold as unconditional and licensing that the buyer must obtain himself and often cannot (pondok wisata being an Indonesian-citizen channel) lies a gap that must be disclosed on the product page rather than at §2.6.

---

## 4. Missing clauses

Beyond the above, the skeleton lacks:

1. Force majeure. The site is on the slope of Mount Sanghyang at 1,200–1,500 m, with a rainy season and landslide gradients. Seismic and volcanic activity are not mentioned once.
2. Insurance after construction. §5A.4 covers the construction period and stops at completion.
3. Quiet enjoyment. Named in §9A.3 as a condition, but the covenant itself is absent.
4. Encumbrance of the right. Whether the Holder may charge a hak sewa is a question of buyer financing, and there is no answer.
5. Succession and the death of the Holder. Over 25+25 years this is not a rare event.
6. Adat. For a Balinese estate the absence of subak, banjar, awig-awig desa adat, ceremonial passage and customary obligations is a large gap. `sempadan sungai` and subak are mentioned once in §2.7 as somebody else's risk. The charter meanwhile spends 10% of recurring income on the desa share and calls it a guardrail on tone.
7. VAT. §12 lists PPh, BPHTB, notarial fees and PBB. VAT on the lease of land and buildings is not mentioned — confirm the rate and base with an adviser, and who bears it.
8. Currency of account against currency of payment. There is no express clause.
9. KYC and source of funds. §9 gives a representation, with no procedure.
10. Boilerplate: notices, entire agreement, counterparts and electronic signature, the language of notices and correspondence, severability.
11. Personal data. Publishing plot analysis results to the cyberia ledger is a disclosure tied to an identifiable person; a processing basis and a scope are needed.

## 5. Missing instruments

Being sold now or in phase 0, with no template:

| product | where promised | status |
|---|---|---|
| parking slot, 25 years, $1k / $5k, minimum-rent guarantee for 2 years | charter §6.2 Z4, tranche 1 in phase 0 ≈ $1M | no template |
| expiring option on wave 2 | charter §7 phase 0, §6.2 Z5 | no template |
| land-for-equity, ×0.2 for 2–5% | charter §6.2 Z5 | no template |
| JV annex, 40–60% split | instrument C | no template |
| Z3 with deed restrictions and reversion on change of use | charter §6.2 Z3 | no template |

The phase 0 slot is closest to sale and the most exposed: a low ticket, many buyers, a promised yield qualified by "assumes Phase 2+ traffic", a guarantee from the management company, and a declared first place in the tokenisation queue. That is a retail product with elements of an investment offering. It needs its own document with risk disclosure rather than a line in the strategy.

## 6. Document hygiene

- The version is ambiguous: the heading says v0.3 while the changelog on the same line runs v0.3 → v0.2 → v0.1 → v0.3.1. The order is broken and the highest version in the list does not match the heading.
- 283 lines — within the ≤500 rule.
- Bold is used widely, whereas the graph rule bans it: emphasis is a heading, frontmatter or a wiki-link. For legal text, bold clause leaders are a normal convention, so either exempt `legal/` from the rule in CLAUDE.md explicitly or convert the leaders into numbered headings. As things stand the rule is simply broken in silence.
- Zoning references are inconsistent: `[[zoning system]]` in §7 against `[[cyber-valley/policies/zoning system|zoning code]]` on the product pages. Likewise `[[rent index]]` in strategy §6.1 against `[[century index]]` everywhere else.
- §2.7 rests on the dispositive character of Arts. 1588–1592 KUHPerdata. That is the clause's only support, and the numbering must be confirmed with the notary before the wording goes into a template: if the articles are the wrong ones, the clause is empty. This item is missing from the open questions.
- The open questions (14 checkboxes) are a strong part of the document; keep them in the template too, carried into a separate file so that they do not travel into the signable text.

## 7. What has to be decided before the template

Fifteen forks. Without answers the template will be a set of brackets.

1. B1 — fix the shopfront or the construction: remove "registered" or build a registrable right.
2. B2 — how predictability of rent is formulated on page B.
3. B3 — hak pakai over land with pemecahan, or over the structure with the plot retained by the PT PMA.
4. M3 — the 10% footprint and 40% canopy measured per plot or per district.
5. C3 — the Z1 grain: 5 are, 10 are or the 5–15 range; and consequently whether the simplified hak milik route is preserved.
6. M4 — reversion or a holding charge; 2–3 years or 12/36 months.
7. C2 — sublet through marketplace rails or through a management company.
8. C4 — the settlement currency of a sublet and its licensing perimeter.
9. M5 — the definition of revenue, and the body and procedure confirming net exporter status for the 5% rate.
10. M9 — the fate of Improvements at the end of term: (a), (b) or (c), and separately for the three termination scenarios.
11. §0 — the actual remaining length of the HGB, and what happens to 25+25 if it is shorter than the sum.
12. §2.6 — sublet as a right, or as a right subject to consent.
13. §8 — the Association: who incorporates it, what the quorum is, and how it relates to the DAO layer.
14. M8 — the form of on-chain representation of a lease and the rule of priority on divergence.
15. The bilingual format: RU-EN-ID is chosen, but an answer is needed on which language prevails on discrepancy and who is answerable for the Indonesian text — a translator or the notary.

## 8. Proposed structure of the v0.4 package

One file for everything does not work: the ≤500 line rule and the zonal differences break it already.

```
legal/
  land-rights-agreement.md      open questions, principles, package map (stays, cleaned up)
  deed-hak-sewa.md              base deed, RU-EN-ID, three columns
  annex-a-estate.md             master title, cadastre, zoning, KKPR
  annex-b-plot.md               boundaries, patok, neighbours, GPS/UTM, peta bidang
  annex-c-design-code.md        the zoning code as numbers, from policies/*
  annex-d-community-rules.md    community rules, tone, car-free, adat
  annex-e-century-index.md      the CX annex under T1 with a worked invoice
  annex-f-utilities.md          access, connections, tariffs
  annex-g-permitted-use.md      use matrix by zone and class
  annex-h-condition.md          condition at site handover, the baseline for BAST #6
  zone-z3-community.md          annex: deed restrictions, reversion on change of use
  zone-z5-innovation.md         annex: land-for-equity, options
  zone-z6-agro.md               annex: participation in farm revenue
  instrument-parking-slot.md    a separate document for the slot, with risk disclosure
  instrument-option.md          the wave option
```

The base deed is written in three parallel columns RU-EN-ID from the start, as chosen. The Indonesian column is written alongside the Russian and English rather than translated afterwards — divergences between languages are born precisely at the stage of late translation, and it is those divergences that later decide the dispute, because under UU 24/2009 priority usually lies with the Indonesian text.

---

## Reservation

This is not legal advice. Every statement about Indonesian law in this audit is either a quotation from the draft itself or an item marked as requiring confirmation. It is verified with a notary and a PPAT — preferably not only the one proposed by the landowner — before signing, against the current editions of the regulations and against the actual master title.
