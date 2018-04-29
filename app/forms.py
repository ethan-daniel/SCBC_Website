from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class SubmitForm(FlaskForm):
    place = StringField('Place', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    type = SelectField('Type', choices=[("", ""), ("Bike Shop", "Bike Shop"), ("Karma Kit", "Karma Kit"),
                                        ("Sponsor", "Sponsor"), ("Water", "Water"), ], validators=[DataRequired()])
    submit = SubmitField('Submit')
