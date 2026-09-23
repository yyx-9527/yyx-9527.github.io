"""Optional Google Scholar statistics refresh; requires an explicit Scholar ID."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from scholarly import scholarly

scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
if not scholar_id:
    raise SystemExit("GOOGLE_SCHOLAR_ID is not configured.")

author = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
author["updated"] = datetime.now(timezone.utc).isoformat()
author["publications"] = {paper["author_pub_id"]: paper for paper in author.get("publications", [])}
results = Path("results")
results.mkdir(exist_ok=True)
(results / "gs_data.json").write_text(json.dumps(author, ensure_ascii=False, indent=2), encoding="utf-8")
badge = {"schemaVersion": 1, "label": "citations", "message": str(author.get("citedby", 0))}
(results / "gs_data_shieldsio.json").write_text(json.dumps(badge), encoding="utf-8")
print("Citation data updated.")
