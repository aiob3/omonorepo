# Agent directives for omonorepo

Read this before changing anything in this repository or in any plugin under
`plugins/`. It applies to every agent (Claude Code, Codex, or any other).

## What this repository is

omonorepo is the **normalizer for Omarchy plugins**. The marketplace validates each
plugin on its own; nobody validates how plugins relate to each other. omonorepo
answers three questions for the user: *Do I already have this? Does it conflict with
anything? What does it depend on?* See [PRODUCT.md](PRODUCT.md).

It is also the home of a **series of plugins**. Each plugin lives in its own
repository (the marketplace requires `manifest.json` at the root) and joins this one
as a git submodule under `plugins/`. **omany** is the first in the series: it makes
AI agents consistent (all open in Herdr, four slots, the Omarchy skill on the first
turn).

## Language

- All documentation is in **English**, end to end: README files, PRODUCT.md,
  acceptance records, compliance rules, code comments, commit messages. English
  leaves no room for ambiguity, for people and for agents.
- The only Portuguese text is the closing section of a README (this repository's and
  each plugin's main page), after `<a id="tupiniquim"></a>`, marking the work as made
  in Brazil. The README's first line after the title is always
  `🇺🇸 English | 🇧🇷 Tupiniquim`, linking to both sections.

## How work moves from idea to marketplace

1. **Build** in `/data/omonorepo/plugins/<plugin>`, committing as you go.
2. **Compliance:** run `compliance/bin/omono-check plugins/<plugin>` and fix every
   failure. Rules and their sources are in [compliance/RULES.md](compliance/RULES.md).
   A new rule found in practice goes into RULES.md and the checker, not only into
   one plugin.
3. **Acceptance in real use:** the operator presses the key or clicks; the agent
   confirms through logs and state and records the result in
   `docs/<plugin>/acceptance/`. No autonomous tests, no break-it tests.
4. **Preview first, in our repository:** push to the private GitHub repositories and
   let the operator review the pages before anything is public.
5. **Only with the operator's explicit go:** make the repositories public, run the
   marketplace steps (validate, install from the public URL, submission issue) and
   follow up until the listing is verified.
6. **While a submission waits for approval,** the marketplace validation is bound to
   one commit, and a different commit at approval time blocks publication. After
   pushing to the plugin, edit the submission issue so the bot validates the new
   HEAD, and confirm both reports name that commit.

## Rules that are easy to break

- **Consent:** a plugin never changes user configuration (`shell.json`,
  `bindings.lua`, bar placement, default agent) without an explicit user action.
- **Never run an agent binary to inspect it.** Omarchy writes first-run stubs that
  install the agent when executed. Read the file or ask `mise where`.
- **No personal data** in any repository or screenshot: no local paths under `/data`
  or `/home`, host names, usage limits, private notes.
- **Omarchy shell changes** (new QML files, changed kinds) need `omarchy restart shell`;
  see compliance/RULES.md for the known traps.
- **Outward actions** (creating or publishing repositories, opening marketplace
  issues) need the operator's explicit go each time.

## Marketplace listing

The marketplace listing shows only a short description and **one** preview image, so
both must carry the whole proposal on their own: what the plugin does, why it is
different, at a glance. The repository README extends this with the full gallery,
the reasoning, and the details a user needs to understand the work.
