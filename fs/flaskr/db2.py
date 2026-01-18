import sqlite3
from datetime import datetime

import click
from flask import current_app, g


def get_db(): #현재 요청에서 DB 연결이 없으면 새로 만들고, 있으면 재사용
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None): #요청이 끝날 때 연결이 있으면 닫음
    db = g.pop('db', None)

    if db is not None:
        db.close()

# db 연결 시 사용하는 code


'''
g
Flask의 요청 단위 저장소
같은 요청 안에서 여러 함수가 DB를 쓰더라도 연결 1개를 공유/재사용하게 하려고 g.db에 저장합니다.

current_app
“지금 이 요청을 처리 중인 Flask 앱 객체”를 가리키는 특수 객체
팩토리 패턴에서는 전역 app이 없으니, 요청 시점에는 current_app로 접근합니다.


sqlite3.connect()
설정값 DATABASE가 가리키는 파일에 연결합니다.
DB 파일은 아직 없어도 되고, “초기화(init)”를 수행하면 생성됩니다.

sqlite3.Row
결과 row를 dict처럼 다룰 수 있게 해서, row["username"]처럼 컬럼명으로 접근 가능하게 합니다.

'''