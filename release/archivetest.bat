@echo off
setlocal enabledelayedexpansion

set VERSIONS=_v0.2.4.zip

set SZIP="C:\Program Files\7-Zip\7z.exe"
set SCRIPT_DIR=%~dp0
set PKG_DIR=%~dp0\temp_pkg
set OUTPUT_DIR=%~dp0
set OPTIONS=-tzip -mx9
set UNITETTC=%SCRIPT_DIR%..\application\unitettc\unitettc64.exe
set SOURCE_DIR=%SCRIPT_DIR%..\processed
set TXT_DIR=%SCRIPT_DIR%\text


echo TTF�̎��W��TTC�̍쐬�ƃA�[�J�C�u�����{���܂��B
pause
echo ���s���܂����H
pause

set TTC_DIR=Bz�Ȃ낤����TTC
set TTC_DIRe=BzNarowMinchoTTC
set TARGET_NAMES=Bz�Ȃ낤���� Bz�Ȃ낤P���� Bz�Ȃ낤M����
REM �e�^�[�Q�b�g���t�H���_�Ɏ��߂�
for %%T in (%TARGET_NAMES%) do (
    set TARGET_NAME=%%T
    set DEST_DIR=%PKG_DIR%\%TTC_DIR%\!TARGET_NAME!
    echo �e�^�[�Q�b�g���t�H���_���쐬����
    if not exist !DEST_DIR! mkdir !DEST_DIR!
    pause
    rem ������t�H���_�Ƀ\�[�X�t�H���_����Ώۂ��R�s�[���Ă��� 
    for %%F in ("%SOURCE_DIR%\!TARGET_NAME!*.ttf") do copy "%%F" "!DEST_DIR!"
    pause
    rem �t�@�C�����X�g���������A�W�߂��t�@�C�������X�g���AUNITETTC�����s
    set FILE_LIST=
    for %%F in ("!DEST_DIR!\*.*") do set FILE_LIST=!FILE_LIST! "%%F"
    call %UNITETTC% !DEST_DIR!.ttc !FILE_LIST!
    pause

)
copy "%TXT_DIR%\OFLa.txt" "%TTC_DIR%\OFL.txt"
%SZIP% a "%OUTPUT_DIR%\%TTC_DIRe%%versions%" "%PKG_DIR%\%TTC_DIR%\" %OPTIONS%
echo ��������: %TTC_DIR%

pause
