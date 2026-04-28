from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class FormWTFAjouterRdvPrestation(FlaskForm):
    id_rdv_wtf = IntegerField("ID du Rendez-vous", validators=[InputRequired()])
    id_prestation_wtf = IntegerField("ID de la Prestation", validators=[InputRequired()])
    quantite_wtf = IntegerField("Quantité", default=1, validators=[InputRequired(), NumberRange(min=1)])
    prix_prestation_wtf = DecimalField("Prix appliqué (CHF)", validators=[InputRequired()])
    submit = SubmitField("Lier la prestation au RDV")

class FormWTFUpdateRdvPrestation(FlaskForm):
    quantite_update_wtf = IntegerField("Quantité", validators=[InputRequired(), NumberRange(min=1)])
    prix_prestation_update_wtf = DecimalField("Prix appliqué (CHF)", validators=[InputRequired()])
    submit = SubmitField("Mettre à jour")

class FormWTFDeleteRdvPrestation(FlaskForm):
    info_rdv_pres_delete_wtf = StringField("Détails de la liaison", render_kw={'readonly': True})
    submit_btn_del = SubmitField("Supprimer cette liaison")
    submit_btn_conf_del = SubmitField("Confirmer la suppression ?")
    submit_btn_annuler = SubmitField("Annuler")