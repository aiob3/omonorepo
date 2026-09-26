# omonorepo: the product

## The problem

The Omarchy marketplace grew fast: **4,178 plugins** in the catalog on 2026-09-26.
Many of them do the same thing, and nothing helps the user choose between them:

| Family | Plugins in the catalog |
|---|---|
| AI agents (agent, Claude, Codex, Herdr) | 228 |
| Herdr only | 29 |
| Clock, calendar, weather | 172 |
| Battery and power | 242 |

The marketplace validates **each plugin on its own**: the manifest, a static security
scan of the exact commit, and a submission checklist. It does **not** validate how
plugins relate to each other. A user who installs a plugin does not learn:

- what they **already have** that does the same thing (overlap);
- what will **fight** with what is already installed (conflict): the same key, the
  same IPC target, the same spot on the bar, two plugins editing the same config file;
- what it **depends on** (relationship): a plugin that needs Herdr, an agent, or
  another plugin.

The result is a system that piles up repeated functions and behaviors that step on
each other, and the user only finds out while using it.

## The proposal

omonorepo is the **normalizer** of what is installed. It answers three questions,
before and after installing:

1. **Do I already have this?** Functional overlap with what is installed.
2. **Does it conflict with anything?** Keys, IPC, bar placement, config files.
3. **What does it depend on?** Tools, agents, and other plugins.

It works on two fronts:

- **For plugin authors (compliance):** the rules of Omarchy, of the marketplace, and
  our own stability rules, with a check that every plugin in the series passes before
  it ships.
- **For users (normalization):** read the installed plugins, map overlaps, conflicts
  and dependencies, and propose a coherent setup.

## What we are not

omonorepo does **not** compete with the marketplace or with the community's curated
lists (awesome-omarchy and others). They answer *what exists*; we answer *how it fits
with what you already have*. The goal is to break a vicious cycle: today every plugin
arrives without any check against what is already installed, starting with what
Omarchy ships by default. Once a family is normalized, everything that comes after
it is checked against that baseline first. Where it helps, we contribute back to the
existing lists instead of creating a rival one.

## Where we start: AI agents

Agents are the family where the lack of consistency hurts the most. Every tool opens
agents its own way: Omarchy's default key opens a loose window, the Herdr plugins
only watch, and installers switch the default agent without asking.

**omany**, the first app in the series, makes this consistent:

- every agent opens in the same place (one Herdr workspace, one tab per agent, one window);
- four predictable slots (A default, Z its counterpart, S and X free), same rules for all;
- the agent starts with the system's context (the Omarchy skill on the first turn);
- the panel shows what is installed and what only installs on first use, without running anything.

Next steps on this front: show when another agent plugin is already installed and
what it does in common with omany, and unify how the default agent is chosen across
Omarchy and plugins.

## Inclusion: an entry point for communities

Normalizing agents also lowers the bar to start. When every agent opens the same way,
from one key or one click, a community can hand new collaborators a single, friendly
path into AI-assisted work instead of a stack of tools to learn.

The first case is the LionLabs community's **LionTUI**, one agent in front of five
providers and the community's entry point for people less familiar with code. With
the community's authorization, omany opens it like any other agent, and omonorepo
documents its onboarding end to end (`docs/integrations/liontui.md`).

## Relationship with omaplug

omaplug (our fork of the plugin manager) already handles key conflicts when it
assigns shortcuts. Item #1 of our backlog there is **"conflicts between active
plugins"**. It is the same front seen from the manager: omonorepo defines the rules
and the relationship map, and omaplug is one of the places where the user sees them.
