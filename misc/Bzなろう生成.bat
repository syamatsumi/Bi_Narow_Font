@echo off
setlocal

rem FontForgeのPython環境パス
set FONTFORGE="C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe"
set SCR="bz_narow.py"

rem スレッド数を制限
set MAX_THREADS=6

rem 実行タスクの設定
set TASKS_LIST="
set TASKS_LIST=%TASKS_LIST% "MゴシR" "Bzなろうゴシック-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "MゴシR" "Bzなろうゴシック-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "MゴシR" "Bzなろうゴシック-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "MゴシB" "Bzなろうゴシック-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "MゴシB" "Bzなろうゴシック-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "MゴシB" "Bzなろうゴシック-Bold" 0.5

set TASKS_LIST=%TASKS_LIST% "PゴシR" "BzなろうPゴシック-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "PゴシR" "BzなろうPゴシック-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "PゴシR" "BzなろうPゴシック-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "PゴシB" "BzなろうPゴシック-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "PゴシB" "BzなろうPゴシック-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "PゴシB" "BzなろうPゴシック-Bold" 0.5

set TASKS_LIST=%TASKS_LIST% "MミンR" "Bzなろう明朝-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "MミンR" "Bzなろう明朝-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "MミンR" "Bzなろう明朝-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "MミンB" "Bzなろう明朝-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "MミンB" "Bzなろう明朝-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "MミンB" "Bzなろう明朝-Bold" 0.5

set TASKS_LIST=%TASKS_LIST% "PミンR" "BzなろうP明朝-Regular" 0.9
set TASKS_LIST=%TASKS_LIST% "PミンR" "BzなろうP明朝-Regular" 0.75
set TASKS_LIST=%TASKS_LIST% "PミンR" "BzなろうP明朝-Regular" 0.5

set TASKS_LIST=%TASKS_LIST% "PミンB" "BzなろうP明朝-Bold" 0.9
set TASKS_LIST=%TASKS_LIST% "PミンB" "BzなろうP明朝-Bold" 0.75
set TASKS_LIST=%TASKS_LIST% "PミンB" "BzなろうP明朝-Bold" 0.5
"

rem タスク実行ループ
for /f "tokens=1,2,3 delims= " %%A in (%TASKS_LIST%) do (
    rem 実行中のスレッド数を取得
    call :CheckThreads

    rem タスクを開始
    echo Starting task: %%A %%B %%C
    start "" %FONTFORGE% %SCR% %%A %%B %%C
)

rem 残りのタスクの完了待機
call :WaitForCompletion
exit /b

:CheckThreads
:WaitForCompletion
    rem 実行中のジョブ数をチェック
    for /f "tokens=*" %%N in ('tasklist /FI "IMAGENAME eq ffpython.exe" /FI "STATUS eq RUNNING" ^| find /C /I "ffpython.exe"') do (
        if %%N geq %MAX_THREADS% (
            timeout /t 1 >nul
            goto :CheckThreads
        )
    )

pause
