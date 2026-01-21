from flask import Blueprint, render_template,request,url_for

from flaskr.models import Question

from flaskr.forms import QuestionForm

from datetime import datetime
from werkzeug.utils import redirect
from flaskr import db

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question) 

@bp.route('/create/',methods=('GET','POST'))
def create():
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit():
        # 적힌 정보 기반으로 필요한 형태의 데이터 생성
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        # db에 추가 및 저장
        db.session.add(question)
        db.session.commit()
        # main으로 이동
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html',form=form)
