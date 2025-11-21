# Python Logging Setup Snippet

Python 프로젝트에서 빠르게 로깅 설정을 구성할 수 있는 재사용 가능한 스니펫입니다.

## 특징

- YAML 기반 로깅 설정
- 콘솔, 파일, 에러 파일 핸들러 지원
- 로그 파일 자동 로테이션 (10MB, 최대 5개 백업)
- 로그 디렉토리 자동 생성
- 모듈별 로거 설정 지원

## 파일 구조

```
.
├── config/
│   ├── logging_config.py  # 로깅 설정 함수
│   └── logging.yaml       # 로깅 설정 파일
├── logs/                  # 로그 파일 저장 디렉토리 (자동 생성)
└── logging_main.py        # 사용 예제
```

## 필요한 패키지

```bash
pip install pyyaml
# uv add pyyaml
```

### 사용 예시

```python
import logging
from config.logging_config import setup_logging_yaml

logger = logging.getLogger(__name__)

def main():
    logger.info("Application started")

    try:
        # Your code here
        logger.debug("Processing data...")
        result = process_data()
        logger.info(f"Result: {result}")
    except Exception as e:
        logger.error(f"Error occurred: {e}", exc_info=True)

    logger.info("Application finished")

if __name__ == "__main__":
    setup_logging_yaml("config/logging.yaml")
    main()
```

## 설정 커스터마이징

### logging.yaml 수정

#### 로그 레벨 변경

```yaml
loggers:
  "":
    level: DEBUG # INFO, WARNING, ERROR, CRITICAL
    handlers: [console, file, error_file]
```

#### 로그 파일 경로 변경

```yaml
handlers:
  file:
    filename: logs/app.log # 원하는 경로로 변경
```

#### 로그 포맷 변경

```yaml
formatters:
  standard:
    format: "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    datefmt: "%Y-%m-%d %H:%M:%S"
```

#### 파일 로테이션 설정 변경

```yaml
handlers:
  file:
    maxBytes: 10485760 # 10MB (바이트 단위)
    backupCount: 5 # 백업 파일 개수
```

### 모듈별 로거 설정

특정 모듈에 대해 다른 로깅 레벨을 설정할 수 있습니다:

```yaml
loggers:
  myapp.module1:
    level: DEBUG
    handlers: [console, file]
    propagate: false

  myapp.module2:
    level: WARNING
    handlers: [error_file]
    propagate: false
```

## 로그 출력 예시

### 콘솔 출력

```
2024-01-15 10:30:45 [INFO] __main__: Application started
2024-01-15 10:30:46 [DEBUG] myapp.module: Processing data
2024-01-15 10:30:47 [INFO] __main__: Application finished
```

### 파일 출력 (logs/app.log)

```
2024-01-15 10:30:45 [INFO] __main__.main:15 - Application started
2024-01-15 10:30:46 [DEBUG] myapp.module.process:42 - Processing data
2024-01-15 10:30:47 [INFO] __main__.main:25 - Application finished
```

## 라이센스

MIT License

## 기여

이슈나 개선 사항이 있으시면 편하게 PR을 보내주세요!
