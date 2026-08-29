# cve — house rule: personal data never enters the graph

`~/cyber/cve` is public (`cyberia-to/cve`) and every push publishes to
`cyber.page`. This repo carries real legal instruments for real people —
the boundary below is not optional.

## The rule

Personal data of a natural person never appears in a committed `.md`
file in this repo, in any language, in any edition (working, bilingual,
draft, translation). This includes:

- passport / KITAS / national ID numbers
- home addresses of individuals
- personal phone numbers, personal email addresses
- personal bank account numbers
- signatures, thumbprints, photographs

**Company-level** identifiers are not personal data and may stay in the
graph: NPWP, NIB, company registered address, company bank account,
certificate numbers (HGB/SHM), deed numbers, share counts, prices.
The line is the natural person, not "sensitive-sounding."

## What goes in the source instead

Where a clause needs to identify a person by document number, write a
placeholder that keeps the sentence legally readable without the digits:

> holder of a Russian passport [number on file with the Company]

Bahasa Indonesia: `[nomor tersimpan pada Perseroan]`.

## Where the real data lives

Only in the generated PDF used for actual signing — never in a file
this repo's `.md` sources, never in a commit, never in anything `git
push` touches. If a document needs real personal data to be signable:

1. Keep the real values in a working file outside this repo (e.g.
   `/tmp` or `/private/tmp`, never `~/cyber/cve`).
2. Substitute the real values into the markdown only in memory, at the
   moment of generating the PDF via `tools/md2pdf.py` — write the
   real-data version to a temp copy, render it, discard the temp copy.
   The file that gets `git add`ed keeps the placeholder.

## Before every commit touching `legal/`

Grep the diff for digit runs that look like a passport number, phone
number, or ID before staging:

    git diff --cached -- legal/ | grep -E '[0-9]{6,}'

Every hit must be a company/certificate/deed/NIB/NPWP number, a price,
or a date — never a person's own document number.

## If it already leaked

If a personal number is found in a past commit that was already pushed
to `origin/main`, treat it as already public — GitHub history and
`cyber.page`'s prior builds may have cached it. Redact going forward
immediately, then flag to the user whether the exposure window needs
separate remediation (rotating the document, notifying the person)
beyond the code fix.
