@echo off
chcp 65001 > nul
echo ========================================================
echo  BERT Test 실행 스크립트
echo ========================================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo [안내] 가상환경(.venv)이 아직 생성되지 않았습니다.
    echo 먼저 setup.bat을 실행하거나 README.md의 설치 가이드를 따라주세요.
    echo.
    pause
    exit /b
)

echo bert_test.py를 실행합니다...
echo.
.venv\Scripts\python.exe bert_test.py
echo.
echo ========================================================
echo  실행 완료
echo ========================================================
echo.
pause
