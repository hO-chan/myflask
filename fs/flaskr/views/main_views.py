from flask import Blueprint, url_for
from werkzeug.utils import redirect

from flaskr.models import Question

bp = Blueprint('main', __name__, url_prefix='/')
# main 은 별명,  __name__ == main_views (.py)
#url_prefix 는 이 함수를 호출하는 주소 지금은 :5000/임

@bp.route('/hello') #app.route 에서 bp.route 로 바뀜
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

'''
from flask import Blueprint, render_template
from werkzeug.utils import redirect

def index():
    question_list = Question.query.order_by(Question.create_date.desc())

    return redirect('question/question_list.html',question_list = question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question)

detail 함수 제거, index 함수는 question._list 에 해당하는
URL로 redirect 하도록 코드 수정.
url_for 함수는 라우팅 함수명으로 URL 을 역으로 찾는 func
question 이라는 블루 프린트 먼저 찾고
# bp = Blueprint('question', __name__, url_prefix='/question')
(question_views.py 에 정의했던 청사진)
_list 함수명을 찾음
'''
#



'''
render_template 함수는 템플릿 파일을 화면으로 렌더링 
하는 함수이다. 조회한 질문 목록 데이터를 render_template
함수의 파라미터로 전달하면 템플릿에서 해당 데이터로 화면을 
구성할수 있다. 여기서 사용한 question/question_list.html
파일을 템플릿 파일이라고 부른다.

탬플릿 파일은 쉽게 말해 파이썬 문법을 사용 할 수 있는
HTML 파일이다. html과 비슷하나 플라스크의 특별한 태그를
쓸 수 있다.
'''




'''
https://wikidocs.net/81510


새로운 URL 매핑이 필요할 때마다 라우팅 함수를 create_app 함수 안에 계속 추가해야 한다. 
이렇게 라우팅 함수가 계속 추가된다면 create_app 함수는 엄청나게 크고 복잡한 함수가 될 것이다.

하지만 걱정하지 말자. 블루프린트(Blueprint)를 사용하면 이 문제를 해결할 수 있다.

플라스크의 블루프린트를 이용하면 라우팅 함수를 체계적으로 관리할 수 있다. 
블루프린트(blueprint)는 보통 객체지향 프로그래밍에서 "청사진"을 뜻하는 용어인데
플라스크에서는 URL과 함수의 매핑을 관리하기 위해 사용하는 도구(클래스)이다.


'''