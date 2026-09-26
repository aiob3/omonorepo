# LionTUI on Omarchy, end to end

[LionTUI](https://github.com/LionLabsCommunity/LionTerminalTUI) (`lion`) is the
LionLabs community's terminal agent: one binary, five providers (Claude, Codex, Grok,
Kimi, Ollama) behind a single event contract. This record covers installing it from
zero on a freshly reinstalled Omarchy and opening it through omany.

The LionTUI repository is private to the LionLabs community; installing it needs an
account with access.

This is a community validation record, not an official LionLabs or Omarchy
certification.

## Fixed set

| Item | Value |
|---|---|
| LionTUI revision | `be50155e1b1207abf72781caf19da95bc1757aa1` (v1.0.0) |
| Omarchy | 4.0.4-1, x86_64, kernel 7.2.5-3-omarchy |
| Hyprland | v0.56.2 |
| Herdr | 0.8.2 |
| Node / npm | 26.7.0 / 11.19.0, via mise |
| omany | 0.10.2 (with LionTUI support, commit `4880ed4`) |
| `package.json` SHA-256 | `ad7b6742a058d4c8af489f69b9ad835c161a913a03c633c3a06e42ec68a18eeb` |
| `package-lock.json` SHA-256 (official) | `be74f1f53f9789d821887e8e66a24435987e11b3b5476117d1f2feeafba21c1d` |

## Starting point

Omarchy reinstalled on 2026-09-25 (factory reset). Before step 1: no `lion` command,
no copy of the repository under `/data`, Node 26.7.0 from mise (LionTUI needs
22.19 or newer), Herdr 0.8.2, omany 0.10.2.

## Installation, as run on 2026-09-26

| Step | Command | Result |
|---|---|---|
| 1 | `gh repo clone LionLabsCommunity/LionTerminalTUI /data/LionTerminalTUI` | commit `be50155`, "LionTUI v1.0" |
| 2 | `npm install` | 188 packages, 0 vulnerabilities |
| 3 | `npm run build` | TypeScript build, `dist/cli.js` executable |
| 4 | `npm link` | `lion` in mise's Node `bin` directory |
| 5 | `mise reshim` | **Omarchy-specific.** The Omarchy shell only looks in `~/.local/share/mise/shims`; without a reshim it cannot find `lion`, so keys and the omany panel would not start it |

Step 5 is not in LionTUI's README: it only shows up on a fresh Omarchy, where the
desktop shell, not an interactive terminal, starts the agent.

## Findings for the LionTUI maintainers

1. **`mise reshim` on Omarchy.** With Node from mise (Omarchy's default), `npm link`
   puts `lion` where interactive shells find it but the desktop shell does not.
   Adding `mise reshim` to the install steps fixes it.
2. **Lockfile version.** In v1.0 `package.json` says `1.0.0` and `package-lock.json`
   says `0.1.0`, so `npm install` (the README's command) rewrites the lockfile's two
   version fields. No dependency changes. The official lockfile was restored after
   the install, and no versioned file of the repository was left modified.

## Opening it through omany

Herdr has no agent kind for LionTUI, so omany opens it as a plain command (`lion`) in
a new Herdr tab, like OpenClaw, Crush and Muse. It gets the tab, the workspace and
the working folder; it does not get Herdr's agent status or `herdr agent prompt`.
omany does not send the Omarchy skill to it: LionTUI isolates its providers from the
machine's Claude and Codex settings by design.

Expected on first run in `~/Work`: LionTUI needs git for checkpoints and `/undo`;
`~/Work` is not a git repository, so it offers to run `git init`. The answer is the
user's.

## Acceptance

| Check | Result |
|---|---|
| Installed from zero on a reinstalled Omarchy | done (table above) |
| omany lists `lion` as installed | done |
| Slot X set to `lion` through the panel's searchable picker (typing "li") | accepted, 2026-09-26 02:05 |
| It opens in a new Herdr tab of the user's `sistema` session, in `~/Work` | accepted: omany log `ok: lion in wY:p1 (plain command: lion)` at 02:04:41 |
| LionTUI boots and checks its providers | accepted: "2 de 5 prontos para usar" (Claude with subscription, Codex) |
| A second press opens another tab, not another window | not tested yet |

Observed along the way:

- On first run in `~/Work`, LionTUI offered `git init`; the operator accepted, and
  `~/Work` became a git repository (branch `master`, no commits). Herdr then shows
  the branch under the workspace.
- Herdr listed the LionTUI tab as a `claude` agent while LionTUI ran its Claude
  provider, since it detects the Claude SDK process inside the tab.
