from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required,Email,EqualTo, ValidationError


class UpdateProfile(FlaskForm):
    bio=TextAreaField('Bio',validators=[Required()])
    submit=SubmitField('Submit')

class submitblogform(FlaskForm):
    title=StringField('Title of your blog',validators=[Required()])
    blog=TextAreaField('Your blog',validators=[Required()])
    

    submit=SubmitField('Submit')

class submitcommentform(FlaskForm):
    
    comment=TextAreaField('Your comment',validators=[Required()])
    
    submit=SubmitField('Submit')


