from flask import Flask
from flask_migrate import Migrate
from  flask_sqlalchemy import SQLAlchemy
import config #config.py
import  os

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    # 앱 생성 및 설정
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config) #설정 파일 적용 apply config.py
    
    #ORM
    ## object relational mapping
    ## 파이썬 문법만으로도 DB를 다룰 수 있게 해줌 (쿼리작성 안해도)

    db.init_app(app)
    migrate.init_app(app,db)
    from . import models #Q/A모델들 가져오기 ->flask 의 migrate가 인식

    #청사진 (blueprint)
    from .views import main_views,question_views,answer_views
    app.register_blueprint(main_views.bp) #views/main_view 청사진을 사용
    app.register_blueprint(question_views.bp) #views/question_view 청사진을 사용
    app.register_blueprint(answer_views.bp) #views/answer_view 청사진을 사용
    #더이상 def hello() 를 사용하지 않아도 된다.
    #create_app에 여러 함수를 계쏙해서 붙일 필요x

    #템플릿 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app

# if __name__=='__init__':
#     app = create_app()
#     app.run(debug=True)

