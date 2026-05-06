#!/usr/bin/env python3
"""
Screenshot helper for XAUTOMATA User Manual.

Lists all missing screenshots grouped by section/dashboard.
For each one: wait for confirmation, detect the latest file in ~/Screenshots,
ask for confirmation, then copy it to the correct docs/images/ path.

Usage:
    python3 screenshot_helper.py
"""

import os
import re
import sys
import shutil
from pathlib import Path
from itertools import groupby

DOCS_DIR = Path(__file__).parent / "docs"
SCREENSHOTS_DIR = Path.home() / "Screenshots"

# Map md file paths (relative to docs/) to human-readable section labels.
# Matched as prefix or suffix — first match wins.
SECTION_MAP = [
    ("widgets/physical_security_capacity_management", "Physical Security — Capacity Management"),
    ("widgets/physical_security_assets_hierarchy",    "Physical Security — Dashboard Service"),
    ("widgets/physical_security_asset_map",           "Physical Security — Dashboard Service"),
    ("widgets/physical_security_firmware_scheduler",  "Physical Security — Dashboard Dispositivo"),
    ("dashboards/physical_security",                  "Physical Security — Dashboards overview"),
    ("dashboards/",                                   "Dashboards"),
    ("widgets/",                                      "Widgets"),
    ("getting_started/",                              "Getting Started"),
    ("data_manager/",                                 "Data Manager"),
    ("cost_management/",                              "Cost Management"),
    ("administration/",                               "Administration"),
    ("super_admin/",                                  "Super Admin"),
]

def section_for(rel_path: str) -> str:
    for prefix, label in SECTION_MAP:
        if rel_path.startswith(prefix) or rel_path.endswith(prefix.rstrip("/")):
            return label
    return rel_path

def parse_images(filepath: Path):
    """Yield (img_rel_path, caption) pairs from a markdown file."""
    lines = filepath.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'!\[[^\]]*\]\(([^)]+)\)', line)
        if m:
            img_path = m.group(1)
            caption = ""
            if i + 1 < len(lines) and lines[i + 1].strip() == "/// caption":
                if i + 2 < len(lines):
                    caption = lines[i + 2].strip()
            yield img_path, caption

def latest_screenshot() -> Path | None:
    files = [
        f for f in SCREENSHOTS_DIR.iterdir()
        if f.suffix.lower() in (".png", ".jpg", ".jpeg")
    ]
    return max(files, key=lambda f: f.stat().st_mtime) if files else None

def collect_missing():
    seen = set()
    items = []

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        if md_file.name.endswith(".it.md"):
            continue
        rel_md = str(md_file.relative_to(DOCS_DIR))
        section = section_for(rel_md)

        for img_rel, caption in parse_images(md_file):
            dest = (md_file.parent / img_rel).resolve()
            try:
                dest.relative_to(DOCS_DIR.resolve())
            except ValueError:
                continue
            key = str(dest)
            if key in seen or dest.exists():
                continue
            seen.add(key)
            items.append({
                "section": section,
                "caption": caption,
                "dest": dest,
                "filename": dest.name,
            })

    # Sort by section order, then by Fig number in caption, then filename
    order = {label: i for i, (_, label) in enumerate(SECTION_MAP)}

    def fig_num(item):
        m = re.search(r'Fig\.(\d+)', item["caption"])
        return int(m.group(1)) if m else 99

    items.sort(key=lambda x: (order.get(x["section"], 99), fig_num(x), x["filename"]))
    return items

def main():
    if not SCREENSHOTS_DIR.exists():
        print(f"⚠️  Screenshots folder not found: {SCREENSHOTS_DIR}")
        sys.exit(1)

    missing = collect_missing()

    if not missing:
        print("✅  No missing screenshots — all images are in place!")
        return

    total = len(missing)
    print(f"\n📸  SCREENSHOT HELPER — {total} image{'s' if total != 1 else ''} missing\n")

    done = 0
    skipped = 0
    current_section = None

    for idx, item in enumerate(missing):
        # Print section header when it changes
        if item["section"] != current_section:
            current_section = item["section"]
            print("─" * 62)
            print(f"  📁  {current_section}")
            print("─" * 62)

        remaining = total - idx
        dest_short = item["dest"].relative_to(DOCS_DIR.parent)
        print(f"\n  [{idx+1}/{total}]  {item['filename']}")
        if item["caption"]:
            print(f"         {item['caption']}")
        print(f"         → {dest_short}")

        while True:
            try:
                action = input("\n  [Enter] copy latest screenshot   [s] skip   [q] quit  › ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                print(f"\n\nInterrupted. {done} copied, {skipped} skipped.")
                sys.exit(0)

            if action == "q":
                print(f"\n  Quit. {done} copied, {skipped} skipped, {remaining - 1} remaining.")
                sys.exit(0)

            if action == "s":
                skipped += 1
                print("  ↷  Skipped.")
                break

            if action == "":
                shot = latest_screenshot()
                if not shot:
                    print("  ⚠️   No screenshots found in ~/Screenshots. Take one first.")
                    continue

                size_kb = shot.stat().st_size // 1024
                print(f"\n  Latest:  {shot.name}  ({size_kb} KB)")
                try:
                    confirm = input(f"  Copy as  {item['filename']}? [y/n] › ").strip().lower()
                except (KeyboardInterrupt, EOFError):
                    print(f"\n\nInterrupted. {done} copied, {skipped} skipped.")
                    sys.exit(0)

                if confirm == "y":
                    item["dest"].parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(shot, item["dest"])
                    done += 1
                    print(f"  ✅  Saved → {dest_short}")
                    break
                else:
                    print("  Try again — take a new screenshot or press [s] to skip.")

    print(f"\n{'─' * 62}")
    print(f"  Done. ✅ {done} copied   ↷ {skipped} skipped   ◻ {total - done - skipped} remaining")
    print(f"{'─' * 62}\n")

if __name__ == "__main__":
    main()
