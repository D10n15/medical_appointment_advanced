from odoo import http
from odoo.http import request, Response
import json

class MedicalAppointmentAPI(http.Controller):

    @http.route('/api/appointments', auth='public', type='json', methods=['GET'])
    def get_appointments(self):
        appointments = request.env['medical.appointment'].sudo().search([])
        data = []
        for appointment in appointments:
            data.append({
                'id': appointment.id,
                'patient': appointment.patient_id.name,
                'doctor': appointment.doctor_id.name,
                'date': appointment.date,
                'status': appointment.status,
            })
        return data

    @http.route('/api/appointments/<int:appointment_id>', auth='public', type='json', methods=['GET'])
    def get_appointment(self, appointment_id):
        appointment = request.env['medical.appointment'].sudo().browse(appointment_id)
        if not appointment.exists():
            return {'error': 'Cita no encontrada'}
        return {
            'id': appointment.id,
            'patient': appointment.patient_id.name,
            'doctor': appointment.doctor_id.name,
            'date': appointment.date,
            'status': appointment.status,
        }

    @http.route('/api/appointments', auth='public', type='json', methods=['POST'])
    def create_appointment(self, **kwargs):
        required_fields = ['patient_id', 'doctor_id', 'date', 'status']
        if not all(field in kwargs for field in required_fields):
            return {'error': 'Faltan datos requeridos'}
        
        appointment = request.env['medical.appointment'].sudo().create({
            'patient_id': kwargs['patient_id'],
            'doctor_id': kwargs['doctor_id'],
            'date': kwargs['date'],
            'status': kwargs['status'],
        })
        return {'success': 'Cita creada', 'id': appointment.id}

    @http.route('/api/appointments/<int:appointment_id>', auth='public', type='json', methods=['PUT'])
    def update_appointment(self, appointment_id, **kwargs):
        appointment = request.env['medical.appointment'].sudo().browse(appointment_id)
        if not appointment.exists():
            return {'error': 'Cita no encontrada'}
        
        appointment.sudo().write(kwargs)
        return {'success': 'Cita actualizada'}

    @http.route('/api/appointments/<int:appointment_id>', auth='public', type='json', methods=['DELETE'])
    def delete_appointment(self, appointment_id):
        appointment = request.env['medical.appointment'].sudo().browse(appointment_id)
        if not appointment.exists():
            return {'error': 'Cita no encontrada'}
        
        appointment.sudo().unlink()
        return {'success': 'Cita eliminada'}
