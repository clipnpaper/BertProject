@echo off
chcp 65001 > nul
echo ========================================================
echo  BERT 프로젝트 초기 설정 (가상환경 생성 및 패키지 설치)
echo ========================================================
echo.

:: 1. 파이썬 설치 확인
python --version > nul 2>&1
if errorlevel 1 (
    echo [오류] Python이 설치되어 있지 않거나 환경 변수(PATH)에 등록되지 않았습니다.
    echo Python 3.9 이상 버전을 설치할 때 "Add Python to PATH"에 체크해주세요.
    echo.
    pause
    exit /b
)

:: 2. 가상환경 생성
if not exist ".venv" (
    echo [1/3] 가상환경(.venv)을 생성하는 중입니다...
    python -m venv .venv
    if errorlevel 1 (
        echo [오류] 가상환경 생성에 실패했습니다.
        pause
        exit /b
    )
    echo [1/3] 가상환경 생성이 완료되었습니다.
) else (
    echo [1/3] 이미 .venv 가상환경이 존재합니다.
)

:: 3. 가상환경 활성화 및 pip 업그레이드
echo.
echo [2/3] pip를 최신 버전으로 업그레이드합니다...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip

:: 4. 필수 패키지 설치
echo.
echo [3/3] requirements.txt 패키지들을 설치하는 중입니다 (시간이 조금 걸릴 수 있습니다)...
pip install -r requirements.txt
if errorlevel 1 (
    echo [오류] 패키지 설치 중 오류가 발생했습니다.
    pause
    exit /b
)

echo.
echo ========================================================
echo  초기 설정이 완료되었습니다!
echo  
echo  1. Hugging Face 로그인이 필요하다면 아래 명령어를 입력하세요:
echo     hf auth login
echo     (또는 huggingface-cli login)
echo  
echo  2. 실행 명령어:
echo     python bert_test.py
echo ========================================================
echo.
pause
