from flask_wtf import FlaskForm
from wtforms import IntegerField, DateTimeLocalField, StringField, SubmitField
from wtforms.validators import InputRequired, Optional

class FormWTFAjouterRendezVous(FlaskForm):
    id_client_wtf = IntegerField("ID du Client (ex: 1 pour Martin Sophie)", validators=[InputRequired(message="L'ID du client est obligatoire")])
    date_rdv_wtf = DateTimeLocalField("Date et Heure du rendez-vous", format='%Y-%m-%dT%H:%M', validators=[InputRequired(message="Date et heure obligatoires")])
    submit = SubmitField("Enregistrer le rendez-vous")

class FormWTFUpdateRendezVous(FlaskForm):
    id_client_update_wtf = IntegerField("ID du Client", validators=[InputRequired(message="L'ID du client est obligatoire")])
    date_rdv_update_wtf = DateTimeLocalField("Date et Heure du rendez-vous", format='%Y-%m-%dT%H:%M', validators=[InputRequired(message="Date et heure obligatoires")])
    date_annulation_update_wtf = DateTimeLocalField("Date d'annulation (Optionnel)", format='%Y-%m-%dT%H:%M', validators=[Optional()])
    submit = SubmitField("Mettre à jour le rendez-vous")

class FormWTFDeleteRendezVous(FlaskForm):
    info_rdv_delete_wtf = StringField("Effacer ce rendez-vous")
    submit_btn_del = SubmitField("Effacer définitivement")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ce RDV ?")
    submit_btn_annuler = SubmitField("Annuler")