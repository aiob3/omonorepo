# Contributing to omonorepo

omonorepo is the normalizer for Omarchy plugins and the home of a series of plugins.
Read [AGENTS.md](AGENTS.md) first: it is written for people and agents alike.

## Kinds of contribution

- **A plugin of the series** (omany today): open the pull request in the plugin's own
  repository. Each one has its CONTRIBUTING.md.
- **Compliance rules** (`compliance/RULES.md`, `compliance/bin/`): a new rule needs a
  source (the marketplace, Omarchy, or a case found in real use) and, when it can be
  checked, a check in `omono-check`.
- **Normalization knowledge**: overlaps, conflicts and dependencies between plugins,
  starting with AI agents (see [PRODUCT.md](PRODUCT.md)).

## Adding a plugin to the series

1. The plugin lives in its own public repository with `manifest.json`, `README.md` and
   `LICENSE` at the root, and joins here as a submodule under `plugins/`.
2. Add `docs/<plugin>/listing.json` with the marketplace listing: category, one to
   three tags from the marketplace's list, a one-sentence description, maintainer notes.
3. `compliance/bin/omono-check plugins/<plugin>` passes with 0 FAIL.
4. It is tested in real use, and the record goes to `docs/<plugin>/acceptance/`.
5. Its README starts with `🇺🇸 English | 🇧🇷 Tupiniquim` and closes with the Portuguese
   section; everything else is in English.

## Automation

`.github/workflows/compliance.yml` runs `omono-check --ci` on every plugin of the
series for each pull request and push to `main`. Without an Omarchy session the check
validates the manifest statically and skips the live key check (K1); run it locally
on Omarchy for the full check before a release.
