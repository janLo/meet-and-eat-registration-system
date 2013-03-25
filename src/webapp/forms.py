from flask.ext.wtf import Form, TextField, Required, Email
from flask.ext.wtf.html5 import EmailField, IntegerField, DecimalField
from wtforms import BooleanField, PasswordField


class TeamRegisterForm(Form):
    name = TextField("Teamname", validators=[Required()])
    email = EmailField("Email", validators=[Required(), Email()])
    phone = IntegerField("Telefonnummer", validators=[Required()])
    address = TextField("Adresse", validators=[Required()])
    zipno = TextField("Postleitzahl", validators=[Required()])
    address_info = TextField("Adresszusatz", default="")
    lat = DecimalField("Lat", validators=[Required()])
    lon = DecimalField("Lon", validators=[Required()])
    member1 = TextField("Teammitglied 3", validators=[Required()])
    member2 = TextField("Teammitglied 3", validators=[Required()])
    member3 = TextField("Teammitglied 3", validators=[Required()])
    allergies = TextField("Allergien", default="")
    vegetarians = IntegerField("Vegetarier", validators={Required()}, default=0)
    legal_accepted = BooleanField("Datenschutzbestimmungen", validators=[Required()])
    information = BooleanField("Informationen")


class AdminLoginForm(Form):
    login = TextField("Login")
    password = PasswordField("Passwort")