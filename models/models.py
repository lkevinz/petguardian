# -*- coding: utf-8 -*-
"""
Definición de los modelos para el módulo PetGuardian.
Autores: Jonatan Casa y Kevin Salinas

Modelos:
- petguardian.patient: Gestión de pacientes (mascotas).
- petguardian.appointment: Gestión de citas veterinarias.
- petguardian.vaccine: Registro del historial de vacunas.
- petguardian.office: Gestión de consultorios o zonas de atención.
- petguardian.veterinarian: Gestión de veterinarios y sus citas.
"""

from odoo import models, fields, api

class PetPatient(models.Model):
    _name = 'petguardian.patient'
    _inherit = ['mail.thread']
    _description = 'Modelo para gestionar pacientes'

    name = fields.Char(
        string="Nombre", 
        required=True, 
        tracking=True
    )
    owner_name = fields.Char(
        string="Propietario", 
        required=True
    )
    photo = fields.Image(
        string="Foto de la Mascota", 
        max_width=200, 
        max_height=200
    )
    birth_date = fields.Date(
        string="Fecha de Nacimiento"
    )
    medical_history = fields.Binary(
        string="Historial Médico"
    )
    vaccine_ids = fields.One2many(
        'petguardian.vaccine', 
        'patient_id', 
        string="Vacunas"
    )
    followup_ids = fields.One2many(
        'petguardian.followup',
        'patient_id',
        string="Seguimientos"
    )

class PetFollowup(models.Model):
    _name = 'petguardian.followup'
    _description = 'Seguimiento postoperatorio'

    followup_date = fields.Date(
        string="Fecha del Seguimiento", 
        required=True
    )
    patient_id = fields.Many2one(
        'petguardian.patient', 
        string="Paciente", 
        required=True
    )
    # Opcional: vincular seguimiento a una cita
    appointment_id = fields.Many2one(
        'petguardian.appointment',
        string="Cita Asociada"
    )
    notes = fields.Text(
        string="Observaciones"
    )
    state = fields.Selection(
        string="Estado",
        selection=[('pending', 'Pendiente'), ('completed', 'Completado'), ('canceled', 'Cancelado')],
        default='pending'
    )

class PetAppointment(models.Model):
    _name = 'petguardian.appointment'
    _inherit = ['mail.thread']
    _description = 'Modelo para gestionar citas veterinarias'

    pet_id = fields.Many2one(
        'petguardian.patient', 
        string="Mascota", 
        required=True
    )
    
    owner_name = fields.Char(
        related='pet_id.owner_name', 
        string="Propietario", 
        readonly=True
    )
    
    date = fields.Datetime(
        string="Fecha de la Cita", 
        required=True, 
        tracking=True
    )
    notes = fields.Text(string="Notas")
    
    state = fields.Selection(
        string='Estado',
        selection=[('scheduled', 'Programada'), ('completed', 'Completada'), ('canceled', 'Cancelada')],
        default='scheduled', 
        tracking=True
    )
    
    office_id = fields.Many2one(
        'petguardian.office',
        string='Zona',
        ondelete='restrict'
    )

    veterinarian_id = fields.Many2one(
        'petguardian.veterinarian',
        string='Veterinario',
        ondelete='restrict'
    )

    okey = fields.Boolean(
        string="Okey", 
        default=False,
    )

class PetVaccine(models.Model):
    _name = 'petguardian.vaccine'
    _description = 'Historial de Vacunas'

    patient_id = fields.Many2one(
        'petguardian.patient', 
        string="Mascota", 
        required=True
    )
    
    vaccine_name = fields.Char(
        string="Nombre Vacuna", 
        required=True
    )
    
    date_administered = fields.Date(
        string="Fecha de Aplicación", 
        required=True
    )
    
    next_dose = fields.Date(
        string="Programar Próxima Dosis"
    )
    
    office_id = fields.Many2one(
        'petguardian.office', 
        string="Consultorio",
        required=True
    )

class PetOffice(models.Model):
    _name = 'petguardian.office'
    _description = 'Modelo para las zonas de atención, consultorios'
    
    name = fields.Char(
        string="Nombre Consulta",
        required=True
    )

    veterinarian_id = fields.Many2one(
        'petguardian.veterinarian',
        string='Veterinario',
        required=True
    )
    
    location = fields.Selection(
        string="Zona de ubicacion",
        selection=[('1', 'Planta 1'), ('2', 'Planta 2'), ('3', 'Planta baja')]
    )
    
    PetAppointment_ids = fields.One2many(
        'petguardian.appointment',
        'office_id',
        string="Citas asociadas"
    )

class PetVeterinarian(models.Model):
    _name = 'petguardian.veterinarian'
    _description = 'Encargado de programar las citas'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    email = fields.Char(
        string='Correo',
        required=True
    )

    phone = fields.Char(
        string='Número de teléfono',
        required=True
    )

    speciality = fields.Char(
        string='Especialidad',
        required=True
    )

    appointment_ids = fields.One2many(
        'petguardian.appointment',
        'veterinarian_id',
        string="Citas asociadas"
    )
