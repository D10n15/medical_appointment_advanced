from odoo import models, fields, api

class MedicalNotification(models.Model):
    _name = 'medical.notification'
    _description = 'Medical Notification'

    appointment_id = fields.Many2one('medical.appointment', string="Cita Médica", required=True)
    message = fields.Text(string="Mensaje", required=True)
    sent = fields.Boolean(string="Enviado", default=False)

    @api.model
    def send_notifications(self):
        """ Enviar notificaciones automáticas """
        notifications = self.search([('sent', '=', False)])
        for notification in notifications:
            # Aquí podrías agregar la lógica para enviar correos o mensajes
            notification.sent = True
