from odoo import models, fields, api

class MedicalAppointment(models.Model):
    _name = 'medical.appointment'
    _description = 'Medical Appointment'

    patient_id = fields.Many2one('medical.patient', string="Paciente", required=True)
    doctor_id = fields.Many2one('medical.doctor', string="Doctor", required=True)
    date = fields.Datetime(string="Fecha y Hora", required=True)
    status = fields.Selection([
        ('scheduled', 'Programada'),
        ('completed', 'Completada'),
        ('cancelled', 'Cancelada')
    ], string="Estado", default='scheduled')

    notes = fields.Text(string="Notas")
