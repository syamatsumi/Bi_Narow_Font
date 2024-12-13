$iniFile = "bz_narow.ini"
$config = @{}
Get-Content $iniFile | ForEach-Object {
    if ($_ -match '^([^#;]+)=(.+)$') {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim()
        $config[$key] = $value
}   }
$scr = "z_narow.py"
$ffpy = $($config['ffpy'])
$ffscr = $($config['ffscr'])


& $ffpy $scr M�~��B test 0.3 uni3085
#& $ffpy $scr P�S�VB Bz�Ȃ낤P�S�V�b�N30-Bold 0.3
#& $ffpy $scr P�~��R Bz�Ȃ낤P����30-Regular 0.3
#& $ffpy $scr P�~��B Bz�Ȃ낤P����30-Bold 0.3