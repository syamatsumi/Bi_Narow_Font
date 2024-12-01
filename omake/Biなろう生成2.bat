@echo off
setlocal

rem FontForge��Python���p�X
set FONTFORGE="C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe"
set SCR="bi_narow.py"

rem �X���b�h���𐧌�
set MAX_THREADS=6

rem ���s�^�X�N�̐ݒ�
set TASKS_LIST="
set TASKS_LIST=%TASKS_LIST% "M�S�VR" "Bi�Ȃ낤�S�V�b�N-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "M�S�VR" "Bi�Ȃ낤�S�V�b�N-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "M�S�VR" "Bi�Ȃ낤�S�V�b�N-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "M�S�VB" "Bi�Ȃ낤�S�V�b�N-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "M�S�VB" "Bi�Ȃ낤�S�V�b�N-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "M�S�VB" "Bi�Ȃ낤�S�V�b�N-Bold" 0.5

set TASKS_LIST=%TASKS_LIST% "P�S�VR" "Bi�Ȃ낤P�S�V�b�N-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "P�S�VR" "Bi�Ȃ낤P�S�V�b�N-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "P�S�VR" "Bi�Ȃ낤P�S�V�b�N-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "P�S�VB" "Bi�Ȃ낤P�S�V�b�N-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "P�S�VB" "Bi�Ȃ낤P�S�V�b�N-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "P�S�VB" "Bi�Ȃ낤P�S�V�b�N-Bold" 0.5

set TASKS_LIST=%TASKS_LIST% "M�~��R" "Bi�Ȃ낤����-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "M�~��R" "Bi�Ȃ낤����-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "M�~��R" "Bi�Ȃ낤����-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "M�~��B" "Bi�Ȃ낤����-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "M�~��B" "Bi�Ȃ낤����-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "M�~��B" "Bi�Ȃ낤����-Bold" 0.5

set TASKS_LIST=%TASKS_LIST% "P�~��R" "Bi�Ȃ낤P����-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "P�~��R" "Bi�Ȃ낤P����-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "P�~��R" "Bi�Ȃ낤P����-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "P�~��B" "Bi�Ȃ낤P����-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "P�~��B" "Bi�Ȃ낤P����-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "P�~��B" "Bi�Ȃ낤P����-Bold" 0.5
"

rem �^�X�N���s���[�v
for /f "tokens=1,2,3 delims= " %%A in (%TASKS_LIST%) do (
    rem ���s���̃X���b�h�����擾
    call :CheckThreads

    rem �^�X�N���J�n
    echo Starting task: %%A %%B %%C
    start "" %FONTFORGE% %SCR% %%A %%B %%C
)

rem �c��̃^�X�N�̊����ҋ@
call :WaitForCompletion
exit /b

:CheckThreads
:WaitForCompletion
    rem ���s���̃W���u�����`�F�b�N
    for /f "tokens=*" %%N in ('tasklist /FI "IMAGENAME eq ffpython.exe" /FI "STATUS eq RUNNING" ^| find /C /I "ffpython.exe"') do (
        if %%N geq %MAX_THREADS% (
            timeout /t 1 >nul
            goto :CheckThreads
        )
    )

pause
