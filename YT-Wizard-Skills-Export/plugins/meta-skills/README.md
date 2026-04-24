# Meta Skills Plugin

This plugin is a Codex-friendly wrapper around the imported `meta-skills` bundle in this workspace.

## What it contains

- A repo-local plugin manifest at `.codex-plugin/plugin.json`
- A copied skill set under `skills/`
- A local marketplace entry at `.agents/plugins/marketplace.json`

## Source and conversion approach

- Source bundle kept intact at `../../meta-skills/`
- Plugin copy lives at `./skills/`
- Obvious provider-specific usage headings were normalized in copied markdown where safe
- Script-heavy skills were not blindly rewritten, so the original logic remains inspectable

## Current intent

This first pass makes the bundle installable and easier to iterate on as a single plugin.
Use `MIGRATION_NOTES.md` to see which imported skills are already usable as instruction skills and which ones still need runtime migration.
