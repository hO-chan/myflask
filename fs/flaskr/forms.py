from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired,Email

# 질문 폼 만들기
class QuestionForm(FlaskForm): #플라스크 폼은 FlaskFrom 을 상속하여 만들어야함
    #글자 수 제한이 있음
    subject = StringField('제목', validators=[DataRequired()])
    
    # email = StringField('이메일',validators=[Email()])
    #글자 수 제한이 없음
    content = StringField('내용', validators=[DataRequired('내용은 필수로 작성 항목 입니다.')])
    #https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
    #https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators


# 답변 폼 만들기

class AnswerForm(FlaskForm):
    content = TextAreaField('내용',validators=[DataRequired('내용은 필수로 작성해야합니다.')])
    #오타나면 안된디. context 라 썼더니 에러남