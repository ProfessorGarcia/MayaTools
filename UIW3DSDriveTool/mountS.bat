@echo off
set "TARGET_DIR=%~dp0"
set "TARGET_DIR=%TARGET_DIR:~0,-1%"
subst S: /d
subst S: "%TARGET_DIR%"
echo S: drive now mapped to: %TARGET_DIR%
pause