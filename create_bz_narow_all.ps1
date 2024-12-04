# FontForge�����s
$fontforge = "C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe"

# ���s����R�}���h�̃��X�g
$commands = @(
    "bz_narow.py M�S�VR Bz�Ȃ낤�S�V�b�N90-Regular 0.9",
    "bz_narow.py M�S�VR Bz�Ȃ낤�S�V�b�N75-Regular 0.75",
    "bz_narow.py M�S�VR Bz�Ȃ낤�S�V�b�N50-Regular 0.5",
    "bz_narow.py M�S�VB Bz�Ȃ낤�S�V�b�N90-Bold 0.9",
    "bz_narow.py M�S�VB Bz�Ȃ낤�S�V�b�N75-Bold 0.75",
    "bz_narow.py M�S�VB Bz�Ȃ낤�S�V�b�N50-Bold 0.5",
    "bz_narow.py P�S�VR Bz�Ȃ낤P�S�V�b�N90-Regular 0.9",
    "bz_narow.py P�S�VR Bz�Ȃ낤P�S�V�b�N75-Regular 0.75",
    "bz_narow.py P�S�VR Bz�Ȃ낤P�S�V�b�N50-Regular 0.5",
    "bz_narow.py P�S�VB Bz�Ȃ낤P�S�V�b�N90-Bold 0.9",
    "bz_narow.py P�S�VB Bz�Ȃ낤P�S�V�b�N75-Bold 0.75",
    "bz_narow.py P�S�VB Bz�Ȃ낤P�S�V�b�N50-Bold 0.5",
    "bz_narow.py M�~��R Bz�Ȃ낤����90-Regular 0.9",
    "bz_narow.py M�~��R Bz�Ȃ낤����75-Regular 0.75",
    "bz_narow.py M�~��R Bz�Ȃ낤����50-Regular 0.5",
    "bz_narow.py M�~��B Bz�Ȃ낤����90-Bold 0.9",
    "bz_narow.py M�~��B Bz�Ȃ낤����75-Bold 0.75",
    "bz_narow.py M�~��B Bz�Ȃ낤����50-Bold 0.5",
    "bz_narow.py P�~��R Bz�Ȃ낤P����90-Regular 0.9",
    "bz_narow.py P�~��R Bz�Ȃ낤P����75-Regular 0.75",
    "bz_narow.py P�~��R Bz�Ȃ낤P����50-Regular 0.5",
    "bz_narow.py P�~��B Bz�Ȃ낤P����90-Bold 0.9",
    "bz_narow.py P�~��B Bz�Ȃ낤P����75-Bold 0.75",
    "bz_narow.py P�~��B Bz�Ȃ낤P����50-Bold 0.5"
)

# �ő哯�����s��
$maxParallel = 8

# ���s���̃v���Z�X���Ǘ�
$runningJobs = @()

foreach ($command in $commands) {
    # ���s���v���Z�X�������𒴂���Ȃ�ҋ@
    while ($runningJobs.Count -ge $maxParallel) {
        Start-Sleep -Seconds 3
        # ���s���̃v���Z�X�̂ݕێ�
        $runningJobs = $runningJobs | Where-Object { $_ -ne $null -and $_.HasExited -eq $false }
    }

    # �R�}���h�𕪊�
    $args = $command -split " "
    if ($args.Count -eq 0) {
        Write-Warning "�����ȃR�}���h: $command"
        continue
    }

    # �R�}���h�����s
    Write-Host "Executing: $fontforge $args"
    try {
        $process = Start-Process -FilePath $fontforge -ArgumentList $args -NoNewWindow -PassThru -ErrorAction 'Continue'
        $runningJobs += $process
    } catch {
        Write-Warning "Start-Process �Ɏ��s: $_"
        Write-Host "�G���[�ڍ�: $($_.Exception.Message)"
    }
}

# �v���Z�X�̏I����҂�
$runningJobs | ForEach-Object {
    try {
        if ($_ -ne $null -and $_.HasExited -eq $false) {
            $_.WaitForExit()
        }
    } catch {
        Write-Warning "�v���Z�XID $($_.Id) �̏I���ҋ@���ɃG���[���������܂���: $_"
        Write-Host "�G���[�ڍ�: $($_.Exception.Message)"
    }
}
