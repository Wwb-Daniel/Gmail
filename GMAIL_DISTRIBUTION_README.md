# 📧 Gmail Malware Distribution System

## ⚠️ ADVERTENCIA IMPORTANTE
**Este sistema es únicamente para fines educativos y de investigación en seguridad cibernética.**
**NO debe ser usado para actividades maliciosas o ilegales.**

---

## 🎯 Descripción del Sistema

El sistema de distribución por Gmail es una herramienta completa para la distribución automatizada de malware a través de correos electrónicos usando cuentas de Gmail. Incluye plantillas sofisticadas, listas de objetivos, y técnicas de evasión avanzadas.

---

## 📁 Archivos del Sistema

### 🔧 Scripts Principales
- **`gmail_master.py`** - Sistema maestro que coordina toda la distribución
- **`gmail_distributor.py`** - Distribuidor principal de emails
- **`gmail_setup.py`** - Configurador de cuentas Gmail
- **`email_list_generator.py`** - Generador de listas de emails objetivo

### ⚙️ Archivos de Configuración
- **`gmail_config.json`** - Configuración del sistema
- **`gmail_distribution_config.json`** - Configuración de distribución
- **`gmail_accounts.json`** - Cuentas Gmail configuradas

### 📧 Listas de Emails
- **`target_emails.txt`** - Lista principal de objetivos
- **`high_value_targets.txt`** - Objetivos de alto valor
- **`corporate_emails.txt`** - Empleados corporativos
- **`government_emails.txt`** - Empleados gubernamentales
- **`university_emails.txt`** - Estudiantes y personal universitario

### 📊 Logs y Estadísticas
- **`gmail_campaign_log.json`** - Log de campañas
- **`email_list_stats.json`** - Estadísticas de listas de emails

---

## 🚀 Instalación y Configuración

### 1. Instalar Dependencias
```bash
pip install smtplib ssl email json random threading datetime
```

### 2. Configurar Cuentas Gmail
```bash
python gmail_setup.py
```

**Importante**: Necesitas configurar App Passwords en Gmail:
1. Habilitar 2-Factor Authentication
2. Ir a Google Account → Security → App passwords
3. Generar una contraseña de aplicación
4. Usar esta contraseña (no tu contraseña normal)

### 3. Generar Listas de Emails
```bash
python email_list_generator.py
```

### 4. Ejecutar el Sistema
```bash
python gmail_master.py
```

---

## 📧 Plantillas de Email Incluidas

### 🏢 Corporativas
- **Microsoft Security Update** - Actualización de seguridad urgente
- **LinkedIn Job Opportunity** - Oferta de trabajo remoto
- **Adobe License Verification** - Verificación de licencia

### 🏛️ Gubernamentales
- **IRS Tax Refund** - Reembolso de impuestos
- **Bank Security Alert** - Alerta de seguridad bancaria

### 🛒 Comerciales
- **Amazon Prime Renewal** - Renovación de membresía
- **Netflix Suspension** - Suspensión de cuenta
- **PayPal Security Alert** - Alerta de seguridad PayPal

### 🎓 Educativas
- **Zoom Meeting Invitation** - Invitación a reunión de seguridad
- **University Security Update** - Actualización de seguridad universitaria

---

## 🎯 Categorías de Objetivos

### 👔 Empleados Corporativos
- **Dominios**: @company.com, @corporation.com, @enterprise.com
- **Plantillas preferidas**: Microsoft Security, LinkedIn Jobs
- **Características**: Acceso a sistemas corporativos, datos sensibles

### 🏛️ Empleados Gubernamentales
- **Dominios**: @gov, @government.com, @state.gov
- **Plantillas preferidas**: IRS Refund, Bank Security
- **Características**: Información clasificada, sistemas críticos

### 🎓 Estudiantes Universitarios
- **Dominios**: @university.edu, @college.edu, @school.edu
- **Plantillas preferidas**: LinkedIn Jobs, Netflix Suspension
- **Características**: Acceso a redes universitarias, datos de investigación

### 👥 Usuarios Generales
- **Dominios**: @gmail.com, @yahoo.com, @hotmail.com
- **Plantillas preferidas**: Amazon Prime, Netflix, PayPal
- **Características**: Datos personales, información financiera

---

## ⚙️ Configuración Avanzada

### 📊 Límites de Distribución
```json
{
  "campaign_settings": {
    "emails_per_hour": 15,
    "max_emails_per_day": 200,
    "delay_between_emails": "30-120 seconds"
  }
}
```

### 🛡️ Técnicas de Evasión
- **Headers personalizados** - Agregar headers legítimos
- **Spoofing de remitente** - Usar dominios legítimos
- **Ofuscación de contenido** - Codificación HTML, caracteres invisibles
- **Delays aleatorios** - Evitar detección por patrones

### 📈 Monitoreo
- **Tracking de aperturas** - Monitorear emails abiertos
- **Tracking de clicks** - Monitorear enlaces clickeados
- **Tracking de adjuntos** - Monitorear archivos descargados
- **Logs completos** - Registrar toda la actividad

---

## 🔧 Uso del Sistema

### 1. Configuración Inicial
```bash
# Ejecutar el asistente de configuración
python gmail_master.py

# Seleccionar opción 1: Setup Gmail Accounts
# Agregar cuentas Gmail con App Passwords
```

### 2. Generar Listas de Objetivos
```bash
# Seleccionar opción 2: Generate Email Lists
# Generar listas categorizadas de emails
```

### 3. Iniciar Campaña
```bash
# Seleccionar opción 3: Start Distribution Campaign
# El sistema comenzará a enviar emails automáticamente
```

### 4. Monitorear Progreso
```bash
# Seleccionar opción 4: View Campaign Logs
# Ver estadísticas y resultados de la campaña
```

---

## 📊 Métricas de Éxito

### 🎯 Objetivos de Campaña
- **Tasa de entrega**: >90%
- **Tasa de apertura**: >20%
- **Tasa de click**: >5%
- **Tasa de descarga**: >2%

### 📈 Monitoreo en Tiempo Real
- Emails enviados por hora
- Tasa de éxito de entrega
- Errores y fallos
- Objetivos alcanzados

---

## 🛡️ Medidas de Seguridad

### 🔒 Para el Atacante
- **Usar VPN** - Ocultar ubicación real
- **Usar Tor** - Anonimato adicional
- **Cuentas desechables** - No usar cuentas personales
- **Límites de velocidad** - Evitar detección por spam

### 🚨 Para las Víctimas
- **Verificar remitente** - Confirmar autenticidad
- **No abrir adjuntos** - Especialmente .exe
- **Usar antivirus** - Protección actualizada
- **Educación** - Reconocer phishing

---

## ⚖️ Consideraciones Legales

### 🚨 ADVERTENCIAS CRÍTICAS
1. **Solo usar en entornos controlados**
2. **Obtener permisos explícitos**
3. **Cumplir con todas las leyes locales**
4. **Usar únicamente para investigación ética**
5. **No usar contra sistemas sin autorización**

### 📋 Responsabilidades
- El usuario es responsable del uso ético
- Debe cumplir con regulaciones locales
- Solo usar en sistemas propios o autorizados
- Mantener confidencialidad de datos

---

## 🔍 Detección y Prevención

### 🛡️ Para Empresas
- **Filtros de email** - Detectar phishing
- **Educación de empleados** - Reconocer amenazas
- **Monitoreo de red** - Detectar actividad sospechosa
- **Respuesta a incidentes** - Plan de contingencia

### 🚨 Señales de Ataque
- Emails con adjuntos .exe
- Remitentes falsificados
- Urgencia artificial
- Enlaces sospechosos

---

## 📞 Soporte y Recursos

### 📚 Documentación
- Revisar todos los archivos README
- Consultar logs de campaña
- Verificar configuraciones

### 🔧 Solución de Problemas
- Verificar App Passwords de Gmail
- Comprobar límites de envío
- Revisar logs de errores
- Validar listas de emails

---

## 🎓 Uso Educativo

### 🔬 Investigación en Seguridad
- Estudiar técnicas de phishing
- Analizar patrones de ataque
- Desarrollar defensas
- Entrenar equipos de seguridad

### 🏫 Entornos de Laboratorio
- Simulaciones controladas
- Pruebas de penetración
- Entrenamiento de personal
- Desarrollo de contramedidas

---

**Recuerda: Este sistema es para fines educativos únicamente. El uso malicioso es ilegal y está prohibido.**

