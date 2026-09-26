# omany acceptance record

Done in real use on 2026-09-25 and 26, on an Omarchy workstation with Hyprland 0.56,
Herdr 0.8.2, Claude Code 2.1.283 and Codex 0.157. Test rule: the operator presses the
key or clicks, and the assistant confirms through the log (`~/.local/state/omany.log`)
and Herdr's state. No automated tests.

## What was accepted

| Feature | Result |
|---|---|
| Super+Ctrl+Shift+A opens the default agent in Herdr, a new tab per press, a single window | accepted |
| Super+Ctrl+Shift+Z opens the other agent (Claude Code ↔ Codex) | accepted |
| Super+Ctrl+Shift+S / X open the agents picked for the slots | accepted (Copilot, Grok) |
| An empty slot warns and opens nothing | accepted |
| Omarchy skill on the first turn (`/omarchy` in Claude Code, `$omarchy` in Codex) | accepted |
| Bar icon, right after the clock | accepted |
| Panel: slots with a picker, Open, running agents with Focus, installed agents | accepted |
| Settings: position, workspace, folder with Save, skill | accepted |
| Reset to a fresh install, confirmed with two clicks | accepted |

## Problems found and fixed along the way

- **Loose window:** Omarchy's original key opened the agent outside Herdr.
- **Codex Enter:** `$` opens the skill menu, and the first Enter only picks the item.
- **Cold start:** with the Herdr server stopped, the window must open before any command.
- **Invisible icon:** without `implicitWidth` the widget had zero width on the bar.
- **"File name case mismatch":** Qt's directory cache; `omarchy restart shell` clears it.
- **Plugin "enabled" but no icon:** a leftover `plugins[]` entry in `shell.json`.
- **Agents Herdr cannot recognize** (OpenClaw, Crush, Muse): they open as a plain command in a tab.
- **First-run installer stubs:** some agents install on first run; the panel reads the file and never runs it.
- **Unnamed Grok:** a retry found the agent already running; now it only gets its name.
- **Omarchy's default-agent bias:** installing an agent from the menu makes it the default; omany's slot A can stay independent.

## Screenshots

| Preview | Panel | Settings | Herdr |
|---|---|---|---|
| ![](preview.png) | ![](panel.png) | ![](settings.png) | ![](herdr.png) |
