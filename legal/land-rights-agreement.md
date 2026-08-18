---
tags: cyber valley, cyberia, legal, draft
alias: land rights agreement, hak sewa agreement, sewa template, land lease draft
crystal-type: pattern
crystal-domain: cyberia
icon: "⚖️"
---
# Land Rights Agreement — Drafting Framework

v0.4.3 · working skeleton, not an executable document

*Changelog: v0.1 initial skeleton · v0.2 §9A Licence Event regime · v0.3 §5A construction control, BAST handover chain and indemnity · v0.3.1 §2.7 plot as per aversionem (ad corpus) · v0.4 holder protocol folded in — §2.5 free assignability and the Register, §9B title warranties, negative pledge, non-disturbance and mirror indemnity, §2.4 renewal by right, §2.6 split into land-time and stay, §6 three-tier build remedy, §8 veto and initiative in place of an Association, §9A full KBLI list from the Articles of Association, §10A force majeure, §10B adat, §2.8 succession, §13 general provisions; Design Code moved to Annex C; clause leaders unbolded per the graph style rule · v0.4.1 §7.4 Design Envelope lock — the signing-to-SLF window, with the Landowner's cure right and exit in both fault and no-fault cases · v0.4.2 §6.0 conditions precedent and the Commencement Certificate — the construction clock starts there, stops when a condition falls away, and carries a long stop; 9B.2 adds pengecekan sertifikat on the day of signing; 9B.7 rewritten as a choice of real security instruments; open questions moved to `legal/notes/open questions.md` · v0.4.3 §2.1 term derived from the Title with automatic extension, 2.1.1–2.1.2 where the term lives and the offer of record, 9B.9 duty to extend Titles in time.*

> Status. Structural draft for discussion with an Indonesian notary (PPAT) and counsel. Nothing here is legal advice. Every clause marked ⚠ carries a known Indonesian-law constraint that must be verified against the current regulations and the actual master title before any version of this is signed. Every clause marked ▲ implements a decision from `holder-protocol-decisions.md` and reverts cleanly if that decision is changed.

Corporate source of authority: Anggaran Dasar / Articles of Association PT. Cyber Valley Estate, 12 August 2026 (Akta Pendirian No. 01, 04-01-2022; PKR No. 13, 14-04-2025; PKR No. 02, 01-07-2025). Where this framework and the Articles diverge, the Articles prevail and this framework is corrected.

Related product pages: [[hak sewa]], [[leasehold upfront]], [[annual leasehold]], [[hak pakai]], [[hak milik]], [[century index]], [[development|city development strategy]].

## Package map

| document | contents |
|---|---|
| this file | framework and operative structure |
| `legal/notes/open questions.md` | release gate and every open item, deliberately outside the signable text |
| Annex A | Estate: one row per land title — certificate number, area, grant and expiry dates, remaining term, RTRW classification, PKKPR number or its absence, LP2B status; plus the KBLI × location table under §9A.1 |
| Annex B | Plot: boundaries (*patok*, adjoining owners, GPS/UTM), indicative area, *peta bidang* |
| [[annex-c-design-code\|Annex C]] | Design Code — the zoning code as numbers |
| Annex D | Community Rules |
| Annex E | Century index annex (T1) — weights, t₀ prices, quantities qᵢ, fixes, collar, floor, worked invoice; also the unamortised-return formula |
| Annex F | Utilities, access and mobility specification |
| Annex G | Permitted-use matrix by Holder class, zone and track |
| Annex H | Condition schedule at site handover (baseline for redelivery, 5A.6 #6) |
| Annex I | Due diligence pack under 9B.2 |
| Annex J | Offer of record under 2.1.2 — the product page and price schedule as they stood, by commit hash and date |

---

## 0. Threshold requirements (apply to every track)

Bilingual execution — mandatory. ⚠ Law No. 24/2009 requires agreements involving an Indonesian party to be executed in Bahasa Indonesia. English-only instruments have been annulled by Indonesian courts. Execute bilingual, with an express clause stating which language prevails on discrepancy (Indonesian text customarily prevails; the parties may agree otherwise but should not assume it will be honoured).

Notarial form. Land leases are executed as *akta sewa* before a notary/PPAT. Private signature agreements are enforceable in principle but weak in practice and unusable for any later BPN procedure.

Anti-nominee. ⚠ Both parties represent that no part of this arrangement is a nominee structure (*perjanjian pinjam nama*). Nominee arrangements violate the Basic Agrarian Law and Art. 1320 Civil Code and are void. Nothing in this framework may be used to simulate freehold for a foreign party, and no Holder may receive shares or share-like economics in exchange for the Plot outside the reviewed joint-venture instrument.

Title subordination. ⚠ There is no single master title. The Estate is assembled from 21 acquisitions; the register of holdings records 18 certificated HGB parcels and three parcels without an HGB certificate (one recorded as *Pipil*, one awaiting certification, one held on agreement only). No right granted may exceed the remaining term of the specific certificate on which the Plot sits. Every term, renewal and option below is expressly capped by, and conditional on, the subsistence and renewal of that certificate. Annex A lists every title with its number, area, grant and expiry dates and remaining term; the recitals name the certificate for this Plot and state its remaining term as a number.

Condition precedent to offering a Plot. ⚠ No Plot is offered, priced or granted unless (a) it sits on a certificated HGB parcel listed in Annex A, and (b) a PKKPR covering the intended use exists for that parcel. Parcels held on *Pipil*, on agreement, or awaiting certification are outside this framework until converted.

Signing authority. Under Articles of Association Pasal 12(2)(c) the Director signs lease agreements and land-rights transfer agreements within KBLI 68111 and 68200 without prior approval. Acts requiring prior written approval of the Board of Commissioners, and in the listed cases also of the GMS, are set out in Pasal 12(3) — in particular encumbrance of land rights (letter b, relevant to §9B.3) and participation in another company (letter e, relevant to the joint-venture instrument). Pasal 12(4) requires separate maker and authorizer roles for every disbursement from the principal revenue account; payment deadlines in this deed are set to accommodate that mandate.

---

## 1. Parties and definitions

| Term | Definition |
|---|---|
| Landowner | PT. CYBER VALLEY ESTATE, an Indonesian limited liability company (PT PMA) domiciled in Gesing, Banjar, Buleleng, Bali; holder of the land titles listed in Annex A; NIB [___] |
| Title | the HGB certificate listed in Annex A on which the Plot sits, named in the recitals |
| Holder | the counterparty; classified at signing as Foreign Holder (non-Indonesian national) or Indonesian Holder (WNI) |
| Estate | the land parcel(s) under the master title, described in Annex A |
| Plot | the demarcated area allocated to the Holder, described by coordinates and site plan in Annex B |
| Improvements | any building or structure erected by the Holder on the Plot |
| Design Code | Annex C, as amended under §7 |
| Community Rules | Annex D |
| Index Annex | Annex E, the century index annex referred to in §2.3 and §2.4 |
| Register | the register of leases maintained by the Landowner under §2.5.8 |
| Estate Certificate | the statement of lease status issued under §2.5.6 |
| Guarantee Fund | the reserve constituted under §9B.7 |
| Community Council | the contractual body of Holders under §8 |
| Licence Event | as defined in §9A.2 |

---

## 2. Part A — Base grant: Hak Sewa (all Holders)

The default product. Available to Foreign and Indonesian Holders alike, with no residency requirement and no minimum-value threshold.

2.1 Grant and term. ▲ The Landowner grants the Holder the right to use and occupy the Plot for [residential / mixed] purposes. The term is derived from the Title under which the Plot was cut, and is not uniform across the Estate:

- initial term = the lesser of [25] years and the remaining term of the Title at signing, less a buffer of [18] months for the extension procedure;
- on each extension (*perpanjangan*) or renewal (*pembaruan*) of the Title, this deed extends automatically by the lesser of [25] years and the new remaining term less the same buffer, with no consideration beyond the price formula in Annex E and no further negotiation;
- the recitals state the certificate number, its expiry date, and the resulting term as a date, not as a duration.

⚠ Where the remaining term less the buffer falls below [__] years, the Plot is not offered under Part A at all until the Title is extended.

2.1.1 Where the term lives. The term is a property of the Plot, not of the product. The shared product pages describe the shape of the instrument; the term as a date appears in three places only — the recitals of this deed, the Register under 2.5.8, and the Estate Certificate under 2.5.6. Price per are is set for the Plot with its term known, so that two Plots on differently-dated Titles are not priced as if identical.

2.1.2 Offer of record. ▲ The product pages are living documents and change as the city develops; what the Holder was told when it decided does not. The version of the product page and price schedule on which the Holder relied is annexed as Annex J, identified by commit hash and date. Later amendment of those pages alters neither this deed nor that annex. Statements in the pages that are commitments — renewal by right, the area revenue charge, the assignment regime, the non-disturbance covenant — change only through this deed and the decision record; statements of current state change freely and bind nothing.

2.2 Nature of the right, and what stands in place of registration. ⚠ Hak Sewa is a contractual right under Indonesian civil law. It is not registered at BPN as a land title and does not appear on the certificate. This is stated in the recitals in those words. ▲ In place of registration the Holder receives, and the Landowner expressly grants:

- a notarial deed and an entry in the Register (§2.5.8);
- the negative pledge and non-disturbance regime (§9B.3–9B.4);
- the covenant that any transferee of the Estate takes subject to this deed (§9B.3);
- the Estate Certificate on demand (§2.5.6), on which a prospective assignee may rely;
- the upgrade path to a registered right after completion — Hak Pakai under §3 or Hak Milik under §4.

No marketing material may describe this instrument as a registered lease.

2.3 Consideration. [Lump sum for full term / annual rent], payable [schedule]. Tax treatment: PPh on lease value at [10%]; PPN and withholding responsibility allocated at §12. ▲ Where consideration is indexed, the obligation is denominated in the century index: what is fixed at signing is the set of quantities qᵢ and the collar and floor, not the amount of any future invoice. The Index Annex (Annex E) carries weights, t₀ prices, quantities, fix sources with fallbacks, collar, floor and one worked invoice, and prevails over prose (thesis T1). The Holder may recompute any invoice from public sources within 30 days and the recomputation prevails (T5). Settlement is in IDR at JISDOR on the invoice date (T6, UU 7/2011). The Index Annex survives assignment, sublease and succession with the same quantities (T7). On divergence between the on-chain fix and the annex computation from named public fixes, the annex computation prevails (T8).

2.4 Renewal by right. ▲ The Holder has the right — not an option subject to the Landowner's agreement — to renew for a further term determined as in 2.1, exercisable between [24] and [12] months before expiry, provided the Holder is not in uncured material default. The renewal price is L(T) = L₀ · I(T)/I(t₀) under the Index Annex. The Landowner may not refuse renewal while the Title subsists. Where the term granted under 2.1 was shortened by the Title rather than by choice, the automatic extension in 2.1 operates first and the renewal right attaches to the extended term.
⚠ The formula must be arithmetic — an index, a benchmark, or a defined valuation method with a named appointing body. "To be agreed" is the single most common defect in Bali leases and renders the option unenforceable in substance. Annex E is that formula; a renewal clause pointing at an empty annex reproduces the defect it warns against.

2.5 Transfer. ▲

2.5.1 Free assignment. The Holder may assign the whole of its interest under this deed to any person without the Landowner's consent, subject to 2.5.3–2.5.8.

2.5.2 Indivisible bundle. What is assigned is one bundle: the hak sewa over the Plot, ownership of the Improvements, membership of the Community Council, the Index Annex with unchanged quantities qᵢ, and all accrued rights and obligations. Separate assignment of any element is prohibited.

2.5.3 Form and notice. Notarial *akta pengalihan hak sewa* / *akta cessie*; written notice to the Landowner with a copy of the deed within 7 days.

2.5.4 Assignee conditions. Written accession to the Design Code, the Community Rules and the Community Council; representations as to absence of nominee arrangement and source of funds. No residency test applies to the assignee.

2.5.5 Transfer fee. [2.0]% of the transaction price, payable on notice, reduced for contribution:

| Holder's position | fee |
|---|---|
| base | [2.0]% |
| built within time, SLF issued | [1.5]% |
| no unremedied Design Code breach for the whole term | [1.0]% |
| soil and water results published to the ledger without gaps | [0.5]% |
| referred residents above the threshold in Annex D | [0]% |
| succession under §2.8 | [0]% |

Right of first refusal exists only in Wave 1 and only until the build obligation under §6 is discharged; it lapses permanently on SLF. Where it applies, its mechanics mirror Articles of Association Pasal 7 for shares: notice stating price and terms, 30 days to respond, right to withdraw the offer after that period.

2.5.6 Estate Certificate. On the Holder's written request the Landowner issues, free of charge and within 10 working days, a certificate stating: remaining term; confirmation of payments and absence of arrears; quantities qᵢ and the latest invoice under the Index Annex; PBG and SLF status; any unremedied Design Code breaches, or confirmation that there are none; status of the master title and of any encumbrance over it at that date. The certificate is valid for 30 days and is a statement on which a prospective assignee may rely.

2.5.7 Deadlines and deemed consent. Every act of the Landowner under this clause is due within 10 working days. Failure to act within that period is deemed consent and confirmation.

2.5.8 Register. The Landowner maintains a register of leases; the entry is evidence of the Holder's rights. Entries may be represented in [[cybergraph]] as particles, with assignments as cyberlinks; state of a lease is public, identity of the Holder is not. On divergence the notarial deed and the Register prevail over the on-chain representation, on the pattern of thesis T8.

2.5.9 Partial assignment and subdivision of the Plot require written consent and compliance with the Design Code.

2.5.10 Taxes on assignment are allocated between assignor and assignee as set out in §12.

2.6 Subletting — two products. ▲ ⚠ The Articles of Association Pasal 3 give the Landowner KBLI 55199 (other short-term accommodation) and 55192 (campgrounds and caravan parks). A Foreign Holder cannot ordinarily hold either. The lease therefore distinguishes:

| product | what it is | licence sits with | estate economics |
|---|---|---|---|
| land-time | hour to season, bare land, no accommodation service supplied | the Holder | area revenue charge of 10%, or 5% where the district is a net exporter of energy, water and food, plus a settlement fee of [1–3]% |
| stay | occupation with an accommodation service | the Landowner, under KBLI 55199 and 55192 | management fee, the Landowner operating |

The Holder elects the channel. Both settle in IDR at JISDOR on the invoice date; where the marketplace quotes in another unit, that unit is a unit of account and not the means of payment (UU 7/2011). Horizon and use remain gated by the Design Code: a day market and a month-long camp are different permitted uses. Definition of revenue, the certification and review cycle for net-exporter status, reporting cadence, audit rights and consequences of understatement are set out in Annex G.

2.7 Plot as a single unit (per aversionem / ad corpus). ⚠ The Plot is leased as one contiguous parcel defined by its boundaries, not by a certified area number.

*Working English formulation (final wording through the notary):*

> The Object is demised as a single land parcel (*per aversionem* / ad corpus) within the boundaries described in Article […] and Annex B, and not by unit of area. Any figure of approximately [1,000] m² is indicative only. The Parties agree to set aside Articles 1588, 1589, 1590, 1591 and 1592 of the Civil Code (KUHPerdata), and there shall be no price adjustment, compensation, or rescission if a later BPN cadastral survey yields a larger or smaller area.

*Indonesian sense-text for notary drafting:*

> Objek disewakan sebagai satu kesatuan bidang tanah (per aversionem) dalam batas-batas sebagaimana diuraikan dalam Pasal … dan Lampiran …, bukan berdasarkan satuan luas. Luas ±[1.000] m² bersifat perkiraan. Para Pihak sepakat mengesampingkan ketentuan Pasal 1588, 1589, 1590, 1591 dan 1592 KUHPerdata, dan tidak ada penyesuaian harga, kompensasi, maupun pembatalan apabila pengukuran kadastral BPN di kemudian hari menghasilkan luas yang lebih besar atau lebih kecil.

Boundary description is mandatory. Without it the clause is empty. Annex B must define boundaries by physical marks (*patok*), adjoining owners by name, and GPS/UTM coordinates; the *peta bidang* / sketch is annexed and initialled by both parties so that the Plot is determinable without reference to area.

What this clause does not do:

1. It does not bind BPN. *Surat Ukur* and any later hak pakai certificate will carry whatever figure BPN measures. The clause protects against monetary revision between the parties; it does not buy the number "[1,000]" onto the certificate.
2. It does not bind third parties. The deed operates *inter partes*. Overlap with a neighbour's certificate, or land falling into *sempadan sungai* / subak / *jalan desa*, is outside this clause. Real boundary fixation is *asas kontradiktur delimitasi*: *Berita Acara Persetujuan Batas* signed by all adjoining owners at the BPN survey.
3. It does not create land. If the ground is physically 900 m², the Holder receives 900 m² and has already waived claims for the shortfall.

Timing. ⚠ Do not lock a pure per aversionem waiver while an already-known shortfall is still unsettled. Signing "no revision" while the parties know the Plot is short donates the difference to the Landowner. Order of operations: first settle the known difference (price recompute / term extension / conversion costs), then in the same addendum fix per aversionem going forward.

Asymmetric option. If the Holder wants downside protection without losing upside surprise: exclude revision on area increase, and on decrease only down to a floor (e.g. 850 m²); below the floor, retain a right to pro-rata reduction. Landowners often accept this more readily than a full bilateral waiver.

2.8 Succession. ▲ On the death of the Holder the interest passes to the heirs by operation of law, with no transfer fee. The heirs accede to the Community Rules within 12 months. Pending accession the interest subsists and the Landowner may not treat the death as a default.

2.9 Security over the Holder's interest. ▲ ⚠ Hak sewa is not an object of *hak tanggungan*: UU 4/1996 Pasal 4 lists Hak Milik, HGU and HGB, and Hak Pakai over state land that is registrable and transferable. A lease right that is not registered at BPN cannot be charged. This clause therefore uses assignment by way of security, not a charge:

- the Holder may assign its interest by way of security (*cessie tot zekerheid*) to a financier, by notarial deed, on written notice to the Landowner;
- the Landowner acknowledges the financier, issues the Estate Certificate to it under 2.5.6, and notifies it of any material breach before terminating, allowing that party the same cure period as the Holder;
- on enforcement the financier takes the whole bundle under 2.5.2 and accedes under 2.5.4; no transfer fee is charged on enforcement, and the fee under 2.5.5 applies on the financier's onward sale.

Confirm the construction with the notary before use. Note the asymmetry this creates and which §9B.3 answers: the Landowner may charge the land under Articles of Association Pasal 12(3)(b), while the Holder cannot charge its lease at all.

---

## 3. Part B — Track F: upgrade to Hak Pakai (Foreign Holders)

⚠ Blocking fork, unresolved. This section and the product page describe two incompatible constructions: hak pakai over land, which requires *pemecahan* of the Plot out of the master title, and a right attaching to a completed structure with the parcel remaining with the Landowner. The parcel cannot both separate and remain. Instrument D is not offered until one construction is chosen, drafted here and described on the product page in the same words.

3.1 Eligibility. ⚠ Requires the Holder to hold a valid KITAS/KITAP for the duration of the right, and the transaction to meet the regional minimum-value threshold. If the permit lapses and is not renewed, the title is exposed.

3.2 Mechanics. [To be settled per the fork above.] Term cycles and extensions under PP 18/2021.

3.3 Trade-offs to be disclosed. Hak Pakai is a registered right and stronger on paper, but: it is residency-dependent; the resale pool is limited to foreigners who themselves qualify, or requires reconversion to a citizen-held title; and it removes the flexibility of §2.5. Many Holders are better served by the base lease. This section exists so the choice is informed, not assumed.

3.4 Costs. Splitting, conversion, BPHTB, notarial and administrative costs borne by the Holder. Upgrade fee to Landowner: [amount].

---

## 4. Part B — Track I: upgrade to title (Indonesian Holders)

4.1 Step 1 — Plot split and sale. On request, the Landowner procures *pemecahan sertifikat* of the Plot and transfers the resulting HGB to the Holder by AJB before the PPAT. Purchase price: [amount / formula], credited [in whole / in part] against sums already paid under Part A.

4.2 Step 2 — Holder's own conversion to Hak Milik. ⚠ The Holder may then apply to BPN to upgrade HGB → Hak Milik. This is the Holder's own application; the Landowner facilitates documents but gives no warranty of outcome. Conditions the Holder must satisfy:

- Indonesian citizenship, natural person;
- the Plot is used as *rumah tinggal* — evidenced by PBG or a *keterangan* from the village head. A bare, unbuilt plot does not qualify. Practice varies between land offices; verify with BPN Buleleng before promising this to anyone;
- plots up to 600 m² follow the simplified route; above 600 m² a *constatering* report is required;
- the Holder declares holdings of no more than 5 residential parcels or 5,000 m² in aggregate.

4.3 Plot sizing. ⚠ Open. The strategy contemplates plots of 5–15 are (500–1,500 m²) and has not settled the Z1 grain; anything above 600 m² leaves the simplified regime and weakens instrument E. Sizing and the grain decision are taken together, not separately.

4.4 Continuing obligations. ⚠ Conversion to Hak Milik does not release the Holder from the Design Code, Community Rules or Community Council membership. These must therefore be secured by instruments that survive the title change — covenants recorded in the AJB, easements over access and utilities, and Council membership as a condition of the sale. Draft this before the first sale; it cannot be imposed retroactively.

---

## 5. Building rights and PBG

5.1 Who builds. The Holder builds at its own cost and risk. The Landowner constructs no Improvements.

5.2 Permits. ⚠ PBG is issued to the holder of the land title. For Foreign Holders on Part A, the applicant is therefore the Landowner. Allocation: the Holder prepares and funds the application, the Landowner applies and cooperates; the Holder indemnifies the Landowner for all consequences of the works. SLF to be obtained on completion.

5.3 No works before permit. The Holder shall commence no construction before PBG issuance. Breach is a material default with immediate cessation rights, because enforcement action against unpermitted structures runs against the title holder, not the occupant.

5.4 Ownership of Improvements. Indonesian law recognises horizontal separation — buildings may be owned separately from land. The parties record that Improvements are owned by the Holder for the term. Consequences at termination: §10.

---

## 5A. Construction control, handover and indemnity

The Landowner does not build, yet remains the title holder and the PBG applicant. This section closes that gap: control proportionate to retained liability.

5A.1 Design and contractor approval. No works until the Landowner has approved (a) the design package for Design Code compliance, (b) the identity of the main contractor, (c) the construction programme. Approval is limited to those matters and creates no design or engineering warranty by the Landowner — say so expressly. Approval or refusal is due within 10 working days; failure to act is deemed approval.

5A.2 Contractor qualification. ⚠ Under UU 2/2017 on Construction Services, construction services must be performed by a qualified provider (*penyedia jasa*) holding a valid SBU and the corresponding KBLI, and the client (*pengguna jasa*) is obliged to engage such a provider. The Holder shall engage only a contractor meeting this standard and shall furnish copies of SBU, licences and the construction contract before commencement.

5A.3 Supervision. An independent construction supervisor (*pengawas* / MK) is appointed [by the Landowner, at the Holder's cost / by the Holder from a Landowner-approved panel], with authority to inspect, to require rectification, and to stop works on material non-compliance. Stage inspections at: foundation, structure, roof, MEP, completion.

5A.4 Insurance. For the construction period, procured by the Holder, naming the Landowner as co-insured / loss payee: Contractors' All Risks (CAR/EAR), third-party liability, workers' accident cover (BPJS Ketenagakerjaan for the workforce). Certificates delivered before commencement; lapse is a stop-work event. From SLF onward the Holder maintains property and public liability cover on the Improvements for the term.

5A.5 Security. [Deposit / bank guarantee] of [__] to secure completion, rectification of defects, and reinstatement if works are abandoned. Released in tranches on the handover milestones below, each release due within [15] working days of the milestone, allowing for the maker/authorizer mandate under Articles of Association Pasal 12(4).

5A.6 Handover chain — the documents that move risk. ⚠ Each transfer of risk must be evidenced by a dated *Berita Acara Serah Terima* (BAST) with photographic and inventory annexes. Absent a BAST, risk is presumed to remain where it was.

| # | Document | Between | What moves |
|---|---|---|---|
| 1 | BAST Lahan (site handover) | Landowner → Holder | possession of the Plot for construction; site safety and security pass to the Holder |
| 2 | PHO — *Berita Acara Serah Terima Pertama* | Contractor → Holder | practical completion; starts the defects liability period (*masa pemeliharaan*), customarily [6–12] months, with retention of [5]% |
| 3 | SLF (see 5A.7) | authority → applicant | public-law confirmation that the building may be occupied |
| 4 | FHO — *Berita Acara Serah Terima Akhir* | Contractor → Holder | end of defects period; retention released |
| 5 | BAST Operasional | Holder ↔ Operator (if any) | day-to-day operation, maintenance, guest liability |
| 6 | BAST Pengembalian (redelivery) | Holder → Landowner at term end | condition on return, measured against Annex H |

5A.7 SLF. Application follows the PBG applicant, therefore the Landowner. The Holder shall fund the process, deliver as-built drawings and test certificates, procure the contractor's cooperation and provide access to the inspecting commission. No occupation or use of any Improvement before SLF issuance. Periodic SLF renewal is treated the same way.

5A.8 Holder's indemnity. The Holder indemnifies the Landowner against all claims, penalties, orders and costs arising from the Holder's works and from the Holder's occupation and use, including: unpermitted works, deviation from PBG, breach of zoning or environmental rules, accidents to workers or third parties, and damage to neighbouring land. The indemnity survives termination for [__] years. Its mirror in favour of the Holder is §9B.5.

5A.9 What the Landowner cannot delegate. ⚠ Regardless of the above, the following follow the title and remain with the Landowner as against the authorities: enforcement action for unpermitted or non-conforming structures; standing as PBG/SLF applicant; and answerability for structural safety. The Holder's indemnity operates between the parties — it does not move public-law liability. This is precisely why 5A.1–5A.5 exist.

---

## 6. Construction timeline and the build obligation

6.0 Conditions precedent and the Commencement Certificate. ▲ The construction clock does not start on the date of grant. It starts on the date of the Commencement Certificate (*Berita Acara Mulai*), a single dated document signed by both parties recording that all of the following Landowner Conditions Precedent are satisfied:

1. the Plot is physically handed over — BAST Lahan under 5A.6 #1;
2. boundaries are accepted — Annex B initialled, *patok* set, *Berita Acara Persetujuan Batas* signed by the adjoining owners on the Estate perimeter and by any *subak*, *desa* or *sempadan* interest;
3. legal access to the Plot subsists — by title or by registered easement, not by tolerated passage;
4. PKKPR and zoning for the parcel confirm the intended use;
5. a PBG application for the approved design is legally capable of being filed;
6. the agreed utility connection points in Annex F are physically ready to the specified capacity;
7. title due diligence is clean — Annex I delivered and the search under 9B.2 clear.

6.0.1 Suspension. If, after the Commencement Certificate, any of 6.0(1)–(7) ceases to be satisfied, the clock stops for the duration and all time-based rights extend day for day. Cessation is notified within [14] days by the party that becomes aware of it.

6.0.2 Symmetry. While the clock is stopped no holding charge accrues under 6.2, and the Design Envelope lock under 7.4.3 extends by the same period — otherwise delay by the Landowner would consume the Holder's protection.

6.0.3 Long stop. ⚠ If the Conditions Precedent are not satisfied within [12] months of signing, the Holder may terminate and recover all sums paid, with [interest / index adjustment under Annex E], secured under 9B.7. Without this the Holder is protected from penalty but its money is held indefinitely.

6.1 Timing. Commence within [12] months of the Commencement Certificate; complete within [24–36] months of it, aligned with what the product pages promise.

6.2 Three-tier remedy. ▲ Escalating, and in this order:

1. Holding charge. On overrun, a charge accruing at [__] per month, rising by [__] every [6] months. The charge is paid into the biosphere and desa tithes under the spending strategy, not into the Landowner's profit — the city loses from delay, so that is where the money goes.
2. Buy-back offer. After [__] months of overrun the Landowner shall offer to acquire the interest at formula price: unamortised prepayment under Annex E plus independent valuation of works actually completed.
3. Reversion. Available only after the Holder declines the buy-back offer or fails to respond within [60] days.

6.3 Purpose. Prevent speculative idle plots and permanent construction sites inside a small community. State the purpose in the recital — it helps enforceability. No Holder loses both the land and the money paid for it.

---

## 7. Design Code (Annex C)

Binding on all Holders, all tracks, all zones. [[annex-c-design-code|Annex C]] states the zoning code as numbers — footprint and floor multiplier, light balance allocation, species density, and the sound, water, light, air and soil limits with their monitoring and publication duties — rather than by cross-reference.

⚠ Bali-specific overlays bind regardless of what the Design Code says: provincial building-height limits, architectural requirements, slope and ravine setbacks, water-catchment restrictions. Estate policy stack: [[cyber-valley/policies/zoning system|zoning code]], [[soil policy]], [[water policy]], [[light policy]], [[sound policy]], [[air policy]], [[carbon policy]].

7.1 Scale of measurement. ▲ Footprint and canopy ratios are measured per Plot.

7.2 Density transfer. ▲ Unused footprint entitlement may be transferred to another Plot within the same district through the Register, subject to the Landowner's check that the district balance in Annex C is maintained, against a settlement fee of [__]%. Transfers open from Wave 2. Entitlement not transferred remains with the Plot.

7.3 Amendment and grandfathering. Amendment by the Landowner. Completed Improvements are grandfathered. Any amendment that would worsen the position of already-built Improvements is subject to the veto in §8.2.

7.4 Design Envelope lock. ▲ Grandfathering under 7.3 and the veto under §8.2 protect what is already built. Between signing and SLF the Holder has paid and has nothing on the ground, and is therefore least protected exactly where it is most exposed. This clause closes that window.

7.4.1 Design Envelope of the Plot means (a) the figures in C2 and C3 of Annex C in the version in force at signing, adjusted for any density transferred under C1.2; (b) the Holder's row in the permitted-use matrix, Annex G; (c) so much of the access and connection specification in Annex F as applies to the Plot. The version of Annex C is identified by version number and content hash and initialled by both parties.

7.4.2 Lock. From signing until SLF plus 12 months the Plot is governed by the Design Envelope in the version in force at signing. Later amendments apply to the Plot only with the Holder's written consent.

7.4.3 Duration and transfer. The lock runs for the period in 7.4.2 and no longer than the build obligation in §6.1 plus 12 months. It transfers with the bundle under 2.5.2 and does not restart on assignment. It lapses with the build obligation, so that an unbuilt Plot cannot freeze the code for the term.

7.4.4 Scope of the Landowner's freedom. The lock is per Plot. The Landowner may amend the Design Code at any time for Plots granted after the amendment, and for Holders whose lock has expired, subject to 7.3 and §8.2.

7.4.5 Material change. A change is material where it: reduces permitted footprint or floor area by more than [10]%; removes a use from the Holder's row in Annex G; or increases the cost of compliance for a design already approved under 5A.1 by more than [10]% of the budgeted construction cost. Fact and amount are certified by the independent supervisor under 5A.3 or an independent valuer; disputes follow §11. Materiality is not determined by the Landowner.

7.4.6 Landowner's cure right. Within 30 days of the Holder's notice the Landowner may withdraw the change as to that Plot, grant a variance, or offer an equivalent Plot. Any of these extinguishes the rights in 7.4.7.

7.4.7 Consequences where the change is not cured. Fault and causation are separated: the trigger is the same, the remedy differs by who caused the change.

| cause of the change | remedy |
|---|---|
| the change originates with the Landowner | the Holder may exit with unamortised prepayment under Annex E, plus the documented value of works completed at independent valuation, plus direct loss; or remain and be compensated in the certified amount of the increased cost |
| the change is required by law, regulation or an act of authority, or by *adat*, *subak* or the *awig-awig* of the *desa adat* | no fault; the Holder may exit with unamortised prepayment plus the value of works completed at independent valuation, without damages; payment is secured by the Guarantee Fund under 9B.7 |

⚠ The Holder's exit right exists in both rows. A regime in which a law-driven change leaves the Holder with nothing loads on the Holder a risk it cannot price, and gives the Landowner a reason to prefer changes that arrive through the regulator. Fault governs damages; it does not govern the exit.

7.4.8 Notice window. The Holder invokes 7.4.7 within 90 days of notification of the change. Silence within that period is acceptance of the change.

7.4.9 Continuity. Signing to SLF: this clause. SLF to end of term: grandfathering under 7.3 and the veto under §8.2. There is no interval in which the Plot is unprotected.

*Indonesian sense-text for notary drafting:*

> Sejak tanggal penandatanganan sampai dengan diterbitkannya SLF ditambah 12 (dua belas) bulan, Bidang Tanah tunduk pada Design Envelope sebagaimana berlaku pada tanggal penandatanganan. Perubahan yang terjadi kemudian hanya berlaku bagi Bidang Tanah tersebut dengan persetujuan tertulis Pemegang Hak.

> Apabila perubahan yang bersifat material tidak dipulihkan sesuai Pasal 7.4.6, Pemegang Hak berhak mengakhiri Perjanjian ini. Apabila perubahan berasal dari Pemilik Tanah, Pemegang Hak berhak atas pengembalian bagian pembayaran yang belum teramortisasi, nilai pekerjaan yang telah dilaksanakan menurut penilaian independen, serta kerugian langsung. Apabila perubahan disebabkan oleh peraturan perundang-undangan, keputusan pejabat yang berwenang, atau ketentuan adat, subak dan awig-awig desa adat, Pemegang Hak berhak atas pengembalian dan nilai pekerjaan tanpa ganti rugi.

---

## 8. Community Council, shared infrastructure and service charge

▲ The Articles of Association know three organs — GMS, Board of Directors, Board of Commissioners — and no residents' body; the preamble and Pasal 3(3) record that residents live under terms and values set by the Company. This deed therefore gives Holders enforceable contractual rights rather than a governing organ.

8.1 Community Council. Contractual body; membership compulsory for all Holders, all tracks; survives assignment and title upgrade. Voting weight [by Plot / by stake in the graph — to be settled]. A separate legal vehicle (*perkumpulan*) is constituted in Phase 3 to hold shared infrastructure, on the community land trust path in the strategy.

8.2 Veto on deterioration. An amendment to the Design Code or the Community Rules that worsens the position of already-completed Improvements requires the consent of [two thirds] of Holders whose Improvements are affected.

8.3 Right of initiative. A proposal supported by [__] of Holders must be considered by the Board of Directors, with a reasoned written answer published in the Register within 30 days. Silence within that period is deemed acceptance of the proposal.

8.4 Service charge. Basis, cap, escalation, audit rights, and the published annual account.

8.5 Landowner's obligations for access roads, drainage, water and power connection points — defined precisely in Annex F, since a Plot without legal access and connections cannot obtain PBG regardless of the lease. Annex F also states the car-free core: vehicles stop at the perimeter mobility hub, and the Holder's access, parking, construction logistics and waste removal are specified there. ⚠ This is a material restriction on use and is disclosed before signing, not after.

8.6 Long-term. Whether shared infrastructure is retained by the Landowner, transferred to the *perkumpulan*, or handed to the municipality.

---

## 9. Representations

Landowner: valid title, no encumbrances beyond those disclosed, zoning permits the intended use, KKPR status disclosed, licences held and their locational scope. Extended warranties: §9B.
Holder: identity and status, source of funds, no nominee arrangement, ability to fund construction.

⚠ Disclose honestly: master-title term and renewal risk, zoning status and any pending change of designation, and that Hak Sewa is unregistered. Non-disclosure here is the fastest route to a void agreement.

### 9A. Licences — warranty and Licence Event regime

9A.1 Warranty. ▲ The Landowner warrants that at the date of this deed it holds a valid NIB and the business licences required for the activity contemplated here, covering the location of the Estate, across the KBLI set out in Articles of Association Pasal 3: 68111 real estate owned or leased · 68200 real estate on a fee or contract basis · 55199 other short-term accommodation · 56101 restaurant · 96122 SPA · 82302 special event organiser · 55192 campgrounds and caravan parks · 93299 other amusement and recreation. Locational scope per KBLI is listed in Annex A as one row per KBLI × business address, taken from the NIB in OSS RBA, stating: KBLI, *alamat usaha*, *skala usaha*, risk class, status of the *perizinan berusaha*, and any PB-UMKU required. ⚠ The known discrepancy — the NIB showing a different location for 68111 than for the other codes — is resolved before any lease is signed, 68111 being the code under which leases are granted. The Landowner undertakes to use reasonable endeavours to maintain them and to file required periodic reporting (including LKPM).

9A.2 Definition. A "Licence Event" means the suspension, revocation, non-renewal or material restriction of any licence of the Landowner necessary for the activity contemplated here.

9A.3 No automatic termination. ⚠ A Licence Event does not of itself constitute a material breach and does not give the Holder a right to terminate, provided the Holder's quiet enjoyment and actual use of the Plot continue undisturbed.

*Rationale — put this in the recitals, not only in counsel's file:* the Landowner's right to grant this lease derives from its land title, not from a business licence; a licence is an administrative requirement whose breach is sanctioned against the Landowner by the authorities, and the parties intend that such an administrative matter shall not cascade into the simultaneous collapse of every agreement across the Estate.

9A.4 Holder's remedies, tiered by actual impact. On a Licence Event the Landowner shall notify the Holder within [14] days, stating cause and cure plan, and:

| Impact on the Holder | Remedy |
|---|---|
| None — occupation and use unaffected | no remedy; Landowner cures within a Cure Period of [180] days, extendable while cure is diligently pursued |
| Landowner cannot process the Holder's PBG application or perform another agreed act | suspension of the corresponding Holder obligation and of construction deadlines under §6; time-based rights extended day for day |
| Holder actually deprived of use or occupation for more than [90] consecutive days | rent abatement pro rata; thereafter termination with return of the unamortised prepaid portion per Annex E, secured by the Guarantee Fund |

9A.5 Landowner's obligations during a Licence Event. Diligent pursuit of cure; [quarterly] progress reporting to the Holder or the Community Council; no new grants over the Estate while the impediment subsists if making them would aggravate the position.

9A.6 Carve-out. ⚠ §§9A.3–9A.4 do not apply where the Licence Event results from the Landowner's fraud, wilful misconduct, or failure to remedy after repeated written warnings from the authorities. Protection against administrative accidents is legitimate; a shield against neglect is not — and a clause drafted as the latter invites a court to disregard the whole of §9A.

9A.7 Holder's own licences. Any licence required for the Holder's own activity on the Plot is the Holder's responsibility, subject to the land-time / stay split in §2.6. The Landowner's licences do not extend to land-time activity.

9A.8 Severability of consequences. A Licence Event affecting one KBLI or one location does not, of itself, affect obligations under this deed that do not depend on that licence.

### 9B. Title warranties, negative pledge and indemnity ▲

9B.1 Warranties of the Landowner, given at signing and repeated on each anniversary and on the date of each assignment in favour of the assignee:

- the Company is duly incorporated and subsisting, its issued capital is fully paid, its NIB is valid;
- the Title is a valid HGB certificate; its number, grant date, expiry date and remaining term are disclosed in Annex A and stated in the recitals as a number;
- a PKKPR covering the intended use subsists for the parcel and is annexed; the Plot does not sit on land recorded as *Pipil*, uncertificated or held on agreement;
- the Plot is free of *hak tanggungan*, attachment (*sita*) and other encumbrances; has not previously been let, promised under a PPJB, optioned or otherwise committed; and is not in the physical possession of a third party;
- there are no judicial, administrative or arbitral proceedings, and no asserted adat, subak or desa claims, affecting the Plot;
- zoning and KKPR permit the intended use; the Plot carries no LP2B designation and falls outside *sempadan*;
- PBB is paid and no arrears subsist;
- the chain of title documents is disclosed.

9B.2 Due diligence pack and the search at signing. Annex I, delivered before signing: certified copy of the Title certificate, *Surat Ukur*, NIB, PBB receipts, a BPN non-encumbrance search dated no more than 30 days before signing, and the PKKPR document. In addition, and as a condition of execution, the PPAT performs *pengecekan sertifikat* at BPN on the day of signing and the result is recited in the deed. The Landowner warrants that nothing has been created over the Plot between the search and signing.

9B.3 Negative pledge and binding on successors. The Landowner shall not, without the Holder's written consent: encumber the Plot with *hak tanggungan* or other security; grant competing rights over the Plot; or dispose of the Plot otherwise than subject to this deed, the transferee taking bound by it.
⚠ Articles of Association Pasal 12(3)(b) permits the Company to encumber land and land rights with the approval of the Board of Commissioners and, per that paragraph, of the GMS. Without this clause the corporate constitution allows the land beneath the leases to be charged without the Holder ever being told.

9B.4 Non-disturbance. Where an encumbrance is nevertheless granted, it is permitted only if the secured party confirms in writing that this deed survives enforcement and binds a purchaser at auction. Holders are notified no later than 30 days before the encumbrance is granted, and the Register is updated. For the period an encumbrance subsists, the area revenue charge under §2.6 is reduced by [__] percentage points.

9B.5 Indemnity in favour of the Holder — the mirror of §5A.8. The Landowner indemnifies the Holder against loss, cost, penalty and reasonable legal expense arising from: breach of the warranties in 9B.1; third-party rights subsisting at signing; enforcement of security over the Plot; loss or non-renewal of the master title otherwise than through the Holder's act; and inability to obtain PBG or SLF for reasons attributable to the Landowner's title or licences. Cap: sums paid by the Holder plus the valuation of Improvements under 9B.6. Claims may be brought within [__] years after termination.

9B.6 Remedies for title defect:

| situation | remedy |
|---|---|
| defect curable within 90 days, use unaffected | cure at the Landowner's cost; §6 deadlines suspended and time-based rights extended day for day |
| Holder deprived of use for more than 90 consecutive days | pro-rata abatement for the period |
| deprivation exceeding 180 days, or incurable defect | termination for the Landowner's default, with payment of unamortised prepayment under Annex E, plus the documented value of Improvements at independent valuation, plus direct loss |

9B.7 Security for the Landowner's payment obligations. ⚠ Open, and the weakest point in this framework. A reserve held on the Company's own account is not insolvency-remote: it is the Company's asset and ranks with its other creditors, and its release requires two signatures that are both the Company's under Articles of Association Pasal 12(4). Denominating it in the [[century index]] does not cure either defect, and settlement must in any event be in IDR.

The construction is chosen from, and may combine:

| instrument | strength | cost |
|---|---|---|
| bank guarantee or standby LC in favour of each Holder | independent of the Company's solvency; called on stated documents | bank limit and annual fee |
| escrow with the notary, released on an arbitral award or agreed trigger | outside the Company's estate; neutral releaser | escrow fee, slower release |
| shareholder guarantee | only as good as the guarantor; requires disclosed financials | cheap, weak |
| reserve on the Company's account | treasury policy, not security | none |

Position taken here, pending confirmation: escrow with the notary up to [threshold] of aggregate exposure, bank guarantee above it; the century-index reserve continues as treasury policy under the spending strategy and is not described to Holders as security. Beneficiary, trigger documents, the enforcement path where the Company does not sign, currency, and tax treatment are settled with counsel before any payment is taken.

This clause secures payments under 6.0.3, 9A.4, 9B.5, 9B.6 and §10.

9B.8 Scope. The warranties in 9B.1 are given without a knowledge qualification save where expressly marked.

9B.9 Title continuity. ▲ Because the term of every lease is derived from its Title under 2.1, the product depends on the Titles actually being extended. The Landowner therefore:

- maintains a title calendar in the Register showing, for each Title, the expiry date and the date by which an extension application must be filed;
- files each application within the statutory window and no later than [12] months before expiry, and pursues it diligently;
- reports progress annually in the Register under 10.3.

Failure to file in time is a breach to which 9B.5 and 9B.6 apply. Allowing a Title to lapse so that only *pembaruan* remains available is the Landowner's default and is not treated as a no-fault event under 7.4.7 or 10.3.

---

## 10. Termination and end of term

10.1 Default and cure mechanics for both sides, with equal notice and cure periods.

10.2 Fate of Improvements. ▲ At natural expiry without renewal, Improvements pass to the Landowner against compensation at independent valuation. The Holder may instead elect to remove them within [__] months. On termination for the Landowner's default, 9B.6 applies. On termination for the Holder's default, compensation is reduced by the Landowner's documented loss.
The free-reversion option is not used: the strategy records that buildings and use-rights trade while the land does not, and free reversion would take back the part that trades.

10.3 Master-title failure. Consequences if the HGB is not renewed: compensation under 10.2 plus unamortised prepayment under Annex E, secured by the Guarantee Fund. ▲ The status of the master title and the progress of its renewal are published in the Register annually.

---

## 10A. Force majeure ▲

Definition covering volcanic activity, earthquake, landslide, extreme weather, flood, epidemic, and act of authority. Suspension of affected obligations, day-for-day extension of time-based rights, notice and mitigation duties, and a termination right without fault for either party where the event subsists beyond [__] months. Allocation of loss and the interaction with the insurance under 5A.4 stated expressly. ⚠ The Estate sits on a volcanic slope at 1,200–1,500 m with a pronounced wet season; this clause is not boilerplate here.

## 10B. Adat, subak and desa ▲

Compliance with *awig-awig* of the *desa adat*, the *banjar* and *subak* arrangements affecting the Estate; ceremonial access and processional routes; the customary contributions expected of residents; and the interaction of these with the Design Code. ⚠ On Bali customary law binds land use in practice regardless of the certificate; a deed silent on it transfers an unpriced risk to the Holder.

---

## 11. Dispute resolution

Governing law: Indonesian. Escalation: negotiation → mediation → [BANI arbitration in Jakarta/Denpasar, in English and Indonesian / District Court of Singaraja, whose jurisdiction covers the Company's domicile under Articles of Association Pasal 1]. Language of proceedings. Interim relief.

## 12. Taxes, currency and costs

Allocate expressly: PPh on lease value; PPN on the lease and on services; BPHTB and PPh on any title transfer; taxes on assignment under §2.5.10; regional accommodation tax on stay activity under §2.6; notarial and PPAT fees; splitting and conversion costs; annual PBB; service charge. State whether prices are gross or net of tax, and name the withholding agent consistently with Articles of Association Pasal 12(6).

Currency. Obligations may be denominated in the century index; invoicing and settlement are in IDR at JISDOR on the invoice date (UU 7/2011). Any other unit appearing in marketplace or estate systems is a unit of account only.

## 13. General provisions ▲

Notices and their language · personal data, covering publication of monitoring results to the ledger under Annex C and entries in the Register · KYC and source-of-funds procedure supporting the §9 representation · entire agreement · severability · counterparts and electronic signature · quiet enjoyment as a positive covenant of the Landowner.

---

## Open drafting questions

Moved to [[open questions]] (`legal/notes/open questions.md`) so that they cannot travel into a signable text. Nothing is drafted for execution while an item there is open against the clause being drafted.

## Decision map

▲ clauses implement `holder-protocol-decisions.md`: D1 → 2.5.1–2.5.5 · D2 → 2.5.6–2.5.8 · D3 → 9B.3–9B.4 · D4 → 9B.7 · D5 → 2.2 · D6 → 2.3 · D7 → 7.1–7.2 · D8 → 6.2 · D9 → 2.4, 10.2, 10.3 · D10 → 2.6 · D11 → 8.1–8.3 · D12 → 9B.5 · D13 → 7.4. Recommended variants are drafted; changing a decision changes only the clauses listed against it.

## Notes for counsel / PPAT

- Not legal advice. English is the working language of this skeleton; the executable instrument is drafted RU-EN-ID in parallel columns, with the Indonesian column written alongside the others rather than translated afterwards, and prevailing under Law 24/2009 unless the parties agree otherwise and accept the risk.
- Arts. 1588–1592 KUHPerdata (area shortfall) are treated here as dispositive; confirm numbering and character before use.
- Concrete articles and final wording through the notary — preferably not only the notary proposed by the Landowner alone.
