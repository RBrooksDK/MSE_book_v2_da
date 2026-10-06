$filePath = "c:\Users\RIB\OneDrive - ViaUC\Arbejde\GitHub\MSE_book_v2\chapter02.tex"
$content = Get-Content -Raw $filePath

# Replace any \begin{example} that doesn't have a preceding empty line
# This regex ensures we don't add empty lines where they already exist
$updatedContent = $content -replace "([^\n])\n\\begin\{example\}", "`$1`n`n\begin{example}"

# Write the updated content back to the file
Set-Content -Path $filePath -Value $updatedContent

Write-Output "Empty lines added before Example environments where needed!"
