# 🚀 BERT Model & Tokenizer Test Project

이 저장소는 Hugging Face의 사전 학습된 BERT 모델(`bert-base-uncased`)과 토크나이저를 다운로드하여 텍스트 토큰화 동작을 테스트하는 기본 프로젝트입니다.

동료들이 Python 및 Hugging Face 환경을 처음 접하더라도, 아래 단계를 차례대로 따라 하면 쉽게 환경을 구축하고 테스트할 수 있습니다.

---

## 📋 목차
1. [사전 준비 (Prerequisites)](#-1-사전-준비-prerequisites)
2. [설치 및 실행 가이드 (Windows CMD 기준)](#-2-설치-및-실행-가이드-windows-cmd-기준)
3. [간편 실행 방법 (배치 파일 활용)](#-3-간편-실행-방법-배치-파일-활용)
4. [정상 실행 결과 예시](#-4-정상-실행-결과-예시)
5. [자주 묻는 질문 및 문제 해결 (FAQ & Troubleshooting)](#-5-자주-묻는-질문-및-문제-해결-faq--troubleshooting)

---

## 🛠 1. 사전 준비 (Prerequisites)

### 1-1. Python 설치 확인
컴퓨터에 Python(3.9 ~ 3.12 권장)이 설치되어 있어야 합니다.
- **설치 확인**: `Win + R` 키를 누르고 `cmd`를 입력하여 명령 프롬프트를 연 뒤 아래 명령어를 입력합니다.
  ```cmd
  python --version
  ```
- **설치되어 있지 않은 경우**:
  1. [Python 공식 다운로드 페이지](https://www.python.org/downloads/)에서 설치 파일을 다운로드합니다.
  2. 설치 시 **반드시 첫 화면 하단의 `Add python.exe to PATH` (또는 `Add Python to PATH`)에 체크**한 후 `Install Now`를 눌러주세요. (체크하지 않으면 cmd에서 python 명령어를 인식하지 못합니다.)

### 1-2. Hugging Face 계정 생성 및 Access Token 발급
Hugging Face의 모델을 안전하게 다운로드하고 인증하기 위해 개인 액세스 토큰(Token)이 필요합니다.

1. [Hugging Face 공식 홈페이지](https://huggingface.co/join)에서 회원가입 및 이메일 인증을 완료합니다.
2. [Hugging Face Access Tokens 페이지](https://huggingface.co/settings/tokens)로 이동합니다.
3. 우측 상단의 **`Create new token`** (또는 `New token`) 버튼을 클릭합니다.
4. 설정 항목을 입력합니다:
   - **Token type**: `Read` 선택 (다운로드 및 테스트용)
   - **Token name**: 원하는 이름 입력 (예: `my-bert-token`)
5. 하단의 **`Create token`** 버튼을 누릅니다.
6. 생성된 토큰(`hf_`로 시작하는 문자열) 옆의 **복사 아이콘(Copy)**을 눌러 안전한 곳에 복사해 둡니다.

---

## 💻 2. 설치 및 실행 가이드 (Windows CMD 기준)

### [Step 1] 프로젝트 폴더 열기 (명령 프롬프트)
1. `Win + R` 키를 누르고 `cmd`를 입력한 뒤 Enter를 누릅니다.
2. 다운로드받은 프로젝트 폴더로 이동합니다. (예: `c:\Users\user\BertProject`)
   ```cmd
   cd c:\Users\user\BertProject
   ```
   *(탐색기에서 프로젝트 폴더 경로를 복사하여 `cd 붙여넣기` 하시면 편리합니다.)*

---

### [Step 2] 가상환경(venv) 생성 및 활성화
독립된 실행 환경을 만들기 위해 가상환경을 생성하고 켭니다.

1. 가상환경 폴더(`.venv`) 생성:
   ```cmd
   python -m venv .venv
   ```
2. 가상환경 활성화:
   ```cmd
   .venv\Scripts\activate
   ```
   > ✅ **성공 확인**: 명령어 줄 맨 앞에 `(.venv)` 표시가 붙었다면 정상적으로 활성화된 것입니다.

---

### [Step 3] 필수 패키지 라이브러리 설치
프로젝트에 필요한 `torch`, `transformers`, `huggingface_hub` 라이브러리를 설치합니다.

```cmd
pip install -r requirements.txt
```
*(PyTorch 등 모델 구동 패키지 다운로드로 인해 최초 1회 실행 시 1~3분 정도 소요될 수 있습니다.)*

---

### [Step 4] Hugging Face CLI 로그인 (인증)
안전한 모델 다운로드를 위해 앞서 발급받은 Hugging Face 토큰으로 로그인합니다.

```cmd
hf auth login
```
*(만약 위 명령어가 인식되지 않을 경우 `huggingface-cli login`을 입력하세요.)*

1. `Token:` 이라는 메시지가 나타나면, 아까 복사해 둔 **토큰(`hf_...`)을 붙여넣고 Enter**를 누릅니다.
   > ⚠️ **주의 (중요!)**: 비밀번호 보안 특성상 토큰을 붙여넣어도 **화면에 글자가 보이지 않습니다**. 멈춘 것이 아니므로 `Ctrl + V` (또는 마우스 우클릭)로 붙여넣은 뒤 바로 `Enter`를 누르시면 됩니다.
2. `Add token as git credential? (Y/n)` 질문이 나오면 `n`을 입력하고 Enter를 누릅니다.
3. `Token is valid (permission: read)` 및 `Login successful` 메시지가 나오면 인증 완료입니다.

---

### [Step 5] 테스트 코드 실행
이제 모든 준비가 끝났습니다! 아래 명령어로 BERT 테스트 코드를 실행합니다.

```cmd
python bert_test.py
```

---

## ⚡ 3. 간편 실행 방법 (배치 파일 활용)

명령어 입력이 번거로운 경우, 제공된 배치(`.bat`) 파일을 더블 클릭하여 진행할 수도 있습니다.

1. **`setup.bat` 더블 클릭**: 가상환경 생성 및 필수 라이브러리 자동 설치
2. **`cmd`에서 `hf auth login` 실행**: 최초 1회 Hugging Face 토큰 인증
3. **`run.bat` 더블 클릭**: `bert_test.py` 스크립트 즉시 실행

---

## 📊 4. 정상 실행 결과 예시

`python bert_test.py` 실행 시 아래와 같이 텐서(Tensor) 형태의 인풋 데이터와 분절된 토큰 리스트가 출력되면 정상 동작한 것입니다:

```text
{'input_ids': tensor([[ 101, 1045, 2293, 3000,  102]]), 'token_type_ids': tensor([[0, 0, 0, 0, 0]]), 'attention_mask': tensor([[1, 1, 1, 1, 1]])}
['[CLS]', 'i', 'love', 'paris', '[SEP]']
```

- `[CLS]`: 문장의 시작을 알리는 특수 토큰
- `[SEP]`: 문장의 끝(구분)을 알리는 특수 토큰
- `1045`, `2293`, `3000`: 각 단어(`i`, `love`, `paris`)에 대응하는 BERT 사전 인덱스 번호

---

## ❓ 5. 자주 묻는 질문 및 문제 해결 (FAQ & Troubleshooting)

### Q1. `'python'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.` 에러가 떠요.
- **원인**: Python이 설치되지 않았거나 설치 시 환경 변수(PATH)에 등록되지 않았습니다.
- **해결**: Python 재설치 프로그램을 실행한 후 `Modify` 또는 설치 첫 화면에서 **`Add Python to PATH`**를 반드시 체크하고 설치를 완료하세요. 그 후 열려있는 cmd 창을 닫고 다시 열어야 적용됩니다.

### Q2. `hf auth login` 시 토큰을 붙여넣었는데 아무 글자도 안 적혀요.
- **원인**: 보안상 비밀번호/토큰을 터미널에 노출하지 않기 위해 키 입력을 숨기는 정상 동작입니다.
- **해결**: 복사한 토큰(`hf_...`)을 `Ctrl + V` 또는 마우스 우클릭으로 붙여넣은 후 바로 **`Enter`**를 누르시면 정상 인식됩니다.

### Q3. `.venv\Scripts\activate` 실행 시 오류가 발생해요.
- PowerShell 환경에서 권한 오류(`이 시스템에서 스크립트를 실행할 수 없으므로...`)가 발생한 경우, **명령 프롬프트(`cmd.exe`)**를 사용하시거나 PowerShell 관리자 모드에서 `Set-ExecutionPolicy RemoteSigned`를 입력해 주세요. (가장 쉬운 방법은 일반 `cmd`를 사용하는 것입니다.)

### Q4. 모델 다운로드 시 시간이 오래 걸리거나 인터넷 오류가 발생해요.
- 최초 실행 시 약 400MB 상당의 BERT 사전 학습 가중치가 Hugging Face 서버에서 자동으로 다운로드됩니다. 네트워크 연결 상태를 확인하시고 잠시 기다려주세요. 다운로드가 완료되면 다음 실행부터는 로컬 캐시에서 즉시 불러옵니다.
