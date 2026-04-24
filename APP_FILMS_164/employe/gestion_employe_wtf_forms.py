from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, InputRequired, Regexp

class FormWTFAjouterEmploye(FlaskForm):
    nom_employe_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"

    nom_employe_wtf = StringField("Nom de l'employé ", validators=[Length(min=2, max=50), Regexp(nom_employe_regexp)])
    prenom_employe_wtf = StringField("Prénom de l'employé ", validators=[Length(min=2, max=50), Regexp(nom_employe_regexp)])
    post_employe_wtf = StringField("Poste de l'employé ", validators=[Length(min=2, max=50), InputRequired()])

    submit = SubmitField("Enregistrer employé")

class FormWTFUpdateEmploye(FlaskForm):
    nom_employe_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"

    nom_employe_update_wtf = StringField("Nom de l'employé ", validators=[Length(min=2, max=50), Regexp(nom_employe_update_regexp)])
    prenom_employe_update_wtf = StringField("Prénom de l'employé ", validators=[Length(min=2, max=50), Regexp(nom_employe_update_regexp)])
    post_employe_update_wtf = StringField("Poste de l'employé ", validators=[Length(min=2, max=50), InputRequired()])

    submit = SubmitField("Mettre à jour l'employé")

class FormWTFDeleteEmploye(FlaskForm):
    nom_employe_delete_wtf = StringField("Effacer cet employé")
    submit_btn_del = SubmitField("Effacer employé")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")