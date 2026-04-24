# Migration Notes

This plugin was created from the imported `meta-skills` folder in the workspace.
The source import remains untouched.

## Converted in this pass

- Scaffolded a repo-local Codex plugin at `plugins/meta-skills/`
- Added a local marketplace entry at `.agents/plugins/marketplace.json`
- Copied all 13 imported skills into the plugin's `skills/` folder
- Normalized obvious legacy provider-specific wording in copied markdown where safe
- Rewrote `audio-transcriber` to use the OpenAI API instead of legacy CLI assumptions
- Rewrote `mcp-builder` evaluation harness to use OpenAI function calling against MCP tools
- Updated several copied skills to use Codex-oriented language and defaults

## Likely usable now

- `fact-checker`
- `file-organizer`
- `find-skills`
- `frontend-slides`
- `humanizer`
- `decision-toolkit`
- `process-interviewer`
- `prompt-master`
- `audio-transcriber`
- `mcp-builder`
- `agent-browser`
- `deep-research`

These are either instruction-heavy or now aligned to Codex/OpenAI runtime expectations.

## Remaining polish opportunities

- `openrouter`
- `prompt-master`
- `find-skills`

These are already usable. Any further work here would be editorial only:

- narrowing example model lists
- tightening external repository references
- reducing cross-tool comparison text

## Notes

- `openrouter` includes its own source `plugin.json` inside the copied skill folder; it was preserved as source material, not treated as the top-level Codex plugin manifest.
- The main plugin manifest for this workspace is `.codex-plugin/plugin.json` under `plugins/meta-skills/`.
- The migrated scripts and Codex-facing skill instructions now use Codex/OpenAI-aligned runtime assumptions.
