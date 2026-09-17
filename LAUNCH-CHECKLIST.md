# Launch checklist — sachinmusale.com

Written 2026-09-17. Everything in the repo is done; this file is the part that needs
a human with account access.

---

## The two reasons Google wasn't showing this site

**1. Every page carried `<meta name="robots" content="noindex,nofollow">`.**
All 67 real pages. The site was left in the staging mode that `set-indexing.py`
sets. Google was explicitly told not to index a single page. *Fixed in the repo.*

**2. This site is not on the domain.** As of today:

| URL | Server | What it serves |
|---|---|---|
| `https://www.sachinmusale.com/` | LiteSpeed | **The old WordPress site** ("Sachin Musale – Artist") |
| `https://manojcpatil.github.io/sachinmusale/` | GitHub.com | This static site |

`www.sachinmusale.com` and `sachinmusale.com` both resolve to `103.250.184.102`,
which is not GitHub Pages (GitHub Pages is `185.199.108–111.153`).

Every canonical tag, `og:url` and sitemap entry in this repo points at
`https://www.sachinmusale.com/...`. Until DNS moves, those URLs are served by a
*different site*. If you publish now without the DNS cutover, Googlebot crawls the
`github.io` copy, reads a canonical pointing at a WordPress page with different
content, and drops the new pages. **Removing the noindex is necessary but not
sufficient — step 2 below is what actually makes the site findable.**

---

## Step 1 — Deploy the repo

```bash
git add -A && git status
```

Review, then commit and push. Nothing here needs a build step.

A `CNAME` file containing `www.sachinmusale.com` has been created (previously only
`CNAME.example` existed). GitHub Pages reads this on push.

> **Note:** `_redirects` is Netlify/Cloudflare Pages syntax and does **nothing** on
> GitHub Pages. It is harmless to keep as documentation. The old-URL redirects are
> actually handled by the 61 stub HTML pages (`about-us/index.html`, `portfolio/*`,
> `shortcodes/*`, …), each of which is `noindex,follow` with a canonical plus a
> meta-refresh to its replacement. That is the correct approach on GitHub Pages and
> it already works.

## Step 2 — Point the domain at GitHub Pages

This is the step that makes the difference. At the DNS host for `sachinmusale.com`:

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `manojcpatil.github.io.` |

Then in the repo: **Settings → Pages → Custom domain** → `www.sachinmusale.com` →
Save → wait for the certificate → tick **Enforce HTTPS**.

Verify before moving on:

```bash
curl -sI https://www.sachinmusale.com/ | head -3
```

You want `server: GitHub.com`, not `server: LiteSpeed`.

> **Decide what happens to the WordPress site first.** Once DNS moves, it is gone
> from this domain. Take a backup. If any old WordPress URL is not covered by an
> existing stub page, add a stub for it before cutting over, or that URL 404s.

## Step 3 — Google Search Console

I cannot do this part; it needs the Google account that owns the property.

1. <https://search.google.com/search-console> → **Add property**.
2. Choose **Domain** (`sachinmusale.com`) if you can add a DNS TXT record — it
   covers `http`, `https`, apex and `www` in one property. Otherwise choose
   **URL prefix** and use `https://www.sachinmusale.com/`.
3. Verification:
   - *Domain property:* add the TXT record Google gives you at the DNS host.
   - *URL prefix:* the **HTML file** method is easiest here — download
     `google<hash>.html`, drop it in the repo root, push. Do **not** use the
     "HTML tag" method: the `<head>` of all 67 pages is managed by scripts and a
     hand-added tag will be lost on the next regeneration.
4. **Sitemaps** → submit `sitemap.xml`.
5. **URL Inspection** on `https://www.sachinmusale.com/` → **Request indexing**.
   Do the same for `/portfolio.html` and `/commission.html`. Don't bother
   requesting all 67; the sitemap handles the rest.
6. Add the property to **Bing Webmaster Tools** too — it can import directly from
   Search Console, and it feeds ChatGPT search results.

Expect **2–6 weeks** before the artwork pages appear for anything but brand-name
searches. A brand-new URL set on a domain that just changed hosts takes time.

## Step 4 — Google Business Profile

Highest-value item for a local artist and it is not a website change.
<https://business.google.com> → "Sachin Musale Art Studio", Jalgaon. Category
*Art studio* / *Art school*. Same address, phone and hours as
`contact.html`, letter for letter — Google cross-checks this against the
`LocalBusiness` schema already on that page. Add photos of the studio and the
work.

---

## Left for a human — content, not markup

These were staging placeholders. I commented them out rather than inventing
copy; search for `STAGING NOTE` to find each one.

| Where | What |
|---|---|
| every page, footer | Newsletter signup is not wired to anything and its **Join** button does nothing. Hidden. Connect Mailchimp, then uncomment. |
| `classes.html` | "this page is deliberately kept out of the main menu…" — internal note. Hidden. |
| `classes.html` | "To confirm before launch: batch timings, current fees, age groups…" Hidden. **The real timings and fees still need writing.** |
| `exhibitions.html` | "To confirm before launch: the record title, the date, the venue…" for the Guinness World Records entry. Hidden. **This is worth writing properly — see the backlink strategy.** |
| `1000-faces.html` | The counter still reads **0** faces complete. Left alone — that may be accurate, but a `0` is poor copy on a live page. |

## Deliberately not changed

- **URL slugs.** They are already clean, lowercase, hyphenated and descriptive
  (`/artworks/sachin-musale-watercolour-portrait-sardarji-01.html`). The `.html`
  extension is not an SEO problem. Renaming them now would throw away the only
  thing that makes the first crawl cheap.
- **Image compression.** Already done properly: every asset is WebP, `srcset` at
  480/751/1000w, largest file 276 KB, 13 MB for the whole library. There was
  nothing to win here. The only non-WebP file is the OG image, which must be JPEG.
