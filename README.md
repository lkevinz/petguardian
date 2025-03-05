# PetGuardian

**PetGuardian** es un módulo de Odoo diseñado para la gestión integral de citas veterinarias, historial médico, vacunas y seguimiento postoperatorio para mascotas.  
Este proyecto final, desarrollado para el curso de **SGE para 2DAM**, ha sido realizado por **Jonatan Casa** y **Kevin Salinas**.  
Repositorio: [https://github.com/lkevinz/petguardian-sge](https://github.com/lkevinz/petguardian-sge)

---

## Tabla de Contenidos

- [Introducción](#introducción)
- [Características](#características)
- [Detalles de la Implementación](#detalles-de-la-implementación)
- [Instalación](#instalación)
- [Uso y Configuración](#uso-y-configuración)
- [Estructura del Módulo](#estructura-del-módulo)
- [Créditos y Contacto](#créditos-y-contacto)

---

## Introducción

El módulo **PetGuardian** ha sido desarrollado para facilitar la gestión y administración de clínicas veterinarias, ofreciendo una solución completa para:
- Programar y gestionar citas veterinarias.
- Administrar la información de pacientes (mascotas).
- Registrar y dar seguimiento a las vacunas.
- Organizar consultorios o zonas de atención.
- Gestionar datos y citas de veterinarios.

Este módulo se integra en Odoo 17 y aprovecha funcionalidades de los módulos base, mail y calendar para ofrecer una experiencia moderna e intuitiva.

---

## Características

- **Gestión de Citas Veterinarias:**  
  - Programación, visualización y seguimiento de citas mediante vistas en calendario, lista y formulario.
- **Gestión de Pacientes (Mascotas):**  
  - Registro completo con información de nombre, propietario, foto, fecha de nacimiento e historial médico.
  - Vista Kanban visual y atractiva para una rápida identificación.
- **Registro de Vacunas:**  
  - Historial de vacunación con control de fechas de aplicación y programación de próximas dosis.
- **Administración de Consultorios:**  
  - Gestión de zonas de atención o consultorios, vinculando directamente las citas.
- **Gestión de Veterinarios:**  
  - Información de contacto, especialidades y visualización de citas asociadas a cada veterinario.
- **Interfaz de Usuario Mejorada:**  
  - Diseño moderno basado en tarjetas (cards) con efectos hover, sombras y bordes redondeados.
  - Diseño responsive para un uso óptimo en dispositivos móviles y de escritorio.
- **Traducciones Integradas:**  
  - Archivo `i18n/es.po` para traducir las cadenas de texto al español, mejorando la localización del módulo.

---

## Detalles de la Implementación

Se han realizado las siguientes mejoras y funcionalidades:

1. **Mejoras en las Vistas:**
   - **Vista Kanban de Pacientes:**  
     Se ha rediseñado utilizando tarjetas que muestran la imagen, nombre y propietario, facilitando la identificación.
   - **Vistas de Citas:**  
     Se han optimizado las vistas de calendario, lista y formulario. El formulario utiliza secciones agrupadas y un fondo resaltado para destacar la información.
   - **Vista de Veterinarios:**  
     El formulario se presenta en formato "card" para una visualización clara y ordenada de los datos.

2. **Integración de Assets:**
   - Se ha implementado un archivo CSS (`static/src/css/petguardian.css`) para dar un estilo moderno con animaciones sutiles.
   - Se incluye un archivo opcional para plantillas QWeb (`static/src/xml/petguardian_templates.xml`) para futuras personalizaciones en el backend.

3. **Traducciones:**
   - Se ha incluido un archivo `i18n/es.po` que traduce automáticamente las cadenas del módulo al español, facilitando su uso en entornos hispanohablantes.

4. **Estructura y Organización:**
   - El módulo está organizado siguiendo las mejores prácticas de Odoo, con separaciones claras entre controladores, modelos, vistas, datos, seguridad y assets.

5. **Control de Accesos:**
   - Se han definido permisos de acceso básicos en `security/ir.model.access.csv` para que los usuarios puedan interactuar con los distintos modelos del módulo.

---

## Instalación

1. **Descarga y Colocación:**  
   - Clona o descarga el repositorio desde [https://github.com/lkevinz/petguardian-sge](https://github.com/lkevinz/petguardian-sge) y copia la carpeta `petguardian` en el directorio de addons de tu instancia Odoo.

2. **Actualizar la Lista de Módulos:**  
   - Desde la interfaz de Odoo, actualiza la lista de módulos.

3. **Instalación del Módulo:**  
   - Busca "PetGuardian" en la lista de módulos y haz clic en instalar.

4. **Idioma Español:**  
   - Asegúrate de tener instalado el idioma español. Si no lo tienes, agrégalo desde **Configuración > Traducciones > Idiomas** y actualiza las traducciones del módulo.

---

## Uso y Configuración

- **Menús y Navegación:**  
  Una vez instalado, encontrarás un menú principal llamado **PetGuardian** en el panel de Odoo. Desde allí se accede a:
  - **Citas:** Gestión completa de citas con vistas en calendario, lista y formulario.
  - **Pacientes:** Administración de la información de las mascotas mediante una vista Kanban.
  - **Vacunas:** Registro del historial de vacunación.
  - **Consultorios:** Gestión de zonas de atención.
  - **Veterinarios:** Información y gestión de citas de los veterinarios.

- **Interfaz Intuitiva y Responsive:**  
  El diseño moderno y responsive facilita la interacción en dispositivos móviles y de escritorio.

- **Control de Accesos:**  
  Los permisos están configurados para permitir la creación, lectura, actualización y eliminación de registros según las necesidades del usuario.

---

## Estructura del Módulo

La estructura del módulo es la siguiente:

petguardian/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── controllers.py
├── data/
│   └── demo.xml
├── i18n/
│   └── es.po
├── models/
│   ├── __init__.py
│   └── models.py
├── security/
│   └── ir.model.access.csv
├── static/
│   └── src/
│       ├── css/
│          └── petguardian.css
└── views/
    ├── office_views.xml
    ├── patient_views.xml
    ├── petguardian_menus.xml
    ├── petguardian_views.xml
    ├── templates.xml
    ├── vaccine_views.xml
    └── veterinarian_views.xml
└── README.md


Cada directorio y archivo tiene una función específica, facilitando la mantenibilidad y escalabilidad del proyecto.

---

## Créditos y Contacto

- **Autores:** Jonatan Casa y Kevin Salinas  
- **Proyecto Final:** SGE para 2DAM  
- **Repositorio:** [https://github.com/lkevinz/petguardian-sge](https://github.com/lkevinz/petguardian-sge)

Si tienes dudas, sugerencias o necesitas soporte, por favor visita el repositorio en GitHub o contáctanos mediante los canales indicados en el mismo.

---

¡Gracias por usar PetGuardian! Esperamos que este módulo te ayude a gestionar de forma eficiente tu clínica veterinaria.

