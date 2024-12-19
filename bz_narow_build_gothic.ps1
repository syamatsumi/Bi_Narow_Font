pause
# ���s����R�}���h�̃��X�g
$commands = @(
"M�S�VB Bz�Ȃ낤M�S�V�b�N20-Bold 0.2",
"M�S�VR Bz�Ȃ낤M�S�V�b�N20-Regular 0.2",
"M�S�VB Bz�Ȃ낤M�S�V�b�N30-Bold 0.3",
"M�S�VR Bz�Ȃ낤M�S�V�b�N30-Regular 0.3",
"M�S�VB Bz�Ȃ낤M�S�V�b�N40-Bold 0.4",
"M�S�VR Bz�Ȃ낤M�S�V�b�N40-Regular 0.4",
"M�S�VB Bz�Ȃ낤M�S�V�b�N50-Bold 0.5",
"M�S�VR Bz�Ȃ낤M�S�V�b�N50-Regular 0.5",
"M�S�VB Bz�Ȃ낤M�S�V�b�N60-Bold 0.6",
"M�S�VR Bz�Ȃ낤M�S�V�b�N60-Regular 0.6",
"M�S�VB Bz�Ȃ낤M�S�V�b�N70-Bold 0.7",
"M�S�VR Bz�Ȃ낤M�S�V�b�N70-Regular 0.7",
"M�S�VB Bz�Ȃ낤M�S�V�b�N80-Bold 0.8",
"M�S�VR Bz�Ȃ낤M�S�V�b�N80-Regular 0.8",
"M�S�VB Bz�Ȃ낤M�S�V�b�N90-Bold 0.9",
"M�S�VR Bz�Ȃ낤M�S�V�b�N90-Regular 0.9",
"P�S�VB Bz�Ȃ낤P�S�V�b�N20-Bold 0.2",
"P�S�VR Bz�Ȃ낤P�S�V�b�N20-Regular 0.2",
"P�S�VB Bz�Ȃ낤P�S�V�b�N30-Bold 0.3",
"P�S�VR Bz�Ȃ낤P�S�V�b�N30-Regular 0.3",
"P�S�VB Bz�Ȃ낤P�S�V�b�N40-Bold 0.4",
"P�S�VR Bz�Ȃ낤P�S�V�b�N40-Regular 0.4",
"P�S�VB Bz�Ȃ낤P�S�V�b�N50-Bold 0.5",
"P�S�VR Bz�Ȃ낤P�S�V�b�N50-Regular 0.5",
"P�S�VB Bz�Ȃ낤P�S�V�b�N60-Bold 0.6",
"P�S�VR Bz�Ȃ낤P�S�V�b�N60-Regular 0.6",
"P�S�VB Bz�Ȃ낤P�S�V�b�N70-Bold 0.7",
"P�S�VR Bz�Ȃ낤P�S�V�b�N70-Regular 0.7",
"P�S�VB Bz�Ȃ낤P�S�V�b�N80-Bold 0.8",
"P�S�VR Bz�Ȃ낤P�S�V�b�N80-Regular 0.8",
"P�S�VB Bz�Ȃ낤P�S�V�b�N90-Bold 0.9",
"P�S�VR Bz�Ȃ낤P�S�V�b�N90-Regular 0.9",
"�S�VB Bz�Ȃ낤�S�V�b�N40-Bold 0.4",
"�S�VR Bz�Ȃ낤�S�V�b�N40-Regular 0.4",
"�S�VB Bz�Ȃ낤�S�V�b�N50-Bold 0.5",
"�S�VR Bz�Ȃ낤�S�V�b�N50-Regular 0.5",
"�S�VB Bz�Ȃ낤�S�V�b�N60-Bold 0.6",
"�S�VR Bz�Ȃ낤�S�V�b�N60-Regular 0.6",
"�S�VB Bz�Ȃ낤�S�V�b�N70-Bold 0.7",
"�S�VR Bz�Ȃ낤�S�V�b�N70-Regular 0.7",
"�S�VB Bz�Ȃ낤�S�V�b�N80-Bold 0.8",
"�S�VR Bz�Ȃ낤�S�V�b�N80-Regular 0.8",
"�S�VB Bz�Ȃ낤�S�V�b�N90-Bold 0.9",
"�S�VR Bz�Ȃ낤�S�V�b�N90-Regular 0.9"
)

# ���s�t�@�C��
$scriptname = "bz_narow_core"

# �g���q��ǉ����ăt�@�C�������쐬
$scriptfullname = "{0}.py" -f $scriptname
$iniFile = "{0}.ini" -f $scriptname

# �ő哯�����s��
$maxParallel = 7

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

    $config = @{}
    Get-Content $iniFile | ForEach-Object {
        if ($_ -match '^([^#;]+)=(.+)$') {
            $key = $matches[1].Trim()
            $value = $matches[2].Trim()
            $config[$key] = $value
    }   }
    $ffpy = $($config['ffpy'])
    $build_dir = $($config['Build_Fonts_Dir'])

    # �t�H���_�����݂��Ȃ��ꍇ�͍쐬����
    if (-not (Test-Path -Path $build_dir)) {
        New-Item -Path $build_dir -ItemType Directory | Out-Null
        Write-Host "Created directory: $build_dir"
    }

    # �R�}���h�����s
    $CommandLine = @($scriptfullname) + $args
    Write-Host "Executing: $ffpy $scriptfullname $args"
    $logFile = "$build_dir\$($args[1])_stdout.err"  # ����3�𒊏o���ă��O�t�@�C�����𐶐�
    try {
        $process = Start-Process -FilePath $ffpy `
            -ArgumentList $CommandLine `
            -RedirectStandardError $logFile `
            -NoNewWindow `
            -PassThru `
            -ErrorAction 'Continue'
        $runningJobs += $process
    }
    catch {
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

pause