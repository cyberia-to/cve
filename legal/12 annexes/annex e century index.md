---
tags: cyber valley, cyberia, legal
alias: annex e, index annex, century index annex, annex-e-century-index
crystal-type: measure
crystal-domain: socio
crystal-size: article
icon: "📈"
---
# Annex E — Century Index

Annexed to [[hak sewa template]]. It sets the rent of the century index form (3.1–3.4), the renewal price (2.4), the Guarantee Fund unit (3.5) and the service charge cap (11.4). The rules follow the [[cyberia/protocol/century-index|century index]] protocol. The daily level, its history, the calculator and worked examples are published at [cyberia.my/cx](https://cyberia.my/cx).

## E1. Terms

| term | meaning |
|---|---|
| Century Index | a fixed basket of eight world assets used as the unit of account |
| leg | one asset of the basket |
| weight | the share of a leg in the basket at signing |
| quantity | the amount of a leg the obligation holds: satoshi, grams of gold, barrels of oil; fixed at signing for the Term |
| fix | the published price of a leg in dollars for one day |
| TWAP | the average of a leg's daily fixes over the trailing 365 days |
| bitcoin fix | the TWAP of BTC/USD, used as the ruler of the collar and the floor |
| satoshi | one hundred-millionth of a bitcoin |
| collar | the band within which the rent may change from one lease year to the next |
| floor | the lowest rent: the year-0 rent in bitcoin and in dollars |
| JISDOR | Bank Indonesia's daily USD/IDR reference rate |
| anniversary | the same calendar day as signing, in each later year of the Term |

## E2. Basket

| leg | weight | primary fix | fallback |
|---|---|---|---|
| BTC | 20% | Pyth BTC/USD daily close | CME CF BRR, then the median of three named exchanges |
| ETH | 15% | Pyth ETH/USD daily close | CME CF ETH RR, then the median of three named exchanges |
| GOLD | 15% | Pyth XAU/USD | LBMA PM fix, then COMEX settle |
| CNY | 15% | Pyth USD/CNH | WM/Refinitiv, then PBOC parity |
| USD | 15% | 1 | — |
| CU | 10% | LME copper cash settle | COMEX HG settle |
| OIL | 5% | ICE Brent front-month settle | EIA Brent spot |
| UX | 5% | CME UxC U3O8 front-month settle | UxC or TradeTech weekly spot |

## E3. Formulas

Quantities, fixed at signing:

    qᵢ = wᵢ · R₀ ÷ Pᵢ(t₀)

| symbol | meaning |
|---|---|
| qᵢ | the quantity of leg i |
| wᵢ | the weight of leg i |
| R₀ | the year-0 rent, in dollars |
| Pᵢ(t₀) | the TWAP of leg i on the signing date |

Value of the basket on day t:

    I(t) = Σ qᵢ · Pᵢ(t)

| symbol | meaning |
|---|---|
| I(t) | the value of the basket, in dollars |
| Σ | the sum over the eight legs |
| qᵢ | the quantity of leg i |
| Pᵢ(t) | the TWAP of leg i on day t |

The basket in bitcoin:

    S(t) = I(t) ÷ X(t)

| symbol | meaning |
|---|---|
| S(t) | the value of the basket, in bitcoin |
| I(t) | the value of the basket, in dollars |
| X(t) | the bitcoin fix on day t |

Rent of a lease year, in bitcoin:

    R(t) = clamp( S(t), 0.85 · R(t−1), 1.35 · R(t−1) ),   at least max( S₀, F ÷ X(t) )

| symbol | meaning |
|---|---|
| R(t) | the rent of the lease year starting at anniversary t, in bitcoin |
| clamp | S(t), held between the lower and the upper bound that follow |
| S(t) | the value of the basket in bitcoin at anniversary t |
| R(t−1) | the rent of the previous lease year, in bitcoin; for the first year, S₀ |
| S₀ | the year-0 rent in bitcoin: R₀ ÷ X(t₀) |
| F | the year-0 rent in dollars: R₀ |
| X(t) | the bitcoin fix at anniversary t |

Monthly instalment, in rupiah:

    M = R(t) · X(t) · J ÷ 12

| symbol | meaning |
|---|---|
| M | the instalment of the month |
| R(t) | the rent of the lease year, in bitcoin |
| X(t) | the bitcoin fix at anniversary t |
| J | JISDOR on the invoice date of the month |

## E4. Rules

| rule | text |
|---|---|
| T1 Annex first | this annex governs over the prose of the deed |
| Quantities | the quantities are fixed at signing for the Term; they pass with the lease on assignment, succession and renewal |
| Yearly amount | at each anniversary the rent of the coming lease year is computed from the fixed quantities at the TWAP prices, with the window closing 30 days before the first payment of that year; the Holder knows the year's rent a month ahead |
| Collar | the rent of a lease year moves at most +35% or −15% in bitcoin from the year before; an increase beyond the band lapses |
| Floor | the rent stays at or above its year-0 value in bitcoin and in dollars |
| T6 Settlement | invoices settle in rupiah at JISDOR on the invoice date, under UU 7/2011; conversion follows the collar and carries the full rupiah rate |
| T2 Asset falls | a leg that falls in price, even to zero, stays in the basket |
| T3 Price source ends | a source is ended by cessation, 30 days without publication or a change of method; the price then comes from the named fallback, then a successor named by the regulator, then an equivalent fix set by an independent expert, with the last TWAP as a bridge. Where every bitcoin source ends, the ruler becomes the dollar |
| T5 Recomputation | the Holder may recompute any invoice from public sources within 30 days; the recomputation prevails and manifest errors are corrected back to their date |
| T7 Continuity | the same quantities define the obligation whoever the parties are |
| T8 On-chain fix | the fix published by the [[cx]] oracle serves as evidence; the computation from the named public sources prevails |
| Publication | the register publishes each year's computation with every fix used; [cyberia.my/cx](https://cyberia.my/cx) publishes the daily level |

## E5. Form at signing

| field | value |
|---|---|
| signing date t₀ | [___] |
| R₀, year-0 rent | USD [___] |
| F, dollar floor | USD [___] |
| X(t₀), bitcoin fix | USD [___] |
| S₀, year-0 rent in bitcoin | [___] BTC |

| leg | weight | TWAP at signing, Pᵢ(t₀) | quantity qᵢ |
|---|---|---|---|
| BTC | 20% | [___] | [___] BTC |
| ETH | 15% | [___] | [___] ETH |
| GOLD | 15% | [___] | [___] g |
| CNY | 15% | [___] | ¥ [___] |
| USD | 15% | 1 | $ [___] |
| CU | 10% | [___] | [___] kg |
| OIL | 5% | [___] | [___] bbl |
| UX | 5% | [___] | [___] lb U₃O₈ |
