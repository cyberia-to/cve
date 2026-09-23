---
tags: cyber valley, cyberia, legal, draft
alias: annex e, index annex, century index annex, annex-e-century-index
crystal-type: measure
crystal-domain: socio
crystal-size: article
icon: "📈"
---
# Annex E — Index Annex

Annexed to [[hak sewa template]]; reasoning in [[land rights agreement]]. Referred to in the template's 3.1 and 3.2 for the scheduled balance, 3.4 as the unit of account for indexed consideration, 2.4 as the renewal formula, and 3.5 and 11.4 as the denomination of the Guarantee Fund and the service charge cap. On any conflict between this annex and the prose of the deed, this annex prevails.

The unit is the [[cx|century index]] — a fixed basket of eight world assets. What is fixed at signing is the set of quantities; what moves is their price. The machine is the one [[cyberia/protocol/century-index|century index]] protocol states, in full — reset, collar, dual floor, fallbacks, valve — and that page is the source of this annex: where the two differ, the protocol page is corrected first and this annex follows it. Contract theses T1–T8 of the protocol are restated in §7.

## 1. What the Holder owes

At signing (t₀) the year-0 amount R₀ splits by weight into fixed quantities at the reference prices:

    qᵢ = wᵢ · R₀ / Pᵢ(t₀)          I(t) = Σ qᵢ · Pᵢ(t)

I(t) is the basket marked to market in dollars; R(t), the amount owed in year t, is derived from it in §3. The quantities qᵢ stay fixed for the life of this deed and travel with the interest on assignment under [[hak sewa template]] 4.2.

The same machine prices every sum under the deed, each with its own R₀:

| sum | R₀ | how it is paid |
|---|---|---|
| Plot price, scheduled form | the Plot price; 30% settles at signing, the balance is 70% of each qᵢ | within 12 months in one sum, thereafter in 5 equal annual instalments of the same quantities, each valued on its day under §3 |
| annual rent, rent form | the year-0 rent | on each anniversary |
| service charge cap, 11.4 | 1% of the Plot price | per year |
| Guarantee Fund, 3.5 | each contribution at the fix of the day it enters | held, and paid out at value |
| renewal price, 2.4 | L₀, the Plot price | L(T) = L₀ · (T₂ ÷ T₁) · I(T) ÷ I(t₀), floored at L₀ · T₂ ÷ T₁; T₁ and T₂ the first and the renewal Terms in years |

Two forms of purchase exist and no other: upfront, or the scheduled balance held in these quantities. No fee and no interest sit on top of the index.

## 2. Basket and weights

| leg | weight | primary fix | fallback |
|---|---|---|---|
| BTC | 20% | Pyth BTC/USD daily close | CME CF BRR, then median of three named exchanges |
| ETH | 15% | Pyth ETH/USD daily close | CME CF ETH RR, then median of three named exchanges |
| GOLD | 15% | Pyth XAU/USD | LBMA PM fix, then COMEX settle |
| CNY | 15% | Pyth USD/CNH (offshore quote) | WM/Refinitiv, then PBOC parity |
| USD | 15% | 1 (quote currency) | — |
| CU | 10% | LME copper cash settle | COMEX HG settle |
| OIL | 5% | ICE Brent front-month settle | EIA Brent spot |
| UX | 5% | CME UxC U3O8 front-month settle | UxC / TradeTech weekly spot |

Every price enters as a trailing 365-day average of daily fixes. The index publishes every day of the year; a closed market carries its last fix forward. Fixes are USD-quoted by market convention; the ruler of the collar and the floor is bitcoin.

## 3. Machine

    X(t) = BTC/USD 365-day TWAP                       the bitcoin fix
    S(t) = I(t) / X(t)                                basket priced in bitcoin
    R(t) = clamp( S(t), R(t−1) · [0.85, 1.35] )       the sat amount, collared
    R(t) ≥ max( S₀, F / X(t) )                        dual floor
    invoice = R(t) · X(t) · JISDOR(t)                 in rupiah on the invoice date

| parameter | value |
|---|---|
| numéraire | BTC, fixes USD-quoted |
| reset | annual anniversary; the TWAP window ends 30 days before payment, so the Holder knows the invoice a month ahead |
| collar | +35% / −15% per year in sats; undelivered increase does not carry over |
| floor | S₀ sats, and F year-0 dollars; F = R₀ unless the recitals state otherwise |
| R(t−1) | the value of the same quantities at the previous anniversary; before the first anniversary, S₀ |
| settlement | IDR at [[jisdor\|JISDOR]] on the invoice date, as [[uu 7-2011 mata uang\|UU 7/2011]] requires; conversion happens after the collar and is never capped |

The collar meters the move year over year: the amount rises at most 35% and falls at most 15% against the previous anniversary, in sats. The floor has two legs: the sat leg guarantees the Landowner no fewer satoshi than year 0; the fiat leg guarantees the year-0 dollar value. Read as one instrument, the Holder owes the basket, metered by the collar, and owes more than the basket whenever bitcoin outruns it: the Holder signs [[hak sewa template]] 3.4 having read this paragraph. A devaluation of the rupiah flows through in full, which is the point of denominating in the index at all.

The same clamp and floor apply to every sum in §1, each measured against its own quantities: a scheduled balance paid in month eight is clamped against S₀ of its 70% share; each of the five annual instalments against the value of that share at the previous anniversary.

## 4. Quantities — completed at signing

Filled from the 365-day TWAP fixes on the signing date. The figures below are the worked model at R₀ = USD 100,000 on indicative fixes of 31 July 2026, kept here so the arithmetic is visible; the executed annex carries the real numbers.

| leg | t₀ fix | quantity qᵢ |
|---|---|---|
| BTC | $62,626 | 0.31935618 BTC (31,935,618 sats) |
| ETH | $1,857.97 | 8.073327 ETH |
| GOLD | $4,039.38 / oz | 115.501 g |
| CNY | 6.765736 / USD | ¥101,486.04 |
| USD | 1 | $15,000.00 |
| CU | $13,552.04 / t | 737.90 kg |
| OIL | $91.82 / bbl | 54.454 bbl |
| UX | $80.00 / lb U₃O₈ | 62.50 lb |

Derived: X(t₀) = $62,626, S₀ = R₀ / X(t₀) = 1.596781 BTC = 159,678,089 sats. F = USD 100,000.

## 5. Worked invoice

Hypothetical year-1 TWAP fixes: BTC $75,000 · ETH $2,200 · GOLD $4,400 · CU $14,500/t · OIL $85 · U₃O₈ $90/lb · USD/CNY 7.00 · JISDOR 19,000.

1. Mark the quantities to market: I(t₁) = Σ qᵢ · Pᵢ = **$108,503.30**
2. Price in bitcoin: S(t₁) = 108,503.30 / 75,000 = **1.446711 BTC**
3. Collar against R(t₀) = S₀: [1.596781 × 0.85, 1.596781 × 1.35] = [1.357264, 2.155654] → 1.446711 passes unclamped
4. Floor: max(1.446711, S₀ = 1.596781, F / X = 100,000 / 75,000 = 1.333333) = **1.596781 → the sat leg binds**
5. R(t₁) = 1.596781 BTC = 159,678,089 sats
6. Settle: 1.596781 × 75,000 = **$119,758.57**, converted at JISDOR 19,000 = **IDR 2,275,412,830** on the invoice date

Reading of this year: the basket grew 8.5% and bitcoin grew 19.8%, so the sat floor binds and the Holder owes the same sats as year 0, worth more dollars. The worked example is part of the annex, and where a calculation is disputed it is the template the parties follow.

## 6. Review valve

On every fifth anniversary, and only by mutual written consent, the parties may replace at most one leg of at most 10% weight, at the then-current TWAP, value-neutral at the moment of substitution. CNY and USD stay. Silence means no change; neither party may substitute unilaterally.

## 7. Contract theses

| # | thesis |
|---|---|
| T1 | this annex — weights, t₀ prices, quantities, fix sources with fallbacks, collar, floor, one worked invoice — prevails over prose |
| T2 | an asset falling, even to zero, triggers nothing: the sleeve rides down. Only death of a price source triggers replacement, and the replacement prices the same asset |
| T3 | a fix is dead on administrator cessation, 30 days unpublished, or methodology change. Then, in order: the named fallback in §2 → a regulator-designated successor → an equivalent fix set by an independent expert → the last TWAP frozen as a bridge, never as a settlement. If the bitcoin fix dies through the whole waterfall, the ruler reverts to USD |
| T4 | the review valve of §6 |
| T5 | the Holder may recompute any invoice from public sources within 30 days; the recomputation prevails and manifest errors are corrected retroactively. Index disputes are arithmetic |
| T6 | settlement in IDR at JISDOR on the invoice date |
| T7 | the annex survives assignment, sublease, succession and renewal; the same t₀ quantities define the obligation, whoever the parties are |
| T8 | the on-chain fix published by the [[cx]] oracle is evidence and automation; on divergence the computation from the named public fixes prevails |

## 8. Open before signature

| item | to settle |
|---|---|
| R₀ per sum | the Plot price, the year-0 rent where the rent form is elected, and L₀ with T₁ for the renewal formula, from the recitals |
| F | the fiat floor leg, equal to R₀ unless the recitals state otherwise |
| signing fixes | the 365-day TWAP for each leg on the signing date, entered in §4 |
| publication | the Register carries the annual index level, every fix used, the collar and floor test, and the invoice calculation, on the same page as the lease entry |
