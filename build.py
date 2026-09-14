#!/usr/bin/env python3
"""把 coach 的 pr-board.json 塞進 template.html，產出可直接發布的 index.html。"""
import json, pathlib
here = pathlib.Path(__file__).parent
data = pathlib.Path.home() / ".claude/skills/coach/data/pr-board.json"
payload = json.dumps(json.loads(data.read_text()), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = (here / "template.html").read_text().replace("__DATA__", payload)
(here / "index.html").write_text(html)
print("built index.html", len(html), "bytes")
