"""Check generated HTML, internal links, anchors and CSS assets without dependencies."""
import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.head_count = 0
        self.body_count = 0
        self.language = None
        self.has_base = False
        self.redirect = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "head":
            self.head_count += 1
        if tag == "body":
            self.body_count += 1
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "base":
            self.has_base = True
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirect = True
        if tag in {"a", "link"} and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in {"img", "script", "source"} and "src" in attrs:
            self.links.append(attrs["src"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", default="_site")
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    if not (root / "index.html").is_file():
        raise SystemExit("Missing generated index.html; run Jekyll first.")
    pages = {path: Page(path.read_text(encoding="utf-8")) for path in root.rglob("*.html")}
    errors = []

    def check(url, source):
        if not url or not url.strip():
            errors.append(f"{source.relative_to(root)}: empty link")
            return
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            return
        path = unquote(parsed.path)
        if args.baseurl and path.startswith("/"):
            if path == args.baseurl:
                path = "/"
            elif path.startswith(args.baseurl.rstrip("/") + "/"):
                path = path[len(args.baseurl):]
            else:
                errors.append(f"{source.relative_to(root)}: missing baseurl in {url}")
                return
        target = ((root / path.lstrip("/")) if path.startswith("/") else
                  source.parent / path) if path else source
        target = target.resolve()
        if not target.is_relative_to(root):
            errors.append(f"{source.relative_to(root)}: path escapes site: {url}")
            return
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file():
            errors.append(f"{source.relative_to(root)}: missing {url}")
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f"{source.relative_to(root)}: missing anchor {url}")

    for path, page in pages.items():
        if not page.redirect and (page.head_count != 1 or page.body_count != 1):
            errors.append(f"{path.relative_to(root)}: expected one head and one body")
        if page.has_base:
            errors.append(f"{path.relative_to(root)}: unexpected base element")
        for link in page.links:
            check(link, path)
    for path in root.rglob("*.css"):
        for url in re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", path.read_text(encoding="utf-8")):
            check(url, path)
    home = pages[root / "index.html"]
    if home.language != "zh-CN":
        errors.append("Homepage language must be zh-CN.")
    for section in ("about-me", "research", "publications", "education", "contact"):
        if section not in home.ids:
            errors.append(f"Homepage section missing: {section}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(pages)} HTML pages, internal links, anchors and CSS assets.")


if __name__ == "__main__":
    main()
