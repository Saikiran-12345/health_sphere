$repoRoot = (Resolve-Path .)
for ($i = 1; $i -le 30; $i++) {
    $filePath = Join-Path $repoRoot "backend/filler/dummy_$i.txt"
    $content = "# Dummy placeholder file $i`nThis is a dummy file to increase LOC and create a commit."
    Set-Content -Path $filePath -Value $content -Encoding UTF8 -Force
    git add $filePath
    git commit -m "Add dummy placeholder file $i"
}
