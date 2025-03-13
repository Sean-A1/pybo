# Python 공식 이미지 사용 (3.12 버전)
FROM python:3.12-slim

# 작업 디렉터리 설정
WORKDIR /app

# 시스템 종속성 설치 (PostgreSQL용 패키지 포함)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 후 Python 의존성 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 프로젝트 파일 복사
COPY . /app/

# Django의 static 파일 수집 (운영환경에서 필요)
RUN python manage.py collectstatic --noinput

# 컨테이너 외부에 노출될 포트 지정 (Gunicorn 기본 포트 8000)
EXPOSE 8000

# 컨테이너 실행 명령어 (Gunicorn을 통한 실행)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]

# 참고:
# 만약 개발환경에서 실행할 경우:
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Gunicorn을 사용하려면 requirements.txt에 추가 (없다면 추가)
# gunicorn==23.0.0

# 주의 사항:
# collectstatic을 위해 settings.py에서 STATIC_ROOT 설정 필수 (운영환경)
# settings.py 예시:
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# 운영환경과 로컬 환경의 구분은 Dockerfile에서 하지 않고, Docker 실행 시 settings 환경변수(DJANGO_SETTINGS_MODULE)를 다르게 설정하여 구분
