# 베이스 이미지로 Python 3.11 사용
FROM python:3.11-slim

# 작업 디렉터리 설정. 컨테이너 안의 어느 경로에서 작업을 진행할지 결정
WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 프로젝트의 요구사항 파일을 복사하고 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트의 모든 파일을 컨테이너로 복사
COPY . /app

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# 데이터베이스 마이그레이션 및 정적 파일 수집
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# WSGI 서버를 사용하여 애플리케이션 실행
CMD ["gunicorn", "testDjango.wsgi:application", "--bind", "0.0.0.0:$PORT"]

# 여기서 'testDjango'는 Django 프로젝트의 이름입니다. 실제 프로젝트 이름으로 변경하세요.