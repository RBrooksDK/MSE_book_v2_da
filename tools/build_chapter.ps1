# Builds a working PDF containing only the selected chapter files, e.g.
#   .\tools\build_chapter.ps1 chapter00 chapter05
# The chapter counter is set so each chapter keeps its final number.
# References to chapters that are not included will show as "??".
param([Parameter(Mandatory = $true)][string[]]$Chapters)

$root = Split-Path $PSScriptRoot -Parent
Set-Location $root
$main = Get-Content main.tex -Raw -Encoding UTF8
$begin = $main.IndexOf('\mainmatter')
$end = $main.IndexOf('\end{document}')
$body = "\mainmatter`n"
foreach ($c in $Chapters) {
    if ($c -match '^chapter(\d+)$') {
        $n = [int]$Matches[1]
        $body += "\setcounter{chapter}{$($n - 1)}`n\input{$c}`n"
    } else {
        $body += "\appendix`n\input{$c}`n"
    }
}
$out = $main.Substring(0, $begin) + $body + "`n\printbibliography[heading=bibintoc, title=\ebibname]`n" + $main.Substring($end)
$name = 'work_' + ($Chapters -join '_')
[IO.File]::WriteAllText((Join-Path $root "$name.tex"), $out, (New-Object Text.UTF8Encoding $false))
latexmk -pdf -interaction=nonstopmode -halt-on-error "$name.tex" | Out-Null
$log = Get-Content "$name.log" -Raw
$pages = [regex]::Match($log, 'Output written on .*?\((\d+) pages').Groups[1].Value
"{0}: pages={1} errors={2} undefined-refs={3} missing-chars={4}" -f $name, $pages,
    ([regex]::Matches($log, '(?m)^! ')).Count,
    ([regex]::Matches($log, 'Reference `[^'']*'' on page')).Count,
    ([regex]::Matches($log, 'Missing character')).Count
[regex]::Matches($log, '(?m)^! .*$') | ForEach-Object { $_.Value }
