---
tags: cyber valley, cyberia, legal, draft
alias: land rights agreement, hak sewa agreement, sewa template, land lease draft, land-rights-agreement
crystal-type: pattern
crystal-domain: cyberia
icon: "⚖️"
---
# Land Rights Agreement — Drafting Framework

v0.4.3 · working skeleton, not an executable document

*Changelog: v0.1 initial skeleton · v0.2 [§9A](#9a-licences-warranty-and-licence-event-regime) Licence Event regime · v0.3 [§5A](#5a-construction-control-handover-and-indemnity) construction control, [[bast|BAST]] handover chain and indemnity · v0.3.1 [§2.7](#2-part-a-base-grant-hak-sewa-all-holders) plot as per aversionem (ad corpus) · v0.4 holder protocol folded in — [§2.5](#2-part-a-base-grant-hak-sewa-all-holders) free assignability and the Register, [§9B](#9b-title-warranties-negative-pledge-and-indemnity) title warranties, negative pledge, non-disturbance and mirror indemnity, [§2.4](#2-part-a-base-grant-hak-sewa-all-holders) renewal by right, [§2.6](#2-part-a-base-grant-hak-sewa-all-holders) split into land-time and stay, [§6](#6-construction-timeline-and-the-build-obligation) three-tier build remedy, [§8](#8-community-council-shared-infrastructure-and-service-charge) veto and initiative in place of an Association, [§9A](#9a-licences-warranty-and-licence-event-regime) full [[kbli|KBLI]] list from the Articles of Association, [§10A](#10a-force-majeure) force majeure, [§10B](#10b-adat-subak-and-desa) adat, [§2.8](#2-part-a-base-grant-hak-sewa-all-holders) succession, [§13](#13-general-provisions) general provisions; Design Code moved to Annex C; clause leaders unbolded per the graph style rule · v0.4.1 [§7.4](#7-design-code-annex-c) Design Envelope lock — the signing-to-SLF window, with the Landowner's cure right and exit in both fault and no-fault cases · v0.4.2 [§6.0](#6-construction-timeline-and-the-build-obligation) conditions precedent and the Commencement Certificate — the construction clock starts there, stops when a condition falls away, and carries a long stop; 9B.2 adds pengecekan sertifikat on the day of signing; 9B.7 rewritten as a choice of real security instruments; open questions moved to `legal/notes/open questions.md` · v0.4.3 [§2.1](#2-part-a-base-grant-hak-sewa-all-holders) term derived from the Title with automatic extension, 2.1.1–2.1.2 where the term lives and the offer of record, 9B.9 duty to extend Titles in time.*

> Status. Structural draft for discussion with an Indonesian notary ([[ppat|PPAT]]) and counsel. Nothing here is legal advice. Every clause marked ⚠ carries a known Indonesian-law constraint that must be verified against the current regulations and the actual master title before any version of this is signed. Every clause marked ▲ implements a decision from `holder protocol decisions.md` and reverts cleanly if that decision is changed.

Corporate source of authority: Anggaran Dasar / Articles of Association PT. Cyber Valley Estate, 12 August 2026 (Akta Pendirian No. 01, 04-01-2022; PKR No. 13, 14-04-2025; PKR No. 02, 01-07-2025). Where this framework and the Articles diverge, the Articles prevail and this framework is corrected.

Related product pages: [[hak sewa]], [[leasehold upfront]], [[annual leasehold]], [[hak pakai]], [[hak milik]], [[century index]], [[development|city development strategy]].

## Package map

| document | contents |
|---|---|
| this file | framework and operative structure |
| `legal/notes/open questions.md` | release gate and every open item, deliberately outside the signable text |
| [[annex a estate registry|Annex A]] | Estate: one row per land title — certificate number, area, grant and expiry dates, remaining term, [[rtrw|RTRW]] classification, [[pkkpr|PKKPR]] number or its absence, [[lp2b|LP2B]] status; plus the KBLI × location table under [§9A.1](#9a-licences-warranty-and-licence-event-regime) |
| [[annex b plot boundary|Annex B]] | Plot: boundaries (*patok*, adjoining owners, GPS/UTM), indicative area, *peta bidang* |
| [[annex c design code|Annex C]] | Design Code — the zoning code as numbers |
| [[annex d community rules|Annex D]] | Community Rules |
| [[annex e century index|Annex E]] | Century index annex (T1) — weights, t₀ prices, quantities qᵢ, fixes, floor, worked invoice; also the unamortised-return formula |
| [[annex f utilities access mobility|Annex F]] | Utilities, access and mobility specification |
| [[annex g permitted use|Annex G]] | Permitted-use matrix by Holder class, zone and track |
| [[annex h handover condition|Annex H]] | Condition schedule at site handover (baseline for redelivery, 5A.6 #6) |
| [[annex i due diligence pack|Annex I]] | Due diligence pack under 9B.2 |
| [[annex j offer of record|Annex J]] | Offer of record under 2.1.2 — the product page and price schedule as they stood, by commit hash and date |

---

## 0. Threshold requirements (apply to every track)

Bilingual execution — mandatory. ⚠ [[uu 24-2009 bahasa|UU 24/2009]] requires agreements involving an Indonesian party to be executed in Bahasa Indonesia. English-only instruments have been annulled by Indonesian courts. Execute bilingual, with an express clause stating which language prevails on discrepancy (Indonesian text customarily prevails; the parties may agree otherwise but should not assume it will be honoured).

Notarial form. Land leases are executed as *akta sewa* before a notary/PPAT. Private signature agreements are enforceable in principle but weak in practice and unusable for any later [[bpn|BPN]] procedure.

Anti-nominee. ⚠ Both parties represent that no part of this arrangement is a nominee structure (*perjanjian pinjam nama*). Nominee arrangements violate the Basic Agrarian Law and Art. 1320 Civil Code and are void. Nothing in this framework may be used to simulate freehold for a foreign party, and no Holder may receive shares or share-like economics in exchange for the Plot outside the reviewed joint-venture instrument.

Title subordination. ⚠ There is no single master title. The Estate is assembled from 21 acquisitions; the register of holdings records 18 certificated [[hgb|HGB]] parcels and three parcels without an HGB certificate (one recorded as *Pipil*, one awaiting certification, one held on agreement only). No right granted may exceed the remaining term of the specific certificate on which the Plot sits. Every term, renewal and option below is expressly capped by, and conditional on, the subsistence and renewal of that certificate. Annex A lists every title with its number, area, grant and expiry dates and remaining term; the recitals name the certificate for this Plot and state its remaining term as a number.

Condition precedent to offering a Plot. ⚠ No Plot is offered, priced or granted unless (a) it sits on a certificated HGB parcel listed in Annex A, and (b) a PKKPR covering the intended use exists for that parcel. Parcels held on *Pipil*, on agreement, or awaiting certification are outside this framework until converted.

Signing authority. Under Articles of Association Pasal 12(2)(c) the Director signs lease agreements and land-rights transfer agreements within KBLI 68111 and 68200 without prior approval, subject to Pasal 12(2)'s own checklist marker. Pasal 12(3) prohibits the Company from borrowing or encumbering its assets, land included, outright; establishing a new business or participating in another company requires the prior written approval of the Board of Commissioners — a joint-venture contribution of a lease is governed by the JV instrument itself, not by this Article. [[shareholders agreement]] Article 6 requires separate maker and authorizer roles for every disbursement from the principal revenue account; payment deadlines in this deed are set to accommodate that mandate.

---

## 1. Parties and definitions

| Term | Definition |
|---|---|
| Landowner | PT. CYBER VALLEY ESTATE, an Indonesian limited liability company (PT [[pma|PMA]]) domiciled in Gesing, Banjar, Buleleng, Bali; holder of the land titles listed in Annex A; [[nib|NIB]] [___] |
| Title | the HGB certificate listed in Annex A on which the Plot sits, named in the recitals |
| Holder | the counterparty; classified at signing as Foreign Holder (non-Indonesian national) or Indonesian Holder (WNI) |
| Estate | the land parcel(s) under the master title, described in Annex A |
| Plot | the demarcated area allocated to the Holder, described by coordinates and site plan in Annex B |
| Improvements | any building or structure erected by the Holder on the Plot |
| Design Code | [[annex c design code|Annex C]], as amended under [§7](#7-design-code-annex-c) |
| Community Rules | [[annex d community rules|Annex D]] |
| Index Annex | [[annex e century index|Annex E]], the century index annex referred to in [§2.3](#2-part-a-base-grant-hak-sewa-all-holders) and [§2.4](#2-part-a-base-grant-hak-sewa-all-holders) |
| Register | the register of leases maintained by the Landowner under [§2.5.8](#2-part-a-base-grant-hak-sewa-all-holders) |
| Estate Certificate | the statement of lease status issued under [§2.5.6](#2-part-a-base-grant-hak-sewa-all-holders) |
| Guarantee Fund | the reserve constituted under [§9B.7](#9b-title-warranties-negative-pledge-and-indemnity) |
| Community Council | the contractual body of Holders under [§8](#8-community-council-shared-infrastructure-and-service-charge) |
| Licence Event | as defined in [§9A.2](#9a-licences-warranty-and-licence-event-regime) |

---

## 2. Part A — Base grant: Hak Sewa (all Holders)

The default product. Available to Foreign and Indonesian Holders alike, with no residency requirement and no minimum-value threshold.

2.1 Grant and term. ▲ The Landowner grants the Holder the right to use and occupy the Plot for [residential / mixed] purposes. The term is derived from the Title under which the Plot was cut, and is not uniform across the Estate:

- initial term = the lesser of [25] years and the remaining term of the Title at signing, less a buffer of [18] months for the extension procedure;
- on each extension (*perpanjangan*) or renewal (*pembaruan*) of the Title, this deed extends automatically by the lesser of [25] years and the new remaining term less the same buffer, with no consideration beyond the price formula in Annex E and no further negotiation;
- the recitals state the certificate number, its expiry date, and the resulting term as a date, not as a duration.

The Landowner covenants to apply for extension and, where extension is exhausted, for renewal of each Title within the windows in [[pp 18-2021 hak atas tanah|PP 18/2021]] [Pasal 41](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-41-when-to-apply), and to pursue the application diligently at its own cost. What the Landowner cannot promise is the outcome: after the extension cycle the land returns to the State and the former holder has a priority on stated conditions under [Pasal 37(4)](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-37-the-term), not a right. The Holder is told this in those words before signing, and the deed states for the Plot the date to which the term is certain and the date to which it depends on renewal.

2.1.1 Where the term lives. The term is a property of the Plot, not of the product. The shared product pages describe the shape of the instrument; the term as a date appears in three places only — the recitals of this deed, the Register under 2.5.8, and the Estate Certificate under 2.5.6. Price per are is set for the Plot with its term known, so that two Plots on differently-dated Titles are not priced as if identical.

2.1.2 Offer of record. ▲ The product pages are living documents and change as the city develops; what the Holder was told when it decided does not. The version of the product page and price schedule on which the Holder relied is annexed as Annex J, identified by commit hash and date. Later amendment of those pages alters neither this deed nor that annex. Statements in the pages that are commitments — renewal by right, the area revenue charge, the assignment regime, the non-disturbance covenant — change only through this deed and the decision record; statements of current state change freely and bind nothing.

2.2 Nature of the right, and what stands in place of registration. ⚠ Hak Sewa is a contractual right under Indonesian civil law. It is not registered at BPN as a land title and does not appear on the certificate. This is stated in the recitals in those words. ▲ In place of registration the Holder receives, and the Landowner expressly grants:

- a notarial deed and an entry in the Register ([§2.5.8](#2-part-a-base-grant-hak-sewa-all-holders));
- the negative pledge and non-disturbance regime ([§9B.3–9B.4](#9b-title-warranties-negative-pledge-and-indemnity));
- the covenant that any transferee of the Estate takes subject to this deed ([§9B.3](#9b-title-warranties-negative-pledge-and-indemnity));
- the Estate Certificate on demand ([§2.5.6](#2-part-a-base-grant-hak-sewa-all-holders)), on which a prospective assignee may rely;
- the upgrade path to a registered right after completion — Hak Pakai under [§3](#3-part-b-track-f-upgrade-to-hak-pakai-foreign-holders) or Hak Milik under [§4](#4-part-b-track-i-upgrade-to-title-indonesian-holders).

No marketing material may describe this instrument as a registered lease.

2.3 Consideration. [Lump sum for full term / annual rent], payable [schedule]. Tax treatment: PPh on lease value at [10%]; PPN and withholding responsibility allocated at [§12](#12-taxes-currency-and-costs). ▲ Where consideration is indexed, the obligation is denominated in the century index: what is fixed at signing is the set of quantities qᵢ and the floor, not the amount of any future invoice; the basket tracks uncapped, subject only to the floor. The Index Annex (Annex E) carries weights, t₀ prices, quantities, fix sources with fallbacks, floor and one worked invoice, and prevails over prose (thesis T1). The Holder may recompute any invoice from public sources within 30 days and the recomputation prevails (T5). Settlement is in IDR at [[jisdor|JISDOR]] on the invoice date (T6, [[uu 7-2011 mata uang|UU 7/2011]]). The Index Annex survives assignment, sublease and succession with the same quantities (T7). On divergence between the on-chain fix and the annex computation from named public fixes, the annex computation prevails (T8).

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
| built within time, [[slf|SLF]] issued | [1.5]% |
| no unremedied Design Code breach for the whole term | [1.0]% |
| soil and water results published to the ledger without gaps | [0.5]% |
| referred residents above the threshold in Annex D | [0]% |
| succession under [§2.8](#2-part-a-base-grant-hak-sewa-all-holders) | [0]% |

Right of first refusal exists only in Wave 1 and only until the build obligation under [§6](#6-construction-timeline-and-the-build-obligation) is discharged; it lapses permanently on SLF. Where it applies, its mechanics mirror the share [[rofr|ROFR]] of the pack: a notice stating price and terms, a 30-day offer period and a 3-day window to take up the offer as [[shareholders agreement|the shareholders agreement]] [Article 1](/cyber-valley/cve/legal/shareholders-agreement/shareholders-agreement#article-1-right-of-first-refusal) sets them, the 3 days matching [[articles of association]] [Article 7(4)](/cyber-valley/cve/legal/articles-of-association/articles-of-association#article-7-transfer-of-shares); right to withdraw the offer thereafter.

2.5.6 Estate Certificate. On the Holder's written request the Landowner issues, free of charge and within 10 working days, a certificate stating: remaining term; confirmation of payments and absence of arrears; quantities qᵢ and the latest invoice under the Index Annex; [[pbg|PBG]] and SLF status; any unremedied Design Code breaches, or confirmation that there are none; status of the master title and of any encumbrance over it at that date. The certificate is valid for 30 days and is a statement on which a prospective assignee may rely.

2.5.7 Deadlines and deemed consent. Every act of the Landowner under this clause is due within 10 working days. Failure to act within that period is deemed consent and confirmation.

2.5.8 Register. The Landowner maintains a register of leases; the entry is evidence of the Holder's rights. Entries may be represented in [[soft3/cybergraph|cybergraph]] as particles, with assignments as cyberlinks; state of a lease is public, identity of the Holder is not. On divergence the notarial deed and the Register prevail over the on-chain representation, on the pattern of thesis T8.

2.5.9 Partial assignment and subdivision of the Plot require written consent and compliance with the Design Code.

2.5.10 Taxes on assignment are allocated between assignor and assignee as set out in [§12](#12-taxes-currency-and-costs).

2.6 Subletting — two products. ▲ ⚠ The Articles of Association Pasal 3 give the Landowner KBLI 55199 (other short-term accommodation) and 55192 (campgrounds and caravan parks). A Foreign Holder cannot ordinarily hold either. The lease therefore distinguishes:

| product | what it is | licence sits with | estate economics |
|---|---|---|---|
| land-time | hour to season, bare land, no accommodation service supplied | the Holder | area revenue charge of 10%, or 5% where the district is a net exporter of energy, water and food, plus a settlement fee of [1–3]% |
| stay | occupation with an accommodation service | the Landowner, under KBLI 55199 and 55192 | management fee, the Landowner operating |

The Holder elects the channel. Both settle in IDR at JISDOR on the invoice date; where the marketplace quotes in another unit, that unit is a unit of account and not the means of payment ([[uu 7-2011 mata uang|UU 7/2011]]). Horizon and use remain gated by the Design Code: a day market and a month-long camp are different permitted uses. Definition of revenue, the certification and review cycle for net-exporter status, reporting cadence, audit rights and consequences of understatement are set out in Annex G.

2.7 Plot as a single unit ([[per aversionem lineage|per aversionem]] / ad corpus). ⚠ The Plot is leased as one contiguous parcel defined by its boundaries, not by a certified area number.

*Working English formulation (final wording through the notary):*

> The Object is demised as a single land parcel (*per aversionem* / ad corpus) within the boundaries described in Article […] and Annex B, and not by unit of area. Any figure of approximately [1,000] m² is indicative only. The Parties agree, as [Article 1486](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale) of the Civil Code ([[kuhperdata|KUHPerdata]]) permits in its closing words, that the stated measure gives neither Party any claim, and that the one-twentieth threshold in that Article does not apply between them. [Article 1588](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1588-1592-special-rules-for-a-lease-of-land) is set aside to the same effect for the lease, and Articles 1589 to 1592, which govern an agricultural tenancy, do not apply to this demise. There shall be no price adjustment, compensation, or rescission if a later [[bpn|BPN]] cadastral survey yields a larger or smaller area, and any claim that would otherwise arise is barred one year after delivery under [Article 1489](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale).

*Indonesian sense-text for notary drafting:*

> Objek disewakan sebagai satu kesatuan bidang tanah (per aversionem) dalam batas-batas sebagaimana diuraikan dalam Pasal … dan Lampiran …, bukan berdasarkan satuan luas. Luas ±[1.000] m² bersifat perkiraan. Sebagaimana dimungkinkan oleh kalimat penutup [Pasal 1486](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale) [[kuhperdata|KUHPerdata]], Para Pihak sepakat bahwa penyebutan ukuran tidak menimbulkan tuntutan apa pun bagi masing-masing Pihak dan bahwa batas seperdua puluh dalam Pasal tersebut tidak berlaku di antara mereka. [Pasal 1588](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1588-1592-special-rules-for-a-lease-of-land) dikesampingkan dengan akibat yang sama untuk sewa ini, dan [Pasal 1589](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1588-1592-special-rules-for-a-lease-of-land) sampai dengan [Pasal 1592](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1588-1592-special-rules-for-a-lease-of-land), yang mengatur sewa tanah pertanian, tidak berlaku terhadap sewa ini. Tidak ada penyesuaian harga, kompensasi, maupun pembatalan apabila pengukuran kadastral BPN di kemudian hari menghasilkan luas yang lebih besar atau lebih kecil, dan setiap tuntutan yang mungkin timbul gugur satu tahun setelah penyerahan berdasarkan [Pasal 1489](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale).

Boundary description is mandatory. Without it the clause is empty. Annex B must define boundaries by physical marks (*patok*), adjoining owners by name, and GPS/UTM coordinates; the *peta bidang* / sketch is annexed and initialled by both parties so that the Plot is determinable without reference to area.

What this clause does not do:

1. It does not bind BPN. *Surat Ukur* and any later hak pakai certificate will carry whatever figure BPN measures. The clause protects against monetary revision between the parties; it does not buy the number "[1,000]" onto the certificate.
2. It does not bind third parties. The deed operates *inter partes*. Overlap with a neighbour's certificate, or land falling into *sempadan sungai* / subak / *jalan desa*, is outside this clause. Real boundary fixation is *asas kontradiktur delimitasi*: *Berita Acara Persetujuan Batas* signed by all adjoining owners at the BPN survey.
3. It does not create land. If the ground is physically 900 m², the Holder receives 900 m² and has already waived claims for the shortfall.

Timing. ⚠ Do not lock a pure per aversionem waiver while an already-known shortfall is still unsettled. Signing "no revision" while the parties know the Plot is short donates the difference to the Landowner. Order of operations: first settle the known difference (price recompute / term extension / conversion costs), then in the same addendum fix per aversionem going forward.

Where the Plot is sold rather than leased — Part B — the same articles apply directly: [Pasal 1486](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale) as the rule, [Pasal 1487](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale) for the buyer's election on excess, [Pasal 1489](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale) for the one-year cut-off, and [Pasal 1490](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale) where two Plots are sold in one deed. [Pasal 1490](/cyber-valley/cve/legal/laws/kuhperdata#pasal-1484-1490-area-stated-in-a-sale) settles price between the two; it does not affect any statutory limit on the number of parcels a person may hold.

Asymmetric option. If the Holder wants downside protection without losing upside surprise: exclude revision on area increase, and on decrease only down to a floor (e.g. 850 m²); below the floor, retain a right to pro-rata reduction. Landowners often accept this more readily than a full bilateral waiver.

2.8 Succession. ▲ On the death of the Holder the interest passes to the heirs by operation of law, with no transfer fee. The heirs accede to the Community Rules within 12 months. Pending accession the interest subsists and the Landowner may not treat the death as a default.

2.9 Security over the Holder's interest. ▲ ⚠ Hak sewa is not an object of *hak tanggungan*: [[uu 4-1996 hak tanggungan|UU 4/1996]] Pasal 4 lists Hak Milik, HGU and HGB, and Hak Pakai over state land that is registrable and transferable. A lease right that is not registered at BPN cannot be charged. This clause therefore uses assignment by way of security, not a charge:

- the Holder may assign its interest by way of security (*cessie tot zekerheid*) to a financier, by notarial deed, on written notice to the Landowner;
- the Landowner acknowledges the financier, issues the Estate Certificate to it under 2.5.6, and notifies it of any material breach before terminating, allowing that party the same cure period as the Holder;
- on enforcement the financier takes the whole bundle under 2.5.2 and accedes under 2.5.4; no transfer fee is charged on enforcement, and the fee under 2.5.5 applies on the financier's onward sale.

Confirm the construction with the notary before use. [[articles of association]] Article 12(3) prohibits the Company from charging its land at all, by the nature of its constitution; [§9B.3](#9b-title-warranties-negative-pledge-and-indemnity) is the Holder's own contractual backstop on top of that. The Holder still cannot charge its lease at all — this clause exists to give it a route regardless.

---

## 3. Part B — Track F: upgrade to Hak Pakai (Foreign Holders)

The construction is settled: the Plot is split out of the Landowner's master title and the Holder takes a *hak pakai* over it. The Plot leaves the Landowner's [[hgb|HGB]]; the Holder's obligations under this deed stay with him by contract, not by title.

3.1 Route. One route, in this order: the Holder pays the upgrade fee and the costs of the procedure; *pemecahan* of the Plot out of the master [[hgb|HGB]] at [[bpn|BPN]], on which a separate certificate issues for the Plot and a new HGB certificate issues to the Landowner for the remainder; *perubahan hak* over the split parcel from HGB to Hak Pakai, registered in the Holder's name. A foreign individual cannot hold HGB at any moment of the chain, and a Hak Pakai cannot be carved out of an HGB that stays in place. The office's practice on the sequence is obtained in writing before the first application.

3.2 Eligibility. The Holder holds a valid KITAS or KITAP for the life of the right and the immigration documents required by [Pasal 69](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-69-who-qualifies). The transaction meets the minimum price, area and parcel-count limits set under [Pasal 72](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-72-the-limits) — those figures live in the Peraturan Menteri and are read at the date of each grant, not fixed here. Where the permit lapses and is not renewed, [Pasal 50](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-50-losing-eligibility) gives the Holder one year to transfer the right to a qualifying party, failing which it lapses by operation of law.

3.3 Term. Hak pakai over State land runs for at most 30 years, extended by at most 20 and renewed by at most 30 — [Pasal 52(1)](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-52-the-term). Renewal is a priority for the former holder on stated conditions, not an entitlement. The Holder is told this in the same words before signing.

3.4 What the Landowner keeps. Nothing in the title: the Plot is gone from the master certificate. Everything else survives by contract — the Design Code under [§7](#7-design-code-annex-c), the service charge and Community Council under [§8](#8-community-council-shared-infrastructure-and-service-charge), the build obligation under [§6](#6-construction-timeline-and-the-build-obligation), and the transfer mechanics of [§2.5](#2-part-a-base-grant-hak-sewa-all-holders) as they apply to an owner rather than a lessee. The Holder accedes to those covenants in the upgrade deed, and they bind his successors by express covenant registered against the new title where BPN permits.

3.5 Trade-offs to be disclosed. Hak pakai is a registered right and stronger on paper, and it is residency-dependent: the resale pool is limited to foreigners who themselves qualify, or requires reconversion to a citizen-held title. It removes the flexibility of [§2.5](#2-part-a-base-grant-hak-sewa-all-holders). Many Holders are better served by the base lease. The upgrade is offered on request, not as the default product.

3.6 Costs. Splitting, release, conversion, [[bphtb|BPHTB]], notarial, [[ppat|PPAT]] and administrative costs are borne by the Holder. Upgrade fee to the Landowner: [amount], settled before the *pelepasan* is signed.

3.7 Order of steps. No release of the Landowner's HGB happens before the Holder's eligibility is confirmed in writing by [[bpn|BPN]] and the upgrade fee is received. The Landowner does not surrender a right over the Plot against a promise.

---

## 4. Part B — Track I: upgrade to title (Indonesian Holders)

4.1 Step 1 — Plot split and sale. On request, the Landowner procures *pemecahan sertifikat* of the Plot and transfers the resulting HGB to the Holder by [[ajb|AJB]] before the PPAT. Purchase price: [amount / formula], credited [in whole / in part] against sums already paid under Part A.

4.2 Step 2 — Holder's own conversion to Hak Milik. ⚠ The Holder may then apply to BPN to upgrade HGB → Hak Milik. This is the Holder's own application; the Landowner facilitates documents but gives no warranty of outcome. Conditions the Holder must satisfy:

- Indonesian citizenship, natural person;
- the Plot is used as *rumah tinggal* — evidenced by PBG or a *keterangan* from the village head. A bare, unbuilt plot does not qualify. Practice varies between land offices; verify with BPN Buleleng before promising this to anyone;
- plots up to 600 m² follow the simplified route; above 600 m² a *constatering* report is required;
- the Holder declares holdings of no more than 5 residential parcels or 5,000 m² in aggregate.

4.2a Married to a foreigner. Where the Holder is an Indonesian citizen married to a foreign national, [[pp 18-2021 hak atas tanah|PP 18/2021]] [Pasal 70](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-70-indonesian-married-to-a-foreigner) allows the same land rights as any other citizen only where the right is not joint marital property, evidenced by a notarial separation-of-assets agreement between the spouses. The agreement is produced before the upgrade is started; without it the application is refused and the Plot sits in limbo between the two regimes.

4.3 Plot sizing. ⚠ Open. The strategy contemplates plots of 5–15 are (500–1,500 m²) and has not settled the [Z1](/cyber-valley/strategy#4-land-use-plan-eight-zones) grain; anything above 600 m² leaves the simplified regime and weakens instrument E. Sizing and the grain decision are taken together, not separately.

4.4 Continuing obligations. Conversion to Hak Milik does not release the Holder from the Design Code, the Community Rules or membership of the Community Council. They survive the title change through a bundle registered against the new title, in this order of strength:

- an easement (*hak servitut* under KUHPerdata Pasal 674 and following) over access, water, power and drainage running with the land, granted by the Landowner and registered at [[bpn|BPN]] against the Plot at the moment of conversion, its terms conditioned on observance of the Design Code and payment of the service charge;
- connection to the estate's roads, water, power and waste is supplied under that easement and is suspended while the Holder is in uncured breach — the easement is the instrument, the connection is the leverage;
- membership of the Community Council as a condition of the easement, binding successors, so that a buyer of the Plot takes the seat and the obligations with it;
- the covenants repeated in the AJB of any onward sale, and the Landowner's right to be notified of that sale.

The easement is drafted and registered as part of the conversion, not afterwards. A conversion completed without it leaves the Plot inside the community by contract only, and that contract does not bind the next buyer.

---

## 5. Building rights and PBG

5.1 Who builds. The Holder builds at its own cost and risk. The Landowner constructs no Improvements.

5.2 Permits. ⚠ PBG is issued to the holder of the land title. For Foreign Holders on Part A, the applicant is therefore the Landowner. Allocation: the Holder prepares and funds the application, the Landowner applies and cooperates; the Holder indemnifies the Landowner for all consequences of the works. SLF to be obtained on completion.

5.3 No works before permit. The Holder shall commence no construction before PBG issuance. Breach is a material default with immediate cessation rights, because enforcement action against unpermitted structures runs against the title holder, not the occupant.

5.4 Ownership of Improvements. Indonesian law recognises horizontal separation — buildings may be owned separately from land. The parties record that Improvements are owned by the Holder for the term. Consequences at termination: [§10](#10-termination-and-end-of-term).

---

## 5A. Construction control, handover and indemnity

The Landowner does not build, yet remains the title holder and the PBG applicant. This section closes that gap: control proportionate to retained liability.

5A.1 Design and contractor approval. No works until the Landowner has approved (a) the design package for Design Code compliance, (b) the identity of the main contractor, (c) the construction programme. Approval is limited to those matters and creates no design or engineering warranty by the Landowner — say so expressly. Approval or refusal is due within 10 working days; failure to act is deemed approval.

5A.2 Contractor qualification. ⚠ Under UU 2/2017 on Construction Services, construction services must be performed by a qualified provider (*penyedia jasa*) holding a valid [[sbu|SBU]] and the corresponding KBLI, and the client (*pengguna jasa*) is obliged to engage such a provider. The Holder shall engage only a contractor meeting this standard and shall furnish copies of SBU, licences and the construction contract before commencement.

5A.3 Supervision. An independent construction supervisor (*pengawas* / MK) is appointed by the Landowner at the Holder's cost. The supervisor is an Indonesian company independent of both parties, holding the qualification the works require; neither the Landowner nor the Holder may appoint an affiliate, with authority to inspect, to require rectification, and to stop works on material non-compliance. Stage inspections at: foundation, structure, roof, MEP, completion.

5A.4 Insurance. For the construction period, procured by the Holder, naming the Landowner as co-insured / loss payee: Contractors' All Risks (CAR/EAR), third-party liability, workers' accident cover (BPJS Ketenagakerjaan for the workforce). Certificates delivered before commencement; lapse is a stop-work event. From SLF onward the Holder maintains property and public liability cover on the Improvements for the term.

5A.5 Security. [Deposit / bank guarantee] of [__] to secure completion, rectification of defects, and reinstatement if works are abandoned. Released in tranches on the handover milestones below, each release due within [15] working days of the milestone, allowing for the maker/authorizer mandate under [[shareholders agreement]] Article 6.

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

5A.8 Holder's indemnity. The Holder indemnifies the Landowner against all claims, penalties, orders and costs arising from the Holder's works and from the Holder's occupation and use, including: unpermitted works, deviation from PBG, breach of zoning or environmental rules, accidents to workers or third parties, and damage to neighbouring land. The indemnity survives termination for [__] years. Its mirror in favour of the Holder is [§9B.5](#9b-title-warranties-negative-pledge-and-indemnity).

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

Binding on all Holders, all tracks, all zones. [[annex c design code|Annex C]] states the zoning code as numbers — footprint and floor multiplier, light balance allocation, species density, and the sound, water, light, air and soil limits with their monitoring and publication duties — rather than by cross-reference. The same rules stand in the graph as [[cyber-valley/policies/zoning system|land usage policy]], with the reasoning behind each number; C0 of the annex maps section to section. The annex is the representation that binds, and it is the version-locked one under 7.4.

⚠ Bali-specific overlays bind regardless of what the Design Code says: provincial building-height limits, architectural requirements, slope and ravine setbacks, water-catchment restrictions. Estate policy stack: [[cyber-valley/policies/zoning system|zoning code]], [[soil policy]], [[water policy]], [[light policy]], [[sound policy]], [[air policy]], [[carbon policy]].

7.1 Scale of measurement. ▲ Footprint and canopy ratios are measured per Plot.

7.2 Density transfer. ▲ Unused footprint entitlement may be transferred to another Plot within the same district through the Register, subject to the Landowner's check that the district balance in Annex C is maintained, against a settlement fee of [__]%. Transfers open from Wave 2. Entitlement not transferred remains with the Plot.

7.3 Amendment and grandfathering. Amendment by the Landowner. Completed Improvements are grandfathered. Any amendment that would worsen the position of already-built Improvements is subject to the veto in [§8.2](#8-community-council-shared-infrastructure-and-service-charge).

7.4 Design Envelope lock. ▲ Grandfathering under 7.3 and the veto under [§8.2](#8-community-council-shared-infrastructure-and-service-charge) protect what is already built. Between signing and SLF the Holder has paid and has nothing on the ground, and is therefore least protected exactly where it is most exposed. This clause closes that window.

7.4.1 Design Envelope of the Plot means (a) the figures in C2 and C3 of Annex C in the version in force at signing, adjusted for any density transferred under C1.2; (b) the Holder's row in the permitted-use matrix, Annex G; (c) so much of the access and connection specification in Annex F as applies to the Plot. The version of Annex C is identified by version number and content hash and initialled by both parties.

7.4.2 Lock. From signing until SLF plus 12 months the Plot is governed by the Design Envelope in the version in force at signing. Later amendments apply to the Plot only with the Holder's written consent.

7.4.3 Duration and transfer. The lock runs for the period in 7.4.2 and no longer than the build obligation in [§6.1](#6-construction-timeline-and-the-build-obligation) plus 12 months. It transfers with the bundle under 2.5.2 and does not restart on assignment. It lapses with the build obligation, so that an unbuilt Plot cannot freeze the code for the term.

7.4.4 Scope of the Landowner's freedom. The lock is per Plot. The Landowner may amend the Design Code at any time for Plots granted after the amendment, and for Holders whose lock has expired, subject to 7.3 and [§8.2](#8-community-council-shared-infrastructure-and-service-charge).

7.4.5 Material change. A change is material where it: reduces permitted footprint or floor area by more than [10]%; removes a use from the Holder's row in Annex G; or increases the cost of compliance for a design already approved under 5A.1 by more than [10]% of the budgeted construction cost. Fact and amount are certified by the independent supervisor under 5A.3 or an independent valuer; disputes follow [§11](#11-dispute-resolution). Materiality is not determined by the Landowner.

7.4.6 Landowner's cure right. Within 30 days of the Holder's notice the Landowner may withdraw the change as to that Plot, grant a variance, or offer an equivalent Plot. Any of these extinguishes the rights in 7.4.7.

7.4.7 Consequences where the change is not cured. Fault and causation are separated: the trigger is the same, the remedy differs by who caused the change.

| cause of the change | remedy |
|---|---|
| the change originates with the Landowner | the Holder may exit with unamortised prepayment under Annex E, plus the documented value of works completed at independent valuation, plus direct loss; or remain and be compensated in the certified amount of the increased cost |
| the change is required by law, regulation or an act of authority, or by *adat*, *subak* or the *awig-awig* of the *desa adat* | no fault; the Holder may exit with unamortised prepayment plus the value of works completed at independent valuation, without damages; payment is secured by the Guarantee Fund under 9B.7 |

⚠ The Holder's exit right exists in both rows. A regime in which a law-driven change leaves the Holder with nothing loads on the Holder a risk it cannot price, and gives the Landowner a reason to prefer changes that arrive through the regulator. Fault governs damages; it does not govern the exit.

7.4.8 Notice window. The Holder invokes 7.4.7 within 90 days of notification of the change. Silence within that period is acceptance of the change.

7.4.9 Continuity. Signing to SLF: this clause. SLF to end of term: grandfathering under 7.3 and the veto under [§8.2](#8-community-council-shared-infrastructure-and-service-charge). There is no interval in which the Plot is unprotected.

*Indonesian sense-text for notary drafting:*

> Sejak tanggal penandatanganan sampai dengan diterbitkannya SLF ditambah 12 (dua belas) bulan, Bidang Tanah tunduk pada Design Envelope sebagaimana berlaku pada tanggal penandatanganan. Perubahan yang terjadi kemudian hanya berlaku bagi Bidang Tanah tersebut dengan persetujuan tertulis Pemegang Hak.

> Apabila perubahan yang bersifat material tidak dipulihkan sesuai Pasal 7.4.6, Pemegang Hak berhak mengakhiri Perjanjian ini. Apabila perubahan berasal dari Pemilik Tanah, Pemegang Hak berhak atas pengembalian bagian pembayaran yang belum teramortisasi, nilai pekerjaan yang telah dilaksanakan menurut penilaian independen, serta kerugian langsung. Apabila perubahan disebabkan oleh peraturan perundang-undangan, keputusan pejabat yang berwenang, atau ketentuan adat, subak dan awig-awig desa adat, Pemegang Hak berhak atas pengembalian dan nilai pekerjaan tanpa ganti rugi.

---

## 8. Community Council, shared infrastructure and service charge

▲ The Articles of Association know three organs — GMS, Board of Directors, Board of Commissioners — and no residents' body; the preamble and Pasal 3(3) record that residents live under terms and values set by the Company. This deed therefore gives Holders enforceable contractual rights rather than a governing organ.

8.1 Community Council. Contractual body; membership compulsory for all Holders, all tracks; survives assignment and title upgrade. Voting weight is fixed on entry and counts both stakes — land and shares, bought separately: base = √(area ÷ district area) + √(shares ÷ issued shares), never reduced, with conduct in each moon cycle adding a bonus, weight = base × (1 + bonus). Normalised across the district, capped at 10% per Holder, renormalised every moon cycle. The factors are stated in [11.1.1](/cyber-valley/cve/legal/hak-sewa/hak-sewa-deed#part-11-community-council) of the deed. A separate legal vehicle (*perkumpulan*) is constituted in Phase 3 to hold shared infrastructure, on the community land trust path in the strategy.

8.2 Veto on deterioration. An amendment to the Design Code or the Community Rules that worsens the position of already-completed Improvements requires the consent of [two thirds] of Holders whose Improvements are affected.

8.3 Right of initiative. A proposal supported by [__] of Holders must be considered by the Board of Directors, with a reasoned written answer published in the Register within 30 days. Silence within that period is deemed acceptance of the proposal.

8.4 Service charge. Basis, cap, escalation, audit rights, and the published annual account.

8.5 Landowner's obligations for access roads, drainage, water and power connection points — defined precisely in Annex F, since a Plot without legal access and connections cannot obtain PBG regardless of the lease. Annex F also states the car-free core: vehicles stop at the perimeter mobility hub, and the Holder's access, parking, construction logistics and waste removal are specified there. ⚠ This is a material restriction on use and is disclosed before signing, not after.

8.6 Long-term. Whether shared infrastructure is retained by the Landowner, transferred to the *perkumpulan*, or handed to the municipality.

---

## 9. Representations

Landowner: valid title, no encumbrances beyond those disclosed, zoning permits the intended use, [[kkpr|KKPR]] status disclosed, licences held and their locational scope. Extended warranties: [§9B](#9b-title-warranties-negative-pledge-and-indemnity).
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
| Landowner cannot process the Holder's PBG application or perform another agreed act | suspension of the corresponding Holder obligation and of construction deadlines under [§6](#6-construction-timeline-and-the-build-obligation); time-based rights extended day for day |
| Holder actually deprived of use or occupation for more than [90] consecutive days | rent abatement pro rata; thereafter termination with return of the unamortised prepaid portion per Annex E, secured by the Guarantee Fund |

9A.5 Landowner's obligations during a Licence Event. Diligent pursuit of cure; [quarterly] progress reporting to the Holder or the Community Council; no new grants over the Estate while the impediment subsists if making them would aggravate the position.

9A.6 Carve-out. ⚠ [§§9A.3–9A.4](#9a-licences-warranty-and-licence-event-regime) do not apply where the Licence Event results from the Landowner's fraud, wilful misconduct, or failure to remedy after repeated written warnings from the authorities. Protection against administrative accidents is legitimate; a shield against neglect is not — and a clause drafted as the latter invites a court to disregard the whole of [§9A](#9a-licences-warranty-and-licence-event-regime).

9A.7 Holder's own licences. Any licence required for the Holder's own activity on the Plot is the Holder's responsibility, subject to the land-time / stay split in [§2.6](#2-part-a-base-grant-hak-sewa-all-holders). The Landowner's licences do not extend to land-time activity.

9A.8 Severability of consequences. A Licence Event affecting one KBLI or one location does not, of itself, affect obligations under this deed that do not depend on that licence.

### 9B. Title warranties, negative pledge and indemnity ▲

9B.1 Warranties of the Landowner, given at signing and repeated on each anniversary and on the date of each assignment in favour of the assignee:

- the Company is duly incorporated and subsisting, its issued capital is fully paid, its NIB is valid;
- the Title is a valid HGB certificate; its number, grant date, expiry date and remaining term are disclosed in Annex A and stated in the recitals as a number;
- a PKKPR covering the intended use subsists for the parcel and is annexed; the Plot does not sit on land recorded as *Pipil*, uncertificated or held on agreement;
- the Plot is free of *hak tanggungan*, attachment (*sita*) and other encumbrances; has not previously been let, promised under a [[ppjb|PPJB]], optioned or otherwise committed; and is not in the physical possession of a third party;
- there are no judicial, administrative or arbitral proceedings, and no asserted adat, subak or desa claims, affecting the Plot;
- zoning and KKPR permit the intended use; the Plot carries no LP2B designation and falls outside *sempadan*;
- [[pbb|PBB]] is paid and no arrears subsist;
- the chain of title documents is disclosed.

9B.2 Due diligence pack and the search at signing. Annex I, delivered before signing: certified copy of the Title certificate, *Surat Ukur*, NIB, PBB receipts, a BPN non-encumbrance search dated no more than 30 days before signing, and the PKKPR document. In addition, and as a condition of execution, the PPAT performs *pengecekan sertifikat* at BPN on the day of signing and the result is recited in the deed. The Landowner warrants that nothing has been created over the Plot between the search and signing.

9B.2a Keeping the Title alive. The Landowner covenants, for the life of this deed, to do everything required to keep the [[hgb|HGB]] over the Plot in force: to satisfy the duties of a holder under [[pp 18-2021 hak atas tanah|PP 18/2021]] [Pasal 42](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-42-the-holder-s-duties), including the duty to build or work the land in line with the grant decision within 2 (two) years of the grant; to apply for extension before the term expires and for renewal within the period allowed by [Pasal 41](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-41-when-to-apply); and to avoid any act or omission that would expose the Plot to being declared Tanah Telantar or otherwise bring the Title to an end under [Pasal 46](/cyber-valley/cve/legal/laws/pp-18-2021-hak-atas-tanah#pasal-46-how-hgb-lapses). Construction carried out by the Holder under this deed counts towards the Landowner's duty under Pasal 42 for the Plot. On written request the Landowner evidences compliance to the Holder, and failure to do so is a Landowner default under [§9B.6](#9b-title-warranties-negative-pledge-and-indemnity).

9B.3 Negative pledge and binding on successors. The Landowner shall not, without the Holder's written consent: encumber the Plot with *hak tanggungan* or other security; grant competing rights over the Plot; or dispose of the Plot otherwise than subject to this deed, the transferee taking bound by it.
[[articles of association]] Article 12(3) independently prohibits the Company from encumbering land and land rights at all, by the nature of its constitution. This clause is the Holder's own contractual right on top of that prohibition, and controls if the Articles are ever amended to permit encumbrance again.

9B.4 Non-disturbance. Where an encumbrance is nevertheless granted, it is permitted only if the secured party confirms in writing that this deed survives enforcement and binds a purchaser at auction. Holders are notified no later than 30 days before the encumbrance is granted, and the Register is updated. For the period an encumbrance subsists, the area revenue charge under [§2.6](#2-part-a-base-grant-hak-sewa-all-holders) is reduced by [__] percentage points.

9B.5 Indemnity in favour of the Holder — the mirror of [§5A.8](#5a-construction-control-handover-and-indemnity). The Landowner indemnifies the Holder against loss, cost, penalty and reasonable legal expense arising from: breach of the warranties in 9B.1; third-party rights subsisting at signing; enforcement of security over the Plot; loss or non-renewal of the master title otherwise than through the Holder's act; and inability to obtain PBG or SLF for reasons attributable to the Landowner's title or licences. Cap: sums paid by the Holder plus the valuation of Improvements under 9B.6. Claims may be brought within [__] years after termination.

9B.6 Remedies for title defect:

| situation | remedy |
|---|---|
| defect curable within 90 days, use unaffected | cure at the Landowner's cost; [§6](#6-construction-timeline-and-the-build-obligation) deadlines suspended and time-based rights extended day for day |
| Holder deprived of use for more than 90 consecutive days | pro-rata abatement for the period |
| deprivation exceeding 180 days, or incurable defect | termination for the Landowner's default, with payment of unamortised prepayment under Annex E, plus the documented value of Improvements at independent valuation, plus direct loss |

9B.7 Guarantee Fund. The Landowner's payment obligations under 6.0.3, 9A.4, 9B.5, 9B.6 and [§10](#10-termination-and-end-of-term) are met from a Guarantee Fund held on a separate Company account, ring-fenced from operating money and used for no other purpose.

9B.7.1 Funding. On each grant, assignment or upgrade of a Plot the Landowner pays 5% (five percent) of the consideration received into the Fund, before any other application of that money and ahead of the operating budget. Contributions continue on every subsequent grant and assignment, whether or not a payment has been made out of the Fund.

9B.7.2 Level. The Fund is whatever has accumulated under 9B.7.1 less payments properly made out of it. There is no separate target and no obligation on the Landowner to top it up from other money: the Fund grows with sales and is replenished by the contributions from subsequent grants and assignments. Its balance at any date is a fact, published under 9B.7.5, and the Holder's expectation is measured by that fact and not by the size of the obligation it answers.

9B.7.3 Denomination. The Fund is denominated in the [[cx|century index]] under [[annex e century index|Annex E]], so that its value tracks the obligations it answers rather than the rupiah.

9B.7.4 Control and payment out. Money leaves the Fund only to pay a Holder a sum due under the clauses named above, on the maker and authorizer mandate in [[shareholders agreement]] Article 6. Payment is made within [30] days of a claim supported by the documents listed in Annex [__], or within [10] days of an arbitral award under [§11](#11-dispute-resolution). No commissioner approval is required to pay a Holder from the Fund; approval is required to take money out of it for anything else, and the only permitted other use is a return of surplus above the 9B.7.2 level.

9B.7.5 Reporting. The Landowner publishes the Fund balance, movements and the exposure calculation in the Register at each anniversary, and on the written request of any Holder within 10 working days. An Estate Certificate issued under 2.5.6 states the Fund balance at its date.

9B.7.6 What this is and is not. ⚠ The Fund is the Company's own asset. It is not insolvency-remote: on the Company's insolvency it ranks with other assets and Holders rank as unsecured creditors. It is disclosed to every Holder in these words, and no marketing material describes it as a bank guarantee, escrow or insurance.

9B.7.7 Shareholder who is also a Holder. Where a Holder is also a shareholder of the Landowner, he takes no part in any decision of the Company concerning his own claim on the Fund, and his claim is paid on the same terms as any other Holder's.

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

Governing law: Indonesian. Escalation: negotiation → mediation → [[bani|BANI]] arbitration in Denpasar, in English and Indonesian, or the District Court of Denpasar (Pengadilan Negeri Denpasar) — the forum chosen throughout the pack, in preference to the District Court of Singaraja that covers the Company's domicile under Articles of Association Pasal 1. Language of proceedings. Interim relief.

## 12. Taxes, currency and costs

Allocate expressly: PPh on lease value; PPN on the lease and on services; BPHTB and PPh on any title transfer; taxes on assignment under [§2.5.10](#2-part-a-base-grant-hak-sewa-all-holders); regional accommodation tax on stay activity under [§2.6](#2-part-a-base-grant-hak-sewa-all-holders); notarial and PPAT fees; splitting and conversion costs; annual PBB; service charge. State whether prices are gross or net of tax, and name the withholding agent consistently with Articles of Association Pasal 12(6).

Currency. Obligations may be denominated in the century index; invoicing and settlement are in IDR at JISDOR on the invoice date ([[uu 7-2011 mata uang|UU 7/2011]]). Any other unit appearing in marketplace or estate systems is a unit of account only.

## 13. General provisions ▲

Notices and their language · personal data, covering publication of monitoring results to the ledger under Annex C and entries in the Register · KYC and source-of-funds procedure supporting the [§9](#9-representations) representation · entire agreement · severability · counterparts and electronic signature · quiet enjoyment as a positive covenant of the Landowner.

---

## Open drafting questions

Moved to [[open questions]] (`legal/notes/open questions.md`) so that they cannot travel into a signable text. Nothing is drafted for execution while an item there is open against the clause being drafted.

## Decision map

▲ clauses implement `holder protocol decisions.md`: D1 → 2.5.1–2.5.5 · D2 → 2.5.6–2.5.8 · D3 → 9B.3–9B.4 · D4 → 9B.7 · D5 → 2.2 · D6 → 2.3 · D7 → 7.1–7.2 · D8 → 6.2 · D9 → 2.4, 10.2, 10.3 · D10 → 2.6 · D11 → 8.1–8.3 · D12 → 9B.5 · D13 → 7.4. Recommended variants are drafted; changing a decision changes only the clauses listed against it.

## Notes for counsel / PPAT

- Not legal advice. English is the working language of this skeleton; the executable instrument is drafted RU-EN-ID in parallel columns, with the Indonesian column written alongside the others rather than translated afterwards, and prevailing under Law 24/2009 unless the parties agree otherwise and accept the risk.
- Arts. 1588–1592 [[kuhperdata|KUHPerdata]] (area shortfall) are treated here as dispositive; confirm numbering and character before use.
- Concrete articles and final wording through the notary — preferably not only the notary proposed by the Landowner alone.
