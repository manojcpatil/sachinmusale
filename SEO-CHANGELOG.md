# SEO work — 2026-09-17

67 indexable pages, 61 redirect stubs, 128 HTML files total.
Every claim below was verified by a script over the built files; results at the bottom.

---

## Indexability

| | Before | After |
|---|---|---|
| Real pages | 67 × `noindex,nofollow` | 67 × `index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1` |
| Redirect stubs + 404 | 61 × `noindex,follow` | unchanged — correct as-is |

`max-image-preview:large` matters for an artist: it is what lets Google show a
full-size thumbnail instead of a postage stamp.

`set-indexing.py` was updated to match the new directive string, so
`python set-indexing.py status` still reports correctly. It now says **LIVE**.

## robots.txt / sitemap.xml

- `robots.txt` — rewritten. Disallows nothing, points at the sitemap, and documents
  *why* the old-theme stub paths are deliberately crawlable (they are `noindex,follow`
  redirect stubs, so link equity from old inbound links still passes through).
- `sitemap.xml` — rebuilt. 67 URLs, exactly matching the 67 indexable pages, no more
  and no less. Added the `image:` namespace with **166 `<image:image>` entries** so
  Google Images can associate each painting with its page. Well-formed XML; every
  image URL resolves to a real file. Also fixed malformed priorities (`.9` → `0.9`).

## Canonicals

All 67 already had one. Verified every canonical is absolute, HTTPS, unique, and
points at *its own* URL — no page canonicalising to another.

> The canonicals point at `https://www.sachinmusale.com/`, which is currently
> served by the old WordPress site. See `LAUNCH-CHECKLIST.md` step 2 — this is the
> second root cause and it is not fixable from the repo.

## Titles and meta descriptions

All 67 pages already had both, but 22 titles ran past Google's ~60-character
display limit (longest 79) and 62 descriptions past ~158 (longest 265) — so the
tails were being cut off in results.

Rewrote titles for 8 key pages by hand and regenerated all 55 artwork pages from
`data/artworks.json`.

- Titles: now **37–60 chars**, all 67 unique.
- Descriptions: now **117–158 chars**, all 67 unique.

Artwork descriptions are built from progressively shorter *complete* variants
rather than being truncated. An early truncating version produced
"a basket of pink water" from "a basket of pink water lilies" — a snippet that
would have been factually wrong. No description ends mid-phrase.

## Headings

Before: **66 of 67 pages** had a broken outline. Two systemic causes —
footer column headings were `<h4>` directly after an `<h2>`, and collection/artwork
pages jumped `h1 → h3`.

- Footer headings `<h4>` → `<h2>`, with the `footer.site h4` CSS selector moved to
  match. Verified in the browser: computed font-size, family, transform, letter-spacing
  and colour are byte-identical to before — no visual change.
- Collection pages got a real section `<h2>` above the grid (visually hidden, keyword
  accurate: *"Watercolour portrait paintings by Sachin Musale — 14 works"*).
- `commission.html` got an `<h2>` above the three-step block.
- 55 artwork pages + `contact.html`: the enquiry-form `<h3>` promoted to `<h2>`, with
  a `.enq h2` rule added so it keeps its 1.2rem size.

After: **0 of 67** pages have a problem. Exactly one `<h1>` each, no skipped levels.

## Images

Already in good shape, and the audit confirms it: **983 `<img>` tags, every one** has
`alt`, `width` and `height`, and every `src` resolves. The 5 empty `alt=""` are the
decorative hero slideshow inside `aria-hidden="true"` — correct as-is.

Changed: the first row of each gallery grid (4 images) no longer has
`loading="lazy"`. Lazy-loading the LCP element delays it — that was costing
Largest Contentful Paint on every collection page.

## Structured data

**135 JSON-LD blocks, all valid JSON.** Added:

- `BreadcrumbList` on all 66 non-homepage pages (Home → Portfolio → Collection → Work).
- `CollectionPage` + `ItemList` on the 7 pages that had no schema at all
  (portfolio, portraits, sketches, landscapes, conceptual, exhibitions, classes).
- `Course` × 6 + `EducationalOrganization` on `classes.html`.
- `WebSite` on the homepage.

Corrected on all 55 artwork pages: `artworkSurface` was set to the *genre*
("Portraits") when the property means the physical surface. Now `Paper`/`Canvas`,
with `artMedium` (Watercolour, Charcoal, Graphite, Oil paint, Mixed media),
`artform` (Painting/Drawing), pixel dimensions, `thumbnailUrl`, `copyrightHolder`
and a linked `isPartOf` collection.

Corrected on `contact.html`: the `LocalBusiness` had an `openingHoursSpecification`
with no `opens`/`closes`, which Google ignores and which misrepresents an
appointment-only studio. Replaced with an accurate `description`, plus `founder`
and `sameAs`.

## Social cards

The 55 artwork pages used **WebP** as `og:image`. LinkedIn and X render WebP
unreliably, so those shares were showing no image at all.

Generated **55 JPEG OG cards** at 1200×630 (`assets/img/og/`, 2.9 MB total) — each
painting centred on the site's paper background with a thin mount rule. Added
`og:image:secure_url`, `:type`, `:width`, `:height`, `:alt`, `og:locale`, and the
full Twitter set (`twitter:title`, `:description`, `:image`, `:image:alt`) — only
`twitter:card` existed before.

## Core Web Vitals

The site was already well built for this: no external scripts, no web fonts, all CSS
inline, every image dimensioned. What was left:

- `<link rel="preload" as="image">` for the LCP image on **63 pages**, carrying
  `imagesrcset`/`imagesizes` so the preload matches what the `<img>` actually fetches.
  (The other 4 are text-led pages with no hero image.)
- Removed a duplicate `fetchpriority="high"` on a below-the-fold thumbnail on the
  homepage, which was competing with the hero for priority.
- Eager-loaded the first grid row, as above.

## Mobile

Tested every page at **320 / 360 / 390 / 768 px** — 44 page-width combinations,
**zero horizontal overflow**, before and after the CSS change.

Found and fixed a genuine defect: footer navigation links had a **20px** tap
target, well under the 24px WCAG 2.5.8 minimum and the 44px comfortable size.
Breadcrumbs were 17px; the burger button 35px. Added a `max-width:900px` block
sizing footer links, filter chips, buttons, breadcrumbs, contact-list links and
prev/next links to 44px.

After: no tap target under 24px anywhere except two inline links inside sentences,
which WCAG 2.5.8 explicitly exempts.

## Removed from the indexable site

Build notes that were harmless while the site was `noindex` but would have gone
straight into Google's snippets. Commented out, not deleted — search `STAGING NOTE`.

- "Newsletter — wire to Mailchimp free tier (500 contacts) before launch" — footer,
  **all 68 pages**, next to a **Join** button that does nothing.
- "this page is deliberately kept out of the main menu…" — `classes.html`.
- "To confirm before launch: batch timings, current fees…" — `classes.html`.
- "To confirm before launch: the record title, the date, the venue…" — `exhibitions.html`.

## Already correct — checked, not changed

- **Broken links:** none. All internal `href`s across 67 pages resolve.
- **HTTPS:** no insecure `http://` resource anywhere.
- **Image compression:** all WebP, responsive `srcset`, largest file 276 KB.
- **URL slugs:** already clean and descriptive.
- **`_redirects`:** does nothing on GitHub Pages, but the 61 stub pages handle the
  old WordPress URLs correctly. See the launch checklist.

---

## Verification

`ALL CHECKS PASSED` — 30 assertions over the built files:

```
indexability   67 indexable · 0 noindex left · 61 stubs still noindex,follow
head tags      67 unique titles (max 60) · 67 unique descriptions (max 158)
               67 unique canonicals, each pointing at its own URL
headings       one H1 + no skipped levels on every page
images         983 imgs: all have alt, all have width+height, all srcs resolve
links          no broken internal links · no insecure http:// resources
sitemap        67 urls == 67 indexable pages · 166 image URLs all resolve · valid XML
schema         135 JSON-LD blocks, all valid · BreadcrumbList on all 66 non-home pages
build notes    no internal to-do copy left visible
deploy         CNAME set · robots.txt disallows nothing · 404.html · 55 OG cards
```

Plus, in a real browser: 0 console errors, 0 horizontal overflow at four widths,
and the footer heading change confirmed pixel-identical.
