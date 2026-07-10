import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = ["en/index.html", "es/index.html"]


for page in PAGES:
    html = (ROOT / page).read_text(encoding="utf-8")
    match = re.search(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        html,
        re.S,
    )

    if not match:
        raise SystemExit(f"{page}: missing JSON-LD")

    data = json.loads(match.group(1))
    print(f"{page}: JSON-LD OK - {data['name']}")

    if 'fetchpriority="high"' not in html:
        raise SystemExit(f"{page}: hero fetchpriority missing")

    if html.count("<img") != html.count('width="'):
        raise SystemExit(f"{page}: some images are missing width attributes")

    if html.count("<img") != html.count('height="'):
        raise SystemExit(f"{page}: some images are missing height attributes")


css = (ROOT / "css/style.min.css").read_text(encoding="utf-8")
if css.count("{") != css.count("}"):
    raise SystemExit("css/style.min.css: unbalanced braces")

print("css/style.min.css: braces OK")
