$files = @(
    @{ Path = 'backend/filler/large_file_01.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_02.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_03.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_04.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_05.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_06.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_07.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_08.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_09.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'backend/filler/large_file_10.py'; Lines = 30000; Content = '# dummy python line' },
    @{ Path = 'frontend/filler/large_component_01.tsx'; Lines = 20000; Content = '// dummy TSX line' },
    @{ Path = 'frontend/filler/large_component_02.tsx'; Lines = 20000; Content = '// dummy TSX line' },
    @{ Path = 'frontend/filler/large_component_03.tsx'; Lines = 20000; Content = '// dummy TSX line' },
    @{ Path = 'frontend/filler/large_component_04.tsx'; Lines = 20000; Content = '// dummy TSX line' },
    @{ Path = 'frontend/filler/large_component_05.tsx'; Lines = 20000; Content = '// dummy TSX line' }
)

foreach ($file in $files) {
    $fullPath = Join-Path -Path (Resolve-Path .) -ChildPath $file.Path
    $dir = Split-Path $fullPath -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    Write-Host "Generating $($file.Lines) lines for $($file.Path)"
    $content = ($file.Content + "`n") * $file.Lines
    Set-Content -Path $fullPath -Value $content -Encoding UTF8 -Force
}
