# Python Pre-commit Setup Snippet

Python 프로젝트에서 코드 품질을 커밋 전에 자동으로 관리할 수 있는 pre-commit 설정입니다.

## 특징

- Git 커밋 전 자동 코드 검사 및 포맷팅
- Ruff를 사용한 빠른 린팅 및 포맷팅 (Black, isort, flake8 대체)
- 기본적인 파일 검사 (trailing whitespace, EOF, 문법 검사 등)
- YAML, JSON, TOML 파일 문법 검사
- Python AST 검증

## 필요한 패키지

```bash
pip install pre-commit
# uv add pre-commit
```

### 설치 및 사용 방법

1. 설정 파일 복사

- 프로젝트 루트 디렉토리에 `.pre-commit-config.yaml` 파일을 복사합니다.

2. pre-commit 훅 설치

```bash
pre-commit install
# uv run pre-commit install
```

3. 사용 방법

- 자동 실행(권장)
  - Pre-commit 훅이 설치 되어 있으면 `git commit` 시 자동으로 실행됩니다.
- 수동 실행
  - 모든 파일에 대해 실행

  ```bash
  pre-commit run --all-files
  # uv run pre-commit run all-files
  ```

  - 스테이징된 파일만 실행

  ```bash
  pre-commit run
  uv run pre-commit run
  ```

  - 특정 훅만 실행

  ```bash
  # Ruff 린터만 실행
  pre-commit run ruff-check --all-files
  uv run pre-commit run ruff-check --all-files

  # Ruff 포맷터만 실행
  pre-commit run ruff-format --all-files
  uv run pre-commit run ruff-format --all-files

  # trailing whitespace만 검사
  pre-commit run trailing-whitespace --all-files
  uv run pre-commit run trailing-whitespace --all-files
  ```

  - pre-commit 훅의 버전을 최신으로 업데이트

  ```bash
  pre-commit autoupdate
  ```

### 실행 예시

```bash
$ git commit -m "Add new feature"
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check python ast.........................................................Passed
Check Yaml...............................................................Passed
Check JSON...............................................................Passed
Check Toml...............................................................Passed
ruff-check...............................................................Passed
ruff-format..............................................................Passed
[main abc1234] Add new feature
 2 files changed, 10 insertions(+), 2 deletions(-)
```

## 라이센스

MIT License

## 기여

이슈나 개선 사항이 있으시면 편하게 PR을 보내주세요!
