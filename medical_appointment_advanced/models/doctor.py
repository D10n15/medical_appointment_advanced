from odoo import models, fields

class MedicalDoctor(models.Model):
    _name = 'medical.doctor'
    _description = 'Medical Doctor'

    name = fields.Char(string="Nombre", required=True)
    specialty = fields.Char(string="Especialidad")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo Electrónico")
    appointments = fields.One2many('medical.appointment', 'doctor_id', string="Citas")
