# sachinmusale.com

The website for **Sachin Musale** — artist, Jalgaon, Maharashtra.
Original watercolour portraits, graphite and charcoal drawings, landscapes and canvas work,
plus **The 1,000 Faces Project**.

- 67 pages, 55 original artworks in four collections
- Every artwork page has a working enquiry route (opens WhatsApp, pre-filled)
- No framework, no build step, no database, no plugins to break
- Median load: **0.3s** on a throttled mobile connection

---

## Publishing this on GitHub Pages — 5 steps

1. **Create a repository** on GitHub. Public, and any name (e.g. `website`).
2. **Upload everything in this folder** to the repository — keep the structure exactly as it
   is. If you prefer the command line:

   ```bash
   cd sachinmusale-website
   git init
   git add .
   git commit -m "Website"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
   git push -u origin main
   ```

3. In the repository go to **Settings → Pages**.
4. Under **Build and deployment → Source**, choose **Deploy from a branch**.
   Set **Branch** to `main` and the folder to **`/ (root)`**. Press **Save**.
5. Wait about a minute. The site is live at:

   ```
   https://YOUR-USERNAME.github.io/YOUR-REPO/
   ```

### Then connect sachinmusale.com

1. In **Settings → Pages → Custom domain**, type `www.sachinmusale.com` and save.
2. In this folder, rename **`CNAME.example`** to **`CNAME`** and commit it.
   *(Do this only after the domain is set up — a `CNAME` file without correct DNS will stop
   the site loading.)*
3. At your domain registrar, add these DNS records:

   | Type | Name | Value |
   |---|---|---|
   | CNAME | `www` | `YOUR-USERNAME.github.io` |
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |

   The four `A` records point the bare `sachinmusale.com` at GitHub; the `CNAME` handles
   `www`. Delete any conflicting `A` or `CNAME` records from your old host first.
4. Back in **Settings → Pages**, tick **Enforce HTTPS** once it becomes available.

> **Important — the site is currently hidden from Google.** Every page ships
> `noindex,nofollow` so nothing gets indexed before it is signed off. When you are ready to
> go live in search:
>
> ```bash
> python3 set-indexing.py index      # allow Google to index every page
> python3 set-indexing.py status     # check the current state
> python3 set-indexing.py noindex    # hide it again if needed
> ```
>
> Then add the site to **Google Search Console** and submit `sitemap.xml`.

---

## What's in here

| Path | What it is |
|---|---|
| `index.html` | Home |
| `1000-faces.html` | The 1,000 Faces Project — the flagship campaign page |
| `portfolio.html` | All 55 works, filterable by collection |
| `portraits.html` `sketches.html` `landscapes.html` `conceptual.html` | The four collections |
| `artworks/…` | 55 individual artwork pages (title, medium, size, enquiry form) |
| `commission.html` | Commission a Portrait — process, price guide, FAQ, form |
| `exhibitions.html` | Exhibition record, Guinness certificate, video list |
| `about.html` · `classes.html` · `contact.html` | Studio pages |
| `assets/img/` | All images, pre-optimised as WebP at three sizes each |
| `data/artworks.json` | The whole catalogue as data |
| `sitemap.xml` · `robots.txt` | Ready for Search Console |
| **`404.html`** | Shown for any unknown URL (GitHub Pages uses this automatically) |
| **`.nojekyll`** | Tells GitHub Pages to serve the files as-is. **Do not delete.** |
| `shortcodes/…` `portfolio/…` and 10 more folders | Redirect pages so the old WordPress URLs still land somewhere real |
| `set-indexing.py` | Switch between staging (hidden) and live (indexable) |

### How the enquiry forms work

There is no form plugin and no server to go wrong. On submit, the form builds the visitor's
message and opens **WhatsApp pre-filled**, so they can see exactly what is sent. A second
button sends the same text by email. Nothing is stored on the website.

This is deliberately replacing the old site's form — which is currently broken and displays
`[contact-form-7 404 "Not Found"]` on the contact page, meaning the live site cannot receive
a single enquiry today.

---

## Editing the site

Everything is plain HTML. Titles, mediums, sizes and alt text all come from
`data/artworks.json` and the pages are generated from it.

**To update the 1,000 Faces counter** after finishing a portrait, the two numbers live in the
build script (`build/generate_pages.py`, the `FACES` dictionary). Whoever maintains the site
has the full source in a separate repository — see `sachinmusale-source-kit.zip`.

Small, safe edits you can make directly in GitHub's web editor:

- **Phone / email** — search for `9890043290` or `sachinmusale81@gmail.com` and replace.
- **A price or note** — edit `data/artworks.json`.
- **Text on a page** — open the `.html` file, find the paragraph, edit it.

After any edit, commit — GitHub Pages republishes automatically in about a minute.

---

## Known follow-ups

Three content items are deliberately left incomplete rather than filled with guesses.
They are documented in the handover notes:

1. The **Guinness World Records** story — a certificate photograph exists, with no explanation
   of what the record was. There is a designed slot for it on `exhibitions.html`.
2. **Titles for the five videos** on `exhibitions.html`.
3. **Class fees and batch timings** on `classes.html` — the old site's page said only
   "Coming Soon!".

Also still to confirm with the artist: the medium of 54 of the 55 works, and the year of each.

---

*Artwork © Sachin Musale. Images may not be reproduced without permission.*
