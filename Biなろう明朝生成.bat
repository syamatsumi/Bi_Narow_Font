rem �ϐ��Ƀp�X��ݒ�
set FONTFORGE="C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe"
set SCR="bi_narow.py"

echo ���̂܂ܐi�߂��6�X���b�h����܂��B
pause
echo �{���Ɏ��s���܂����H
pause

rem start�R�}���h�ŕ�����s
start "" %FONTFORGE% %SCR% "M�~��R" "Bi�Ȃ낤����90-Regular" 0.9
start "" %FONTFORGE% %SCR% "M�~��R" "Bi�Ȃ낤����75-Regular" 0.75
start "" %FONTFORGE% %SCR% "M�~��R" "Bi�Ȃ낤����50-Regular" 0.5

start "" %FONTFORGE% %SCR% "M�~��B" "Bi�Ȃ낤����90-Bold" 0.9
start "" %FONTFORGE% %SCR% "M�~��B" "Bi�Ȃ낤����75-Bold" 0.75
start "" %FONTFORGE% %SCR% "M�~��B" "Bi�Ȃ낤����50-Bold" 0.5
