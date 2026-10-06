$files = Get-ChildItem -Path "*.tex" -Recurse

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Replace [h] with [htbp] for both figure and table environments
    $updatedContent = $content -replace '\\begin\{figure\}\[h\]', '\begin{figure}[htbp]'
    $updatedContent = $updatedContent -replace '\\begin\{table\}\[h\]', '\begin{table}[htbp]'
    
    # Save the modified content back to the file
    if ($content -ne $updatedContent) {
        Set-Content -Path $file.FullName -Value $updatedContent
        Write-Output "Updated float specifiers in $($file.Name)"
    }
}

Write-Output "Float specifier update complete!"
