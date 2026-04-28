from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class FormWTFAjouterVente(FlaskForm):
    id_employe_wtf = IntegerField("ID de l'employé", validators=[InputRequired(message="Champ obligatoire")])
    id_produit_wtf = IntegerField("ID du produit", validators=[InputRequired(message="Champ obligatoire")])
    id_client_wtf = IntegerField("ID du client", validators=[InputRequired(message="Champ obligatoire")])
    quantite_wtf = IntegerField("Quantité", validators=[InputRequired(message="Champ obligatoire"), NumberRange(min=1, message="La quantité doit être au moins 1")])
    submit = SubmitField("Enregistrer la vente")

class FormWTFUpdateVente(FlaskForm):
    id_employe_update_wtf = IntegerField("ID de l'employé", validators=[InputRequired()])
    id_produit_update_wtf = IntegerField("ID du produit", validators=[InputRequired()])
    id_client_update_wtf = IntegerField("ID du client", validators=[InputRequired()])
    quantite_update_wtf = IntegerField("Quantité", validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField("Mettre à jour la vente")

class FormWTFDeleteVente(FlaskForm):
    info_vente_delete_wtf = StringField("Effacer cette vente", render_kw={'readonly': True})
    submit_btn_del = SubmitField("Effacer définitivement")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer cette vente ?")
    submit_btn_annuler = SubmitField("Annuler")