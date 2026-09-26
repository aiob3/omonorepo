# LionTUI and LionClaw Desktop on Omarchy: two onboarding paths

The LionLabs community ships two front doors, and they land on Omarchy differently.
Each path keeps its own record: the Desktop homologation lives with its installer
([HOMOLOGACAO.md](https://github.com/aiob3/lionclaw-omarchy/blob/main/HOMOLOGACAO.md)),
where the community publication started; LionTUI's lives here. This page only compares them as observed on one station, validated together with the
operator on 2026-09-26. It is a community validation record, not an official
LionLabs or Omarchy certification.

- **LionTUI** (`lion`): the system's terminal assistant, opened through omany in a
  Herdr tab. Details: [liontui.md](liontui.md).
- **LionClaw Desktop**: the Electron app, installed with the community installer
  [aiob3/lionclaw-omarchy](https://github.com/aiob3/lionclaw-omarchy) and opened
  from the application menu.

## Fixed set

| Item | LionTUI | LionClaw Desktop |
|---|---|---|
| Revision | `be50155` (v1.0.0) | `b0907f7` (3.9.0) |
| Node | 26.7.0, the system default from mise | 24.11.1, pinned through mise; the system default is untouched |
| Where it runs | Herdr tab, working folder `~/Work` | Its own window, native Wayland |
| How it opens | omany key or bar panel | Application menu (`lionclaw.desktop`) |

Shared: Omarchy 4.0.4, Hyprland 0.56.2, Herdr 0.8.2, omany 0.11.0, Voxtype 1.0.1.

## Side by side

| Topic | LionTUI | LionClaw Desktop |
|---|---|---|
| Install | `gh repo clone`, `npm install`, `npm run build`, `npm link`, then `mise reshim` (Omarchy-specific) | Installer steps: pinned Node, `npm ci`, `rebuild:electron`, native check (SQLite, PTY, keytar), `npm run build`, menu entry |
| Display | Terminal; nothing to adjust | Must run on **native Wayland** with the app's own `LIONCLAW_ENABLE_HARDWARE_ACCELERATION=1`. Under XWayland the UI doubled (Omarchy exports `GDK_SCALE=2`) and Voxtype dictation arrived as digits. Without the switch the native window never shows |
| Voice | Voxtype types into the terminal like any other app | Same, once native on Wayland. Voxtype stays in its `type` mode; the installer no longer changes it |
| First run | Asks to `git init` the working folder; offers to import the LionClaw persona | Password, orchestrator SDK choice, API key, then an interview in the chat |
| Credentials | Reuses the machine's agents: Claude subscription and Codex CLI ("2 de 5 prontos"). No key asked | The recommended Claude Agent SDK asks for an Anthropic **API key** (billed per use, separate from the subscription), stored in the OS keychain. Codex SDK uses the Codex CLI login |
| Files it writes | `~/.lion/` (`providers.yaml`, `SOUL.md`, `USER.md`) | `~/.lionclaw/` (103 agents, skills, persona, database), `~/.config/lionclaw/` (Electron profile) |
| Effect on other agents | None observed | Writes about 18 `lionclaw-*` and helper MCP servers into **`~/.codex/config.toml`**, the global Codex config. Every Codex session on the machine, including the one omany opens, now loads them |
| Host access | Runs its providers in the tab's folder | Its agents run shell commands on the host from the GUI. The composer shows an "Ignorar permissões" (skip permissions) toggle |
| Omarchy skill | Not sent: LionTUI isolates its providers | Not applicable |

## How the two connect

`~/.lionclaw` is the bridge. When LionClaw Desktop has already run, LionTUI finds
its persona and offers to import `SOUL.md` and `USER.md` into `~/.lion/`. Order
matters: install and onboard the Desktop first, and LionTUI starts with the same
persona.

## Findings from the joint validation

1. **`git init` in the agents' home folder happened again.** On LionTUI's first
   question in `~/Work` the answer was yes, and `~/Work/.git` was created
   (02:32), even with omany's notice in place. A notice is not enough; the
   suggested `LION_NO_GIT_PROMPT` option (or a flag) is the real fix.
2. **XWayland is the root of two Desktop defects** (scale and dictation). Native
   Wayland fixes both without touching Voxtype or the system configuration.
3. **The Desktop hides its window on native Wayland by default.** It disables GPU
   acceleration on Linux and shows the window only on `ready-to-show`. That is why
   the 3.8.0 record saw "no window" on Wayland.
4. **The Desktop changes the global Codex configuration.** This touches the
   Claude + Codex pair that omany opens. It is recorded here; any decision to
   isolate it (for example a separate `CODEX_HOME` for LionClaw) is the operator's.
5. **The Desktop can act as a system assistant.** Asked "Qual o status do
   sistema?", it found five failed systemd units. They were real: a zero-byte
   `/swap/swapfile`, a dirty NTFS volume that refuses to mount, and three
   automounts left failed after the USB disks dropped at 03:10:49.

## Which one for whom

- **LionTUI**: the inclusive entry point. One key, a terminal tab, the machine's
  existing Claude and Codex logins, no API key, nothing written outside `~/.lion/`.
- **LionClaw Desktop**: the full workspace (sub-agents, pipelines, kanban, vault).
  It needs a pinned toolchain, an API key for its recommended SDK, and it extends
  the global Codex configuration.

## Status

| Check | Result |
|---|---|
| LionTUI through omany, in `~/Work` | accepted (see [liontui.md](liontui.md)) |
| LionClaw 3.9.0 production build from the menu, native Wayland | accepted: window `LionClaw`, `xwayland: false`, started by the user session, chat answered |
| Dictation in the Desktop, development build | accepted by the operator |
| Dictation in the Desktop, production build from the menu | accepted by the operator |
