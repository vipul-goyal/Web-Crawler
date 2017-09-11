@ echo off
cls
:start1
python "DE_Websites.py"
python "NLP.py"
python "OnlineDB_DI.py"
python "OnlineDB_DE.py"
start http://localhost/mobdb2.php
timeout /t 900 /nobreak
goto start1
pause