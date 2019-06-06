@ECHO OFF
:BEGIN
CLS
ECHO Enter Commit Message
ECHO.
SET /P COMMITMESSAGE=message: 

git add .
git commit -m "%COMMITMESSAGE%"
git push

pause