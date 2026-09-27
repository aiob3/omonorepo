# Compliance rules

Every plugin in the series passes these rules before it is published. Each rule has
an ID, the source it comes from, and whether `bin/omono-check` checks it
automatically (**auto**), flags it for a person to confirm (**review**), or leaves it
to the acceptance run (**manual**).

Sources:
- **[form]** marketplace submission form, `omacom/omarchy-plugin-marketplace/.github/ISSUE_TEMPLATE/submit-plugin.yml`
- **[scan]** marketplace Automated Security Baseline, `scripts/security-baseline-policy.mjs` and `VERIFICATION.md`
- **[omarchy]** Omarchy plugin reference and `omarchy plugin validate`
- **[top]** what the most starred verified plugins publish (omapods, time-machine, omaproton-vpn, omanki)
- **[ours]** lessons from building omany; see `docs/omany/acceptance/`

## Marketplace listing

| ID | Rule | Source | Check |
|---|---|---|---|
| M1 | `omarchy plugin validate` passes on the plugin folder | [omarchy] | auto |
| M2 | Public repository with `manifest.json`, `README.md` and `LICENSE` at the root | [form] | auto (files) |
| M3 | `docs/<plugin>/listing.json` declares one category from the form's list | [form] | auto |
| M4 | 1 to 3 tags, all from the form's list (more than three are rejected); the manifest uses the same tags | [form] | auto |
| M5 | `preview.png` at the root, at least 1200 px wide, 16:9 or 4:3; the listing shows only this image | [top] | auto |
| M6 | The listing description says what the plugin does and why it differs, in one or two sentences | [form] [top] | auto (length) + review |
| M7 | Maintainer notes list dependencies, permissions and anything a reviewer must know | [form] | auto (present) |

## Security baseline

The marketplace scans the exact commit statically and never runs it. A plugin with
none of the capabilities below is verified automatically; any capability means a
maintainer must review it. Two rules block publication outright.

| ID | Rule | Source | Check |
|---|---|---|---|
| S1 | No blocking rules: passwordless sudoers for dangerous commands, privileged process control from shared temp paths | [scan] | auto |
| S2 | Know which capabilities the scanner will see: installer or setup path, package management, privilege (`sudo`, `pkexec`), remote source build, bundled executable binary, service management, sudoers edits | [scan] | auto (flag) |
| S3 | No download piped to a shell, no unpinned remote Git execution | [scan] | auto |

## Consent and behavior

| ID | Rule | Source | Check |
|---|---|---|---|
| C1 | The plugin never changes user configuration without an explicit user action: `shell.json`, `bindings.lua`, bar placement, the default agent | [form] | review (lists every write) |
| C2 | No agent or tool binary is run just to inspect it; Omarchy first-run stubs install when run | [ours] | review |
| C3 | Launching agents in approval-skipping modes is stated plainly in the README | [ours] | auto (text) |
| K1 | Every key the README tells users to bind is free on a stock Omarchy, unless the README frees it first with `hl.unbind`. Checked against the live Hyprland bindings with omaplug's own conflict logic (`plugins/omaplug/shortcut.py`) | [ours] (Super+Ctrl+Shift+G opened Google Messages too) | auto |
| K2 | Prefer letters terminals and agent TUIs do not use with Ctrl (avoid P, N, R, L, U, W, K, A, E, D). A combination Hyprland does not catch reaches the focused app: Super+Ctrl+Shift+P recalled the previous prompt, like Ctrl+P | [ours] | review |

## Documentation

| ID | Rule | Source | Check |
|---|---|---|---|
| D1 | README sections: requirements, install, remove, how it works, what it writes, troubleshooting | [top] | auto (headings) |
| D2 | Removal covers every file the plugin leaves behind | [top] [form] | review |
| D3 | All documentation is in English; a README may close with a Portuguese section after `<a id="tupiniquim"></a>`, announced in its first line as `🇺🇸 English \| 🇧🇷 Tupiniquim` | [ours] | auto (heuristic) |
| D4 | Third-party assets (icons, fonts) are credited with their license | [form] | review |

## Hygiene

| ID | Rule | Source | Check |
|---|---|---|---|
| H1 | No personal data: local paths under `/data` or `/home`, host names, user names | [ours] | auto |
| H2 | A git tag `v<manifest version>` exists for the version being published | [top] | auto |
| H3 | No tracked build junk (`__pycache__`, `*.pyc`, editor backups) | [ours] | auto |
| H4 | A change that ships (`manifest.json`, `bin/`, `assets/`, `*.qml`) moves the manifest version in the same pull request. H2 alone does not catch this: it only asks whether a tag exists for the version already in the manifest, so code merged without a bump keeps passing on the old version and its old tag | [ours] (agy reached omany's main at 0.11.2, the version the marketplace had already validated, so the listing could not see the update) | auto (`omono-version`, in the `version guard` workflow) |

## Releasing

The version is the only thing the marketplace uses to tell one snapshot from
another, and a listing is bound to one exact commit. Two automated steps keep that
honest, and neither of them publishes anything on its own:

1. **`version guard`** runs on every pull request, including from forks. It fails
   when something that ships changed and `manifest.json` kept its version, and it
   prints the version to use. The level comes from Conventional Commits, the form
   contributions already arrive in: `feat` is a minor bump, a `!` or
   `BREAKING CHANGE` is major, anything else is a patch.
2. **`release`** is a button a maintainer presses (`workflow_dispatch`). It reruns
   the compliance rules, creates the `v<version>` tag H2 asks for, and prints a
   marketplace update link with the action, plugin ID, repository and exact commit
   already filled in.

Opening the marketplace request stays a person's click. Outward actions need the
operator's explicit go each time, and the exact commit deserves one last look
before it becomes a public snapshot. Automation removes the typing, not the
decision.

## Known Omarchy shell traps (build time)

- **"File name case mismatch"** when loading a new or renamed QML file: Qt caches the
  plugin directory listing; run `omarchy restart shell`.
- **Enabled but no icon:** a leftover `plugins[]` entry from a version without
  `bar-widget` stops the shell from placing it; `omarchy plugin disable` then `enable`.
- **Invisible bar widget:** the root needs `implicitWidth`/`implicitHeight` from its button.
- **SVG as a `data:` URI does not render:** ship a file and tint it with `MultiEffect`.
- **Two bars, two widgets:** with more than one monitor, only the first widget
  registers an IPC target; the warning for the second is expected.
