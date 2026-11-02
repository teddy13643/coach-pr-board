#!/usr/bin/env python3
"""把 coach 的 pr-board.json 塞進 template.html，產出 GitHub Pages 用的 index.html 與 Claude Artifact 用的 artifact.html。"""
import json, pathlib
here = pathlib.Path(__file__).parent
data = pathlib.Path.home() / ".claude/skills/coach/data/pr-board.json"
payload = json.dumps(json.loads(data.read_text()), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = (here / "template.html").read_text().replace("__DATA__", payload)
(here / "index.html").write_text(html)
# Artifact 發布時會自己包 doctype／html／charset／viewport，這四行要拿掉
artifact = "\n".join(html.split("\n")[4:])
(here / "artifact.html").write_text(artifact)
print("built index.html + artifact.html", len(html), "bytes")
