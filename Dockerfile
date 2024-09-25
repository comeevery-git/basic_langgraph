# 베이스 이미지 설정
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# Poetry 설치
RUN pip install poetry

# 의존성 파일 복사 및 설치
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

# 전체 애플리케이션 코드 복사
COPY . .

# Python 패키지 경로 설정
ENV PYTHONPATH=/app

# FastAPI 서버 실행
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
