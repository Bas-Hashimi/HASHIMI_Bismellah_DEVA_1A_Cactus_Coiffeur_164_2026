from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired

class FormWTFAjouterRdvEmploye(FlaskForm):
    id_rdv_wtf = IntegerField("ID du Rendez-vous", validators=[InputRequired(message="L'ID du RDV est obligatoire")])
    id_employe_wtf = IntegerField("ID de l'Employé (Coiffeur)", validators=[InputRequired(message="L'ID de l'employé est obligatoire")])
    submit = SubmitField("Assigner l'employé au RDV")

class FormWTFDeleteRdvEmploye(FlaskForm):
    info_rdv_emp_delete_wtf = StringField("Détails de l'assignation", render_kw={'readonly': True})
    submit_btn_del = SubmitField("Supprimer cette assignation")
    submit_btn_conf_del = SubmitField("Confirmer la suppression ?")
    submit_btn_annuler = SubmitField("Annuler")