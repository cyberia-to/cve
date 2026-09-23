---
tags: cyber valley, cyberia, legal, draft
alias: annex e, index annex, century index annex, annex-e-century-index
crystal-type: measure
crystal-domain: socio
crystal-size: article
icon: "📈"
---
# Annex E — Index Annex

Annexed to [[hak sewa template]]; reasoning in [[land rights agreement]]. Referred to in the template's 3.4 as the unit of account for indexed consideration, in 2.4 as the renewal formula, and in 3.5 and 11.4 as the denomination of the Guarantee Fund and the service charge cap. On any conflict between this annex and the prose of the deed, this annex prevails.

The unit is the [[cx|century index]] — a fixed basket of eight world assets. What is fixed at signing is the set of quantities; what moves is their price. General protocol and basket rationale: [[cyberia/protocol/century-index|century index]] — that page still documents the collar as the general design; this annex is the CVE-specific implementation and the collar does not apply here (§3). Where the two disagree on the machine itself, this annex governs for any deed under [[land rights agreement]].

## 1. What the Holder owes

At signing (t₀) the year-0 amount R₀ splits by weight into fixed quantities at the reference prices:

    qᵢ = wᵢ · R₀ / Pᵢ(t₀)          I(t) = Σ qᵢ · Pᵢ(t)

I(t) is the basket marked to market in dollars; R(t), the amount owed in year t, is derived from it in §3. The quantities qᵢ stay fixed for the life of this deed and travel with the interest on assignment under [[hak sewa template]] 4.2.

The same machine prices three things, each with its own R₀: the annual rent of the rent form; the service charge cap of 11.4; and the renewal price of 2.4, where R₀ = L₀, the Plot price, and L(T) = L₀ · (T₂ ÷ T₁) · I(T) ÷ I(t₀), floored at L₀ · T₂ ÷ T₁, T₁ and T₂ being the first and the renewal Terms in years. The Guarantee Fund of 3.5 is carried in quantities qᵢ computed from each contribution at the fix on the day it enters.

**Deferred balances stay outside the index.** The scheduled forms of [[hak sewa template]] 3.1 carry a fixed fee and no index on the balance. The one instrument that revalues a late balance through this annex is [[hak sewa simple]] clause 5, and only there.

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

Every price enters as a trailing 365-day average of daily fixes. The index publishes every day of the year; a closed market carries its last fix forward.

## 3. Machine

    S(t) = I(t) / X(t)                              basket priced in bitcoin
    R(t) = max( S(t), S₀, F / X(t) )                 dual floor, no cap; R(t) in bitcoin
    invoice = R(t) · X(t) · JISDOR(t)                 in rupiah on the invoice date

| parameter | value |
|---|---|
| numéraire | BTC, fixes USD-quoted |
| reset | annual anniversary; the TWAP window ends 30 days before payment |
| settlement | IDR at [[jisdor\|JISDOR]] on the invoice date, as [[uu 7-2011 mata uang\|UU 7/2011]] requires |

R(t) tracks the basket uncapped. Conversion into the settlement currency is never capped either: a devaluation of the rupiah flows through in full, which is the point of denominating in the index at all.

The floor has two legs. The sat leg guarantees the Landowner no fewer satoshi than year 0. The fiat leg guarantees the year-0 dollar value. The Holder pays the higher of S(t) and the floor. Read as one instrument, the Holder owes the basket, and owes more than the basket whenever bitcoin outruns it: the Holder signs [[hak sewa template]] 3.4 having read this sentence.

## 4. Quantities — completed at signing

Filled from the 365-day TWAP fixes on the signing date. The figures below are the worked model at R₀ = USD 100,000 per year on indicative fixes of 31 July 2026, kept here so the arithmetic is visible; the executed annex carries the real numbers.

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
3. Apply the floor: max(S(t₁) = 1.446711, S₀ = 1.596781, F / X = 100,000 / 75,000 = 1.333333) = **1.596781 → the sat leg of the floor binds**
4. R(t₁) = 1.596781 BTC = 159,678,089 sats
5. Settle: 1.596781 × 75,000 = **$119,758.57**, converted at JISDOR 19,000 = **IDR 2,275,412,830** on the invoice date

The worked example is part of the annex, not an illustration. Where a calculation is disputed, it is the template the parties follow.

## 6. Review valve

On every fifth anniversary, and only by mutual written consent, the parties may replace at most one leg of at most 10% weight, at the then-current TWAP, value-neutral at the moment of substitution. Silence means no change. Neither party may substitute unilaterally.

## 7. Open before signature

| item | to settle |
|---|---|
| R₀ | the year-0 rent per Plot, from which every quantity is derived |
| F | the fiat floor leg — normally equal to R₀ |
| signing fixes | the 365-day TWAP for each leg on the signing date, entered in §4 |
| publication | the Register carries the annual index level, every fix used and the invoice calculation, on the same page as the lease entry |
| L₀, T₁ | for the renewal formula: the Plot price and the first Term in years, from the recitals |
