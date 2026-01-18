import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'flaskr.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False





'''
https://wikidocs.net/81045

SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소이고 
SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트를 처리하는 옵션이다.
이 옵션은 파이보에 필요하지 않으므로 False로 비활성화하자.
SQLALCHEMY_DATABASE_URI 설정에 의해 SQLite 데이터베이스가 사용되고 
데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장된다.


SQLite는 어떤 데이터베이스일까?

파이썬 기본 패키지에 포함된 SQLite는 
주로 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 데이터베이스다. 
보통은 SQLite로 개발을 빠르게 진행하고 이후 실제 운영 시스템에 반영할 때에는 좀 더 규모가 큰 데이터베이스로 교체한다.





'''