#!/usr/bin/env python3
"""
Switch the site between STAGING and LIVE indexing.

  python3 set-indexing.py status    -> show current state
  python3 set-indexing.py index     -> allow Google to index every page (GO LIVE)
  python3 set-indexing.py noindex   -> hide from Google (staging / preview)

Only the real pages are touched. The old-URL redirect pages and 404.html stay
'noindex,follow' on purpose, in both modes.
"""
import os, re, sys

# Always operate on the folder this script lives in, wherever it is run from.
ROOT = os.path.dirname(os.path.abspath(__file__))

NOINDEX = '<meta name="robots" content="noindex,nofollow">'
INDEX   = '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">'
SKIP_DIRS = {'shortcodes', 'portfolio'}

def pages():
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in ('.git',)]
        for f in files:
            if f.endswith('.html'):
                yield os.path.join(root, f)

def find():
    live = hidden = 0
    for p in pages():
        h = open(p, encoding='utf-8').read()
        if INDEX in h: live += 1
        elif NOINDEX in h: hidden += 1
    return live, hidden

def switch(to):
    changed = 0
    for p in pages():
        h = open(p, encoding='utf-8').read()
        if INDEX in h or NOINDEX in h:
            new = h.replace(INDEX, NOINDEX) if to == 'noindex' else h.replace(NOINDEX, INDEX)
            if new != h:
                open(p, 'w', encoding='utf-8').write(new)
                changed += 1
    live, hidden = find()
    print(f"{changed} page(s) updated.")
    print(f"Now: {live} indexable, {hidden} hidden, rest left untouched (redirect pages / 404).")

if __name__ == '__main__':
    mode = (sys.argv[1] if len(sys.argv) > 1 else 'status').lower()
    live, hidden = find()
    if mode == 'status':
        print(f"indexable pages : {live}")
        print(f"hidden pages    : {hidden}")
        print()
        print("This site is " + ("LIVE (Google may index it)." if live and not hidden
              else "in STAGING mode (hidden from Google)."))
        print("Run:  python3 set-indexing.py index      to go live")
        print("      python3 set-indexing.py noindex    to hide it again")
    elif mode == 'index':
        switch('index')
        print("\nThe site is now indexable. Next:")
        print("  - Google Search Console -> add the property -> submit sitemap.xml")
        print("  - Google Business Profile -> 'Sachin Musale Art Studio', Jalgaon")
    elif mode == 'noindex':
        switch('noindex')
        print("\nThe site is hidden from search engines again.")
    else:
        print(__doc__)
