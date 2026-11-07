# Project settings

Project Folder: `/Users/gmahoney/projects/art-studio`

Settled 2026-11-07 by `/project-setup`. Every value is this Project's own; no home default was added.
The Project Folder is the git repo gabemahoney/art-studio, its only code folder (repo root). Worktrees go
under `.worktrees/`; the Ideas, Plans and Bugs hives live in `tickets/`. Both are git-ignored.

Deliberately absent:
- `child_watch_command`: this host ships no command that waits on Child Agents, so the Launcher's fallback applies.
- `ticket_links`: `protocol:ticket-bees.md` covers Dependency, Association and Source Reference.

ticket_system: bees
launcher: agent-director
prd_template: /Users/gmahoney/.sdlc/install/doc-templates/prd.md
new_idea_intake: /Users/gmahoney/.sdlc/install/intakes/interview.md
new_bug_intake: /Users/gmahoney/.sdlc/install/intakes/interview.md
research_location: /Users/gmahoney/research/tickets

## levels

max: {agent: claude-code, model: claude-opus-5-5, effort: max}
xhigh: {agent: claude-code, model: claude-opus-5-5, effort: xhigh}
high: {agent: claude-code, model: claude-opus-5-5, effort: high}
medium: {agent: claude-code, model: claude-opus-5-5, effort: medium}
low: {agent: claude-code, model: claude-sonnet-5-5, effort: low}

## thinking_levels

project-setup: medium
write-idea: medium
write-bug: medium
define-bug: high
fix-bug: medium
write-prd: xhigh
write-srd: max
write-plan: max
write-epic: xhigh
develop-epic: medium
idea-review: high
research: high
release: medium
configure-worktree: medium
teardown-worktree: medium
engineer: high
test-writer: high
doc-writer: high
model-writer: xhigh
model-review: xhigh
engineer-planner: high
test-writer-planner: high
doc-writer-planner: high
req-review: xhigh
code-review: xhigh
test-review: xhigh
doc-review: high
product-manager: xhigh
