---
name: latex-on-windows
description: Compile LaTeX (resume, report) on Windows with MiKTeX. Use whenever a .tex file must be built or its page count checked on a Windows machine.
---
# LaTeX on Windows (MiKTeX)

- Install: `winget install --id MiKTeX.MiKTeX --exact --scope user --silent --accept-package-agreements --accept-source-agreements`. Binaries land in `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64` (pdflatex, xelatex, initexmf, mpm). They may NOT be on PATH in new shells: prepend it (`$env:PATH = "$bin;$env:PATH"`).
- Missing packages install on the fly after `initexmf --set-config-value "[MPM]AutoInstall=1"`.
- Build in a scratch dir, never in the project: copy the .tex and every asset it names (`\includegraphics` files), then `pdflatex -interaction=nonstopmode -halt-on-error file.tex` (twice if hyperref or outlines changed). The line `Output written on x.pdf (N pages ...)` gives the page count.
- PowerShell shows `NativeCommandError` plus "you have not checked for MiKTeX updates": harmless noise; judge success by the `Output written` line.
- `Out-File -Encoding utf8` adds a BOM; pdflatex accepts it.
- Page count only matches the real document if the real image assets are present. A stand-in logo changed a tight one-page resume to two pages; the environment, not the edit, was the cause. Get the real assets before trusting a page count.
- `Font shape OT1/cmr/bx/sc undefined` (bold small caps) is normal for common resume templates.
