rem �ϐ��Ƀp�X��ݒ�
set FONTFORGE="C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe"
set SCR="bi_narow.py"

echo ���̂܂ܐi�߂��6�X���b�h����܂��B
pause
echo �{���Ɏ��s���܂����H
pause

rem start�R�}���h�ŕ�����s
start "" %FONTFORGE% %SCR% "M�S�VR" "Bi�Ȃ낤�S�V�b�N90-Regular" 0.9
start "" %FONTFORGE% %SCR% "M�S�VR" "Bi�Ȃ낤�S�V�b�N75-Regular" 0.75
start "" %FONTFORGE% %SCR% "M�S�VR" "Bi�Ȃ낤�S�V�b�N50-Regular" 0.5

start "" %FONTFORGE% %SCR% "M�S�VB" "Bi�Ȃ낤�S�V�b�N90-Bold" 0.9
start "" %FONTFORGE% %SCR% "M�S�VB" "Bi�Ȃ낤�S�V�b�N75-Bold" 0.75
start "" %FONTFORGE% %SCR% "M�S�VB" "Bi�Ȃ낤�S�V�b�N50-Bold" 0.5
