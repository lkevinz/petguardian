# -*- coding: utf-8 -*-
{
    'name': "petguardian",
    'summary': "Gestión de citas veterinarias, vacunas y pacientes.",
    'description': """
        PetGuardian permite gestionar citas veterinarias, historial médico,
        vacunas y seguimiento postoperatorio con vistas Kanban y Calendario.
        Proyecto final de SGE para 2DAM.
    """,
    'author': "Jonatan Casa y Kevin Salinas",
    'website': "https://github.com/lkevinz/petguardian",
    'category': 'Tools',
    'version': '1.0',
    'depends': ['base', 'mail', 'calendar'],
    'data': [
        'security/ir.model.access.csv',   # Definición de accesos a los modelos
        'views/petguardian_views.xml',      # Vistas de Citas
        'views/patient_views.xml',          # Vista Kanban de Pacientes
        'views/vaccine_views.xml',          # Vistas de Vacunas
        'views/office_views.xml',           # Vistas de Consultorios
        'views/veterinarian_views.xml',     # Vistas de Veterinarios
        'views/petguardian_menus.xml',      # Menús del módulo
        'views/templates.xml',              # Plantilla web para listar Citas
    ],
    'demo': [
        'data/demo.xml',                  # Datos de demostración
    ],
    'assets': {
        'web.assets_backend': [
            # Archivo CSS personalizado para mejorar la apariencia
            'petguardian/static/src/css/petguardian.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
