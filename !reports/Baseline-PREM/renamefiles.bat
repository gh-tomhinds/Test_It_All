for %%i in ("*.csv") do (set fname=%%i) & call :rename
goto :eof
:rename
::Cuts off 1st four chars, then appends prefix
ren "%fname%" "%fname:~5%"
goto :eof