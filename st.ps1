param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$File
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) { $python = "python" }

if (-not [IO.Path]::IsPathRooted($File)) {
    $candidate = Join-Path (Get-Location) $File
    if (Test-Path $candidate) {
        $File = (Resolve-Path $candidate).Path
    } else {
        $name = $File
        if (-not $name.EndsWith(".py")) { $name += ".py" }
        $hits = @(Get-ChildItem -Path (Join-Path $root "src") -Recurse -Filter $name -File)
        if ($hits.Count -eq 0) {
            Write-Error "파일을 찾지 못했습니다: $name"
            exit 1
        }
        if ($hits.Count -gt 1) {
            $hits | ForEach-Object { $_.FullName }
            Write-Error "같은 이름이 여러 개입니다. 경로를 지정하세요."
            exit 1
        }
        $File = $hits[0].FullName
    }
}

$port = 8501
while (Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue) {
    $port++
    if ($port -gt 8510) {
        Write-Error "8501부터 8510까지 빈 포트가 없습니다."
        exit 1
    }
}

Write-Host "http://localhost:$port"
Write-Host $File
& $python -m streamlit run $File --server.port $port
