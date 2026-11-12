# Copy the kit's skills and templates into ~/.claude without overwriting anything.
# Usage: powershell -ExecutionPolicy Bypass -File scripts\install.ps1 [-DryRun] [-Vault DIR] [-Target DIR]
#   -DryRun   show what would be copied, change nothing
#   -Vault    also copy vault-template\ to DIR (skipped if DIR exists)
#   -Target   install root (default: $env:CLAUDE_HOME, else ~\.claude)
param(
  [switch]$DryRun,
  [string]$Vault = "",
  [string]$Target = ""
)
$ErrorActionPreference = "Stop"

$kit = Split-Path -Parent $PSScriptRoot
if (-not $Target) {
  if ($env:CLAUDE_HOME) { $Target = $env:CLAUDE_HOME } else { $Target = Join-Path $HOME ".claude" }
}
$script:copied = 0
$script:skipped = 0

function Copy-New([string]$Src, [string]$Dest) {
  if (Test-Path -LiteralPath $Dest) {
    Write-Output "skip (exists): $Dest"
    $script:skipped++
  } else {
    Write-Output "copy: $Dest"
    $script:copied++
    if (-not $DryRun) {
      $parent = Split-Path -Parent $Dest
      if (-not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent | Out-Null }
      Copy-Item -LiteralPath $Src -Destination $Dest -Recurse
    }
  }
}

if ($DryRun) { Write-Output "DRY RUN: nothing will be written" }
Write-Output "target: $Target"

Get-ChildItem -LiteralPath (Join-Path $kit "skills") -Directory | ForEach-Object {
  Copy-New $_.FullName (Join-Path (Join-Path $Target "skills") $_.Name)
}
Copy-New (Join-Path $kit "templates\CLAUDE.md") (Join-Path $Target "CLAUDE.md")
Copy-New (Join-Path $kit "settings.example.json") (Join-Path $Target "settings.example.json")

if ($Vault) { Copy-New (Join-Path $kit "vault-template") $Vault }

Write-Output "done: $($script:copied) copied, $($script:skipped) skipped"
Write-Output "Next: merge settings.example.json into settings.json by hand, then install plugins (plugins.md) and MCP servers (mcp.md)."
