
# Chatbot Multicanal agente de ia

Este proyecto es un **chatbot multicanal** que puede conectarse y operar en varias plataformas, incluyendo **WhatsApp** (mediante la API de Waha), **Facebook**, **Instagram** y una interfaz web construida con **Flask**. El chatbot está diseñado para interactuar con los usuarios de manera eficiente y sencilla en estos diferentes canales. El proyecto está **dockerizado** para una fácil configuración y despliegue.

## Tecnologías utilizadas

- **Python**: Lenguaje principal para el desarrollo del chatbot.
- **Flask**: Framework web para levantar el entorno web.
- **Waha API**: Para la integración con WhatsApp.
- **Facebook Graph API**: Para integrar el chatbot en Facebook.
- **Instagram Graph API**: Para integración con Instagram.
- **Docker**: Para contenerizar la aplicación y facilitar su despliegue.

## Características

- **Interacción Multicanal**: El chatbot puede recibir y responder mensajes desde WhatsApp, Facebook, Instagram y una interfaz web.
- **Flask Web Interface**: Levanta un servidor web con Flask para proporcionar acceso adicional al chatbot.
- **Dockerizado**: Todo el proyecto está dockerizado, lo que facilita su despliegue en cualquier entorno.
- **Escalabilidad**: El sistema puede extenderse fácilmente para incluir otros canales de comunicación en el futuro.

## Requisitos previos

Antes de comenzar, asegúrate de tener las siguientes herramientas instaladas:

- **Docker**: Asegúrate de tener Docker instalado en tu máquina. Si no lo tienes, puedes seguir las instrucciones de instalación desde [aquí](https://www.docker.com/get-started).
- **Docker Compose**: Para gestionar los contenedores y redes de manera fácil. Si no lo tienes, puedes instalarlo siguiendo las instrucciones [aquí](https://docs.docker.com/compose/install/).
- **Credenciales de API** de Waha, Facebook y Instagram para integrar sus respectivas APIs.

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/cocolizo945/ia-agent.git
   cd ia-agent
   ```

2. **Configurar las credenciales de las APIs**:

   Asegúrate de configurar las credenciales de las APIs de Waha, Facebook y Instagram en los archivos correspondientes (`.env`, etc.).

3. **Configurar funcionamiento**:
    sientete libre de modificar la funcion [generar_comparacion_ia](https://github.com/cocolizo945/ia-agent/blob/master/src/agent.py#L14) para que tu chatbot tenga la informacion que requiera y asi pueda responderte de forma coherente a tus necesidades.

4. **Construir y levantar los contenedores Docker**:

   Ejecuta el siguiente comando para construir la imagen Docker y levantar los contenedores:

   ```bash
   docker-compose up --build
   ```

   Este comando construirá la imagen de Docker y levantará los contenedores necesarios para ejecutar la aplicación, incluyendo el servidor web Flask.

5. **Acceder al chatbot**:

   Una vez que los contenedores estén corriendo, puedes acceder al chatbot a través de los siguientes canales:
   
   - **Web**: Abre tu navegador y dirígete a `http://localhost:1400` para interactuar con el chatbot en la interfaz web.
   - **WhatsApp**: Envía un mensaje al número de WhatsApp vinculado con la API de Waha.
   - **Facebook/Instagram**: Los mensajes enviados a la página de Facebook o perfil de Instagram conectados al chatbot recibirán respuestas automáticas.

## Uso

- **WhatsApp**: Envía un mensaje a tu número de WhatsApp vinculado con la API de Waha para interactuar con el chatbot.
- **Facebook/Instagram**: Los mensajes enviados a la página de Facebook o perfil de Instagram conectados al chatbot recibirán respuestas automáticas.
- **Web**: Accede a la interfaz web en `http://localhost:1400/` para interactuar directamente con el chatbot.

