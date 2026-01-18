'''
데이터베이스 관리 명령어 정리하기
앞으로 모델을 추가하거나 변경할 때는 flask db migrate 명령과 flask db upgrade 명령만 사용할 것이다. 즉, 앞으로 데이터베이스 관리를 위해 여러분이 반드시 알아야 할 명령어는 다음 2가지이다.

[표 2-2 데이터베이스 관리 명령어]

명령어	설명
flask db migrate	모델을 새로 생성하거나 변경할 때 사용 (실행하면 작업파일이 생성된다.)
flask db upgrade	모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용 (위에서 생성된 작업파일을 실행하여 데이터베이스를 변경한다.)

모델 만들기
https://wikidocs.net/81045
모델은 데이터를 다룰 목적으로 만든 파이썬 클래스다.

### 모델 속성 구상하기

질문과 답변 모델에는 어떤 속성이 있어야 할까?

[질문 모델 속성]
속성명	    설명
id	        질문      데이터의 고유 번호
subject	    질문      제목
content	    질문      내용
create_date	질문      작성일시

[답변 모델 속성]
속성명	        설명
id	            답변 데이터의 고유 번호
question_id	    질문 데이터의 고유 번호
(어떤 질문에 달린 답변인지 알아야 하므로 질문 데이터의 고유 번호가 필요하다)
content	        답변  내용
create_date	    답변  작성일시

질문 모델 생성하기
이렇게 구상한 속성을 바탕으로 모델을 정의해 보자. 먼저 pybo 디렉터리에 모델을 정의하기 위한 models.py 파일을 생성하고 질문 모델인 Question 클래스를 다음과 같이 작성해 보자.

models.py 파일에는 모델 클래스들을 정의하여 사용할 것이다.
'''
from flaskr import db

# 질문 생성 및 요소 추가
##Question 모델을 통해 테이블이 생성되면 테이블명은 question이 된다. -> SQLAlchemy conventions
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary_key -> each id is uniq
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


#답변 생성 및 요소 설정
## https://docs.sqlalchemy.org/en/13/core/type_basics.html 추가적인 속성들
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #질문과 연결하기 위한 속성, db.ForeignKey로 두 모델을 서로 연결,
    #q_id는 Q테이블의 id 칼럼과 연결됨, CASCADE -> 질문 삭제 시 해당 질문 관련 답변도 함께 삭제
    #다만 파이썬 코드로 질문 삭제 시  답변 데이터를 모두 삭제하지는 않음
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    #Question -> 참조 모델 명 / backref = 역참조 설정| 질문-> 답변으로의 접근
    #q1.answer_set 으로 답변 접근이 가능하다
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

















