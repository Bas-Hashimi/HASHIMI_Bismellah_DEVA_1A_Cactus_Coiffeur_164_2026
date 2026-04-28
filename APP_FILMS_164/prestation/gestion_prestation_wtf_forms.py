from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import Length, InputRequired, NumberRange

class FormWTFAjouterPrestation(FlaskForm):
    libelle_wtf = StringField("Libellé de la prestation", validators=[Length(min=2, max=100), InputRequired()])
    prix_wtf = DecimalField("Prix (CHF)", validators=[InputRequired(), NumberRange(min=0.0, message="Le prix doit être positif")])
    duree_wtf = IntegerField("Durée (minutes)", validators=[InputRequired(), NumberRange(min=1, message="La durée doit être d'au moins 1 minute")])
    submit = SubmitField("Enregistrer la prestation")

class FormWTFUpdatePrestation(FlaskForm):
    libelle_update_wtf = StringField("Libellé de la prestation", validators=[Length(min=2, max=100), InputRequired()])
    prix_update_wtf = DecimalField("Prix (CHF)", validators=[InputRequired(), NumberRange(min=0.0)])
    duree_update_wtf = IntegerField("Durée (minutes)", validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField("Mettre à jour la prestation")

class FormWTFDeletePrestation(FlaskForm):
    libelle_delete_wtf = StringField("Effacer cette prestation")
    submit_btn_del = SubmitField("Effacer la prestation")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")