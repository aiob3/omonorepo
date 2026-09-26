# LionTUI on Omarchy, end to end

[LionTUI](https://github.com/LionLabsCommunity/LionTerminalTUI) (`lion`) is the
LionLabs community's terminal agent: one binary, five providers (Claude, Codex, Grok,
Kimi, Ollama) behind a single event contract. This record covers installing it from
zero on a freshly reinstalled Omarchy and opening it through omany.

The LionTUI repository is private to the LionLabs community; installing it needs an
account with access.

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
| A slot set to `lion` opens it in a new Herdr tab, in `~/Work`, in the user's session | pending: operator test |
| A second press opens another tab, not another window | pending: operator test |
