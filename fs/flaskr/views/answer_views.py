from datetime import datetime

from flask import Blueprint,url_for,request,render_template
from werkzeug.utils  import redirect

from flaskr import db
from flaskr.models import Question,Answer

from flaskr.forms import AnswerForm

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>',methods=('POST',))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit():
        content = request.form['content'] #폼 중 이름이 content인
        #탬플릿의 form 애들은 request 객체로 얻을 수 있음
        answer = Answer(content=content, create_date=datetime.now())
        question.answer_set.append(answer)
        #question 과 answer 모델은 서로 연결되어있음
        #backref 에 설정한 answer_set을 사용 할 수 있음
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html',question = question, fomr = form)


'''
블루프린트를 만들었다면  __init__.py 에 블루 프린트를 등록하자
'''