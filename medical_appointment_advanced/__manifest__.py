{
    'name': 'Medical Appointment Advanced',
    'version': '1.0',
    'summary': 'Gestión avanzada de citas médicas en Odoo 18 Enterprise',
    'sequence': -100,
    'description': """Módulo avanzado para la gestión de citas médicas""",
    'category': 'Medical',
    'author': 'Yefferson',
    'website': 'https://tu-sitio-web.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],  # Dependencias necesarias
    'data': [
        'security/ir.model.access.csv',  # Permisos de acceso
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/notification_view.xml',
        'data/email_template.xml',
        'data/cron_job.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'medical_appointment_advanced/static/src/css/style.css',
            'medical_appointment_advanced/static/src/js/appointment.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

