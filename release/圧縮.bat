@echo off
setlocal

set sz="C:\Program Files\7-Zip\7z.exe"
set input_dir=%~dp0
set output_dir=%~dp0
set options=-tzip -mx9

%sz% a "%output_dir%Bz�Ȃ낤�S�V�b�N.zip" "%input_dir%\Bz�Ȃ낤�S�V�b�N\" %options%
%sz% a "%output_dir%Bz�Ȃ낤����.zip" "%input_dir%\Bz�Ȃ낤����\" %options%

pause
