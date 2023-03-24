
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddAnimalForm(FlaskForm):
    """form for adding an animal"""

    name = StringField("Animal name",
                       validators=[InputRequired()])
    species = StringField("Species",
                       validators=[InputRequired(), AnyOf(["cat", 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0,max=30,message='age out of range')])
    notes = StringField("Notes")

class EditAnimalForm(FlaskForm):
    """form for editing an animal"""

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0,max=30,message='age out of range')])
    notes = StringField("Notes")
    available = BooleanField('Available', default=False)

