#!/usr/bin/env python3
"""Repo hygiene gate for np-kb-public.

Enforces, over every text file in the repo:
  1. No references to private channels (staff-chat, watch-list, etc.).
  2. No person-identifying field names in data (owner, poster, author, message_id...).
  3. No absolute local paths (C:\\, /home/, /mnt/).
  4. Data files parse as JSON, every record `src` resolves in its file's `sources`,
     every source origin/confidence is a legal enum value, and no source cites a
     private channel.
  5. sourcedValue discipline: objects with a `value` key must carry `src` (when
     value is non-null) or `status` (when null).

A separate, private-side name scrub (not in this repo) runs before every push.
Exit code 0 = clean, 1 = violations found.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PRIVATE_CHANNEL_TOKENS = [
    "staff-chat", "staff chat", "watch-list", "watch list", "watchlist",
    "dossier", "mod-chat", "admin-chat",
]
FORBIDDEN_FIELDS = {"owner", "owned_by", "owned_status", "poster", "author",
                    "message_id", "message_ids", "discord_user", "player_name"}
PATH_RE = re.compile(r"[A-Za-z]:\\\\|/home/|/mnt/")
ORIGINS = {"dev-doc", "wiki", "discord-public", "in-game-tooltip", "in-game-measured", "player-reported", "community-dataset", "game-esm"}
CONFIDENCE = {"dev-stated", "measured", "player-reported", "provisional", "contested"}

errors = []

def err(path, msg):
    errors.append(f"{path}: {msg}")

def walk_fields(obj, path, fpath):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.lower() in FORBIDDEN_FIELDS:
                err(fpath, f"forbidden field '{k}' at {path}")
            if k == "value" and isinstance(obj, dict):
                if v is None and "status" not in obj:
                    err(fpath, f"null value without status at {path}")
                if v is not None and "src" not in obj and "status" not in obj:
                    err(fpath, f"value without src at {path}")
            walk_fields(v, f"{path}.{k}", fpath)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk_fields(v, f"{path}[{i}]", fpath)

def check_json(fpath):
    try:
        doc = json.loads(fpath.read_text(encoding="utf-8"))
    except Exception as e:
        err(fpath, f"invalid JSON: {e}")
        return
    walk_fields(doc, "$", fpath)
    if isinstance(doc, dict):
        sources = doc.get("sources", {})
        for skey, s in sources.items():
            if s.get("origin") not in ORIGINS:
                err(fpath, f"source '{skey}' has illegal origin {s.get('origin')!r}")
            if s.get("confidence") not in CONFIDENCE:
                err(fpath, f"source '{skey}' has illegal confidence {s.get('confidence')!r}")
            chan = (s.get("channel") or "") + (s.get("url") or "")
            for tok in PRIVATE_CHANNEL_TOKENS:
                if tok in chan.lower():
                    err(fpath, f"source '{skey}' cites a private channel")
        # every record src resolves
        def srcs_resolve(obj, path):
            if isinstance(obj, dict):
                if "src" in obj and isinstance(obj["src"], str) and sources and obj["src"] not in sources:
                    err(fpath, f"unresolved src '{obj['src']}' at {path}")
                for k, v in obj.items():
                    srcs_resolve(v, f"{path}.{k}")
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    srcs_resolve(v, f"{path}[{i}]")
        srcs_resolve(doc, "$")

def main():
    for fpath in sorted(ROOT.rglob("*")):
        if not fpath.is_file() or ".git" in fpath.parts:
            continue
        if fpath.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        text = fpath.read_text(encoding="utf-8", errors="replace")
        low = text.lower()
        for tok in PRIVATE_CHANNEL_TOKENS:
            if tok in low and fpath.name != "check_public.py":
                err(fpath, f"private-channel token '{tok}' present")
        if PATH_RE.search(text) and fpath.name != "check_public.py":
            err(fpath, "absolute local path present")
        if fpath.suffix == ".json" and fpath.parent.name == "data":
            check_json(fpath)
    if errors:
        print(f"FAIL — {len(errors)} violation(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("check_public: clean")

if __name__ == "__main__":
    main()
