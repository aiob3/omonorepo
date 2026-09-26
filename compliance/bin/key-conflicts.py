#!/usr/bin/env python3
"""key-conflicts.py <plugin-dir> <plugin-id>: check every key the plugin's README
tells users to bind against the live Hyprland bindings (Omarchy defaults included).

Reuses omaplug's own conflict logic (plugins/omaplug/shortcut.py), so the series and
the plugin manager agree on what a conflict is. Keys the README frees first with
hl.unbind, and bindings that already belong to this plugin, are not conflicts.
Prints one line per conflict; exit status = number of conflicts."""

import json
import re
import subprocess
import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[2]
sys.dont_write_bytecode = True  # do not leave __pycache__ inside the omaplug checkout
sys.path.insert(0, str(repo / "plugins" / "omaplug"))
from shortcut import combination, conflict  # noqa: E402

plugin_dir, plugin_id = Path(sys.argv[1]), sys.argv[2]
readme = (plugin_dir / "README.md").read_text()

bound = re.findall(r'o\.bind\(\s*"([^"]+)"', readme)
freed = {combination(c)[0] for c in re.findall(r'hl\.unbind\(\s*"([^"]+)"', readme)}
# Lua bindings show up as dispatcher "__lua" with an opaque argument, so this
# plugin's own bindings are recognized by description: the ones the README uses,
# or any that names the plugin.
own_descriptions = set(re.findall(r'o\.bind\(\s*"[^"]+",\s*"([^"]+)"', readme))
short_name = plugin_id.rsplit(".", 1)[-1]

live = json.loads(subprocess.run(["hyprctl", "-j", "binds"], capture_output=True, text=True, check=True).stdout)
others = [b for b in live
          if plugin_id not in str(b.get("arg", ""))
          and b.get("description", "") not in own_descriptions
          and short_name not in b.get("description", "")]

conflicts = 0
for combo in dict.fromkeys(bound):
    normalized = combination(combo)[0]
    if normalized in freed:
        continue
    message = conflict(others, normalized, plugin_id)
    if message:
        conflicts += 1
        print(f"{normalized}: {message}")
sys.exit(conflicts)
