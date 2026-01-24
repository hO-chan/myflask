from flask import Blueprint, render_template,request,url_for

from flaskr.models import Question

from flaskr.forms import QuestionForm, AnswerForm

from datetime import datetime
from werkzeug.utils import redirect
from flaskr import db

bp = Blueprint('question', __name__, url_prefix='/question')


# @bp.route('/list/')
# def _list():
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question,form=form) 

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

@bp.route('/list/')
def _list():
    #get 방식으로 욫어한 url 에서 page 값을 가져올 때 사용
    page = request.args.get('page',type= int, default=1) #페이지

    question_list = Question.query.order_by(Question.create_date.desc())
    #조회한 데이터 q_list에 paginate 함수로 페이징을 적용
    ## (현재 조회할 페이지 번호, 부터 ㅁ개씩 보여주기)
    ## Pagination 객체가 return 됨
    question_list =question_list.paginate(page=page,per_page=10)
    return render_template('question/question_list.html',question_list=question_list)