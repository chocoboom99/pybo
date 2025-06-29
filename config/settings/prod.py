# config/settings/prod.py

from .base import * # base.py의 모든 설정을 가져옵니다.

DEBUG = False # 운영 환경에서는 항상 False여야 합니다.

ALLOWED_HOSTS = ['52.78.16.227'] # 운영 서버의 실제 IP 주소 또는 도메인

# 운영 환경에 맞는 다른 설정들 (DB, SECRET_KEY 로드 방식, 로깅 등)을 여기에 추가합니다.