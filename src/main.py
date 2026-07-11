"""WASH module starter template — minimal daemon with heartbeat."""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone

DATA_DIR = os.environ.get("MODULE_DATA_DIR", "/data")
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "30"))
GREETING = os.environ.get("GREETING", "Hello from WASH module")


def write_heartbeat() -> dict:
    payload = {
        "recordedAt": datetime.now(timezone.utc).isoformat(),
        "greeting": GREETING,
        "message": "Module starter is running",
        "tick": int(time.time()),
    }
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, "last_snapshot.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return payload


def main() -> None:
    while True:
        snap = write_heartbeat()
        print(f"[module-starter] heartbeat tick={snap['tick']}")
        time.sleep(max(10, POLL_INTERVAL))


if __name__ == "__main__":
    main()
