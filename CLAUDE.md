# safe-pay-agent

블록체인(Base Sepolia)과 AI 에이전트를 학습하기 위한 토이 프로젝트. 진행 방법은 `docs/WORKFLOW.md`(로컬 전용, 커밋하지 않음)를 따른다.

## 안전 규칙 (예외 없음)

- `.env`는 절대 읽거나 출력하지 않는다. 개인키를 출력하는 코드도 쓰지 않는다.
- 테스트넷(Base Sepolia, chain_id 84532)만 쓴다. 메인넷 RPC 주소를 코드에 넣지 않는다.

## 역할 나누기

- git 커밋과 푸시는 사용자가 직접 한다. Claude는 파일을 만들거나 고친 뒤 커밋 명령과 메시지 초안만 제시하고, 사용자가 커밋하면 검토한다.
- 저장소 설정(머지 방식 등)은 강제로 바꾸지 않는다.
- `notes/` 노트는 사용자가 직접 쓴다. Claude는 검토만 한다.
- `safe_pay/sender.py`의 `check_policy`는 사용자가 직접 쓴다.

## 규칙

- 브랜치 이름: `m1/reader`처럼 `마일스톤/짧은-설명`
- 커밋 메시지와 PR 제목: Conventional Commits 접두어는 영어, 제목과 본문은 한국어 (예: `feat(reader): 트랜잭션 요약 함수 추가`)
- 실행: `.venv\Scripts\python`, 한글 출력이 깨지면 `PYTHONUTF8=1`
- web3 8.x 기준으로 문서를 본다.
