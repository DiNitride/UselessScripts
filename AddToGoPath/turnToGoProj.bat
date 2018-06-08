@echo off

set MYDIR=%1
for %%f in (%MYDIR%) do set myfolder=%%~nxf


mklink /J "%GOPATH%\src\%myfolder%" %1