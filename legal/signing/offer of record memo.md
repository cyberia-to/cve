---
tags: cyber valley, cyberia, legal, signing, memo
alias: offer of record memo, annex d memo
crystal-type: pattern
crystal-domain: socio
icon: "🧾"
---
# Offer of record — memo for the recorder

How to fill [[annex d offer of record|Annex D (Offer of Record)]]. Written as a prompt: a person or an agent follows it step by step.

## Task

Record the version of the product page the Holder saw and the numbers agreed, so that later edits of the page leave the deal unchanged.

## Steps

1. Identify the page the Holder decided on: [[annual leasehold]] for the century index form, [[leasehold upfront]] for full payment.
2. In the `cyber-valley` repository, take the commit of that page as it stood when the Holder saw it:

       git log -1 --format='%H %cs' --before='<date the Holder saw the page>' -- strategy/annual-leasehold.md

   The first field is the commit hash, the second its date. Enter both in D1, row "page version".
3. Open the page at that commit to confirm what the Holder saw:

       git show <hash>:strategy/annual-leasehold.md

4. Take the Plot number and the Plot price from the offer the Holder accepted; enter them in D1.
5. For the century index form, run the calculator at cyberia.my/cx with the agreed Premium; enter the Premium, R₀ and the base rate it shows.
6. Print D1 and D2; both sides initial them at signing.

## Filled example — format only

| field | value |
|---|---|
| product page | [[annual leasehold]] |
| page version | commit 2f4d487cb6fdc9bf4f9a7a8a4bac4b826cd3ce84 of 2026-08-27 |
| Plot and price | sinwood-25, Plot price Rp [___] |
| form | century index |
| Premium | 30% = Rp [___] |
| year-0 rent R₀ | Rp [___] |
| base rate for early redemption | 9% |

## Checks

- the hash opens with `git show` and the page shows the form the Holder chose
- the numbers in D1 match the akta and the recitals of the agreement
