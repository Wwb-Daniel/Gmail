# 🦠 Malware Distribution Guide

## ⚠️ ADVERTENCIA IMPORTANTE
**Este kit es únicamente para fines educativos y de investigación en seguridad cibernética.**
**NO debe ser usado para actividades maliciosas o ilegales.**

---

## 📋 Contenido del Kit de Distribución

### 🎯 Archivos Principales
- **`app.py`** - Malware principal con todas las funcionalidades
- **`master_distributor.py`** - Coordinador maestro de distribución
- **`auto_distribute.py`** - Sistema de distribución automatizada
- **`distribution_config.json`** - Configuración de distribución

### 📧 Campañas de Email
- **`email_template_1.txt`** - Plantilla: Actualización de Seguridad Microsoft
- **`email_template_2.txt`** - Plantilla: Factura Pendiente PayPal
- **`email_template_3.txt`** - Plantilla: Oferta de Trabajo LinkedIn

### 📱 Redes Sociales
- **`social_media_posts.txt`** - Posts para distribución en redes sociales

### 💾 Distribución Física
- **`usb_strategy.json`** - Estrategia de USB drops
- **`autorun.inf`** - Archivo de auto-ejecución para USB

### 🌐 Propagación de Red
- **`network_worm.py`** - Gusano para propagación en red
- **`network_strategy.json`** - Estrategia de propagación de red

### 🏞️ Ataques de Watering Hole
- **`watering_hole_strategy.json`** - Estrategia de sitios comprometidos

### 🔗 Cadena de Suministro
- **`supply_chain_strategy.json`** - Ataques a la cadena de suministro

### 📱 Distribución Móvil
- **`mobile_strategy.json`** - Estrategias para dispositivos móviles

### 🖥️ Servidor C2
- **`c2_server.py`** - Servidor de comando y control

### 📦 Kit Completo
- **`malware_distribution_kit.zip`** - Kit completo de distribución

---

## 🚀 Instrucciones de Uso

### 1. Configuración Inicial
```bash
# Instalar dependencias
pip install flask requests psutil pynput cryptography

# Configurar el archivo de configuración
nano distribution_config.json
```

### 2. Personalización
- Edita `distribution_config.json` para personalizar la campaña
- Modifica las plantillas de email según tus necesidades
- Ajusta los objetivos y métodos de distribución

### 3. Crear Payloads Ofuscados
```bash
python master_distributor.py
```

### 4. Ejecutar Campaña de Distribución
```bash
# Distribución automatizada
python auto_distribute.py

# O usar el coordinador maestro
python master_distributor.py
```

### 5. Monitorear Infecciones
- El servidor C2 se ejecuta en `http://localhost:8080`
- Revisa `campaign_stats.json` para estadísticas
- Monitorea los logs de infección

---

## 🎯 Métodos de Distribución

### 📧 Email Phishing
- **Objetivo**: Empleados corporativos, usuarios generales
- **Método**: Emails con archivos adjuntos maliciosos
- **Plantillas**: Actualizaciones de seguridad, facturas, ofertas de trabajo

### 📱 Redes Sociales
- **Objetivo**: Usuarios jóvenes, gamers, entusiastas de crypto
- **Método**: Posts atractivos con enlaces maliciosos
- **Plataformas**: Facebook, Twitter, Instagram, LinkedIn, TikTok

### 💾 USB Drops
- **Objetivo**: Empleados de empresas, estudiantes universitarios
- **Método**: USBs con archivos atractivos en ubicaciones estratégicas
- **Ubicaciones**: Estacionamientos, universidades, cafeterías

### 🌐 Propagación de Red
- **Objetivo**: Sistemas en la misma red
- **Método**: Explotación de vulnerabilidades SMB, RDP, SSH
- **Técnicas**: EternalBlue, BlueKeep, SMBGhost

### 🏞️ Watering Hole
- **Objetivo**: Visitantes de sitios web específicos
- **Método**: Compromiso de sitios web legítimos
- **Técnicas**: Inyección de código, anuncios maliciosos

---

## 🔧 Funcionalidades del Malware

### 🛡️ Desactivación de Seguridad
- Windows Defender
- Windows Firewall
- User Account Control (UAC)
- Windows Update
- SmartScreen

### 📁 Robo de Datos
- Datos de navegadores (Chrome, Edge, Firefox)
- Documentos importantes
- Contraseñas WiFi
- Información del sistema

### 🔄 Persistencia
- Registro de Windows
- Carpeta de inicio
- Servicios de Windows
- Tareas programadas

### ⌨️ Keylogging
- Captura de teclas
- Registro de procesos activos
- Almacenamiento en archivos JSON

### ⛏️ Minería de Criptomonedas
- Uso de CPU para minería
- Operación en segundo plano
- Simulación de trabajo de minería

### 🔐 Encriptación de Archivos
- Encriptación de documentos importantes
- Extensión .encrypted
- Cifrado Fernet

### 🌐 Escaneo de Red
- Detección de objetivos vulnerables
- Escaneo de puertos comunes
- Identificación de servicios

---

## 📊 Métricas de Éxito

### 🎯 Objetivos de Infección
- **Tasa de infección objetivo**: 5%
- **Tasa de persistencia objetivo**: 80%
- **Exfiltración de datos objetivo**: 1GB por día
- **Movimiento lateral objetivo**: 10 máquinas por infección

### 📈 Monitoreo
- Número total de infecciones
- Tiempo de ejecución de la campaña
- Datos exfiltrados
- Máquinas comprometidas

---

## ⚖️ Consideraciones Legales

### 🚨 ADVERTENCIAS IMPORTANTES
1. **Solo usar en entornos controlados**
2. **Obtener permisos explícitos**
3. **Cumplir con todas las leyes locales**
4. **Usar únicamente para investigación ética**
5. **No usar contra sistemas sin autorización**

### 📋 Responsabilidades
- El usuario es responsable del uso ético de este kit
- Debe cumplir con todas las regulaciones locales
- Solo usar en sistemas propios o con autorización explícita
- Mantener la confidencialidad de los datos obtenidos

---

## 🔍 Detección y Prevención

### 🛡️ Medidas de Seguridad
- Mantener software actualizado
- Usar antivirus actualizado
- Educar a los usuarios sobre phishing
- Implementar filtros de email
- Monitorear actividad de red

### 🚨 Señales de Infección
- Desactivación inesperada de antivirus
- Archivos encriptados con extensión .encrypted
- Actividad de red inusual
- Procesos sospechosos ejecutándose
- Archivos de keylog en el sistema

---

## 📞 Soporte y Contacto

Para preguntas sobre el uso educativo de este kit:
- Revisar la documentación incluida
- Consultar con expertos en seguridad
- Usar únicamente en entornos de laboratorio

---

**Recuerda: Este kit es para fines educativos únicamente. El uso malicioso es ilegal y está prohibido.**

