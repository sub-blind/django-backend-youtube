# django-backend-youtube

# 1일차

## 프로젝트 세팅

### 1. Github

- 레포지토리 생성
- 로컬에 있는 내 컴퓨터 폴더와 깃헙의 Remote 공간 연결
- git clone https://github.com/sub-blind/django-backend-youtube
- 깃헙 데스크탑 프로그램 다운

### 2. Docker Hub

- 회원가입
- 나의 컴퓨ㅜ터에 가상환경을 구축(윈도우, 맥 -> 리눅스 환경 구축(MySQL, Python, Redis))
- AccessToken값을 github에 레포지토리에 등록

### 3. 장고 프로젝트 세팅

- 실제 배포 환경
- requirements.txt 실제 배포할때
- requirements.dev.txt 개발하고 연습할 때 사용(파이썬 패키지 관리) DRF 버전업 할때
- 실전 : 패키지 의존성 관리 -> 버전관리, 패키지들 간의 관계 관리
- docker-compose run --rm app sh -c 'python manage.py runserver'
- docker compose up

### PostgreSQL 을 쓴 이유

- ACID 호환성: PostgreSQL은 ACID(Atomicity, Consistency, Isolation, Durability)를 준수하는 관계형 데이터베이스로, 데이터 무결성과 일관성을 보장합니다.

- 완전한 기능 세트: PostgreSQL은 다양한 기능을 제공하여 복잡한 데이터베이스 작업을 수행할 수 있습니다. 이는 외부 키, 서브쿼리, 다중 버전 동시성 제어 등을 포함합니다.

- 확장성: PostgreSQL은 대규모 데이터베이스와 고성능 애플리케이션을 위한 확장성을 제공합니다. 복제, 파티셔닝, 스트리밍 복제 등의 기능을 사용하여 성능을 향상시킬 수 있습니다.

- JSON 및 XML 지원: PostgreSQL은 JSON 및 XML과 같은 반정형 데이터 형식을 지원합니다. 이는 더 유연한 데이터 모델링을 가능하게 합니다.

- django에서 추천하는 DB
- ![Untitled](https://github.com/sub-blind/django-backend-youtube/assets/58137602/a3145f4a-f006-4d75-aa34-9eeee5dabad8)

### DRF 셋팅

- Setup DRF(Django Restframework) & DRF-Spectacular
