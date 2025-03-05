# -*- coding: utf-8 -*-
"""
Controlador del módulo PetGuardian.
Define la ruta web para visualizar las citas veterinarias.
Autores: Jonatan Casa y Kevin Salinas
"""

from odoo import http

class PetGuardian(http.Controller):
    @http.route('/petguardian/citas', auth='user', website=True)
    def list_appointments(self, **kw):
        # Se obtienen todas las citas registradas en el modelo petguardian.appointment
        appointments = http.request.env['petguardian.appointment'].search([])
        # Se renderiza la plantilla 'list_appointments' pasando las citas encontradas
        return http.request.render('petguardian.list_appointments', {'appointments': appointments})
