@echo off
setlocal

set sz="C:\Program Files\7-Zip\7z.exe"
set input_dir=%~dp0
set output_dir=%~dp0
set options=-tzip -mx9
set versions=_v0.1.3.zip

%sz% a "%output_dir%BzNarowGothic%versions%" "%input_dir%\Bz�Ȃ낤�S�V�b�N\" %options%
%sz% a "%output_dir%BzNarowMincho%versions%" "%input_dir%\Bz�Ȃ낤����\" %options%

pause
