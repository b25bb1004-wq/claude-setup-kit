# Skill-trigger benchmark report

| Config | Runs | Errors | Trigger accuracy | False fires (expected none) | Graded success | Mean wall s | Tokens (in+out+cache) | Cost USD |
|---|---|---|---|---|---|---|---|---|
| kit | 2 | 0 | 2/2 | 0/1 | 2/2 | 7.2 | 88377 | 0.0066 |
| vanilla | 2 | 0 | 1/2 | 0/1 | 2/2 | 5.8 | 42449 | 0.0032 |

| Config | Prompt | Expected | Fired | Trigger OK | Graded |
|---|---|---|---|---|---|
| kit | p01 | claude-mcp-add-windows | claude-mcp-add-windows | True | True |
| vanilla | p01 | claude-mcp-add-windows | (none) | False | True |
| kit | n01 | (none) | (none) | True | True |
| vanilla | n01 | (none) | (none) | True | True |
