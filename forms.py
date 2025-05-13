from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, IPAddress, InputRequired, EqualTo

class Login(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=3, max=150)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesion')

#TODO form de registro en los campos faltantes
class Register(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=3, max=150)]) #CURP
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=20)])
    apPaterno = StringField('Apellido Materno', validators=[DataRequired()])
    apMaterno = StringField('Apellido Materno', validators=[DataRequired()])
    numTelefono = StringField('Numero de telefono', validators=[DataRequired(), Length(min=13, max=13)])
    submit = SubmitField('Registrarse')


class changePassword(FlaskForm):
    password = PasswordField('Ingrese la contraseña', [InputRequired(), EqualTo('confirm', message='Las contraseñas deben coincidir')])
    confirm  = PasswordField('Repite la contraseña')
    ipSuplicant = IPAddress(IPAddress)

