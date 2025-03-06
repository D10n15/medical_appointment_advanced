from odoo import models, fields, api
from odoo.exceptions import ValidationError
import uuid

class MedicalPatient(models.Model):
    _name = 'medical.patient'
    _description = 'Paciente'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo', required=True)
    phone = fields.Char(string='Teléfono')
    age = fields.Integer(string='Edad', required=True)
    identifier = fields.Char(string='Identificador Único', readonly=True, copy=False, default=lambda self: str(uuid.uuid4()))

    _sql_constraints = [
        ('unique_email', 'unique(email)', 'El correo ya está en uso.'),
    ]

    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError("La edad debe ser mayor a 0.")
