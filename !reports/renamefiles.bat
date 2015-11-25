for %%i in ("*.csv" or "*.txt") do (set fname=%%i) & call :rename
exit /b

:rename
ren "%fname%" "%fname:-2014.=.%"
exit /b