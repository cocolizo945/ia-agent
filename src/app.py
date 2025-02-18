
from flask import Flask, request, jsonify, render_template
from decouple import config
import agent

app = Flask(__name__)

FB_ACCESS_TOKEN = config("FB_ACCESS_TOKEN")
FB_VERIFY_TOKEN = config("FB_VERIFY_TOKEN")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if verify_token == FB_VERIFY_TOKEN:
            return challenge
        return "Token inválido", 403
    elif request.method == "POST":
        data = request.get_json()
        for entry in data["entry"]:
            for event in entry["messaging"]:
                if "message" in event:
                    user_id = event["sender"]["id"]
                    respuesta = agent.procesar_mensaje_fb(event)
                    agent.enviar_mensaje_facebook(user_id, respuesta)
        return "OK", 200

# Página de chat web
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    datos = request.get_json()
    mensaje = datos.get("mensaje", "").lower()
    respuesta = agent.procesar_mensaje_fb({"message": {"text": mensaje}})
    return jsonify({"respuesta": respuesta})




@app.route("/bot", methods=["GET", "POST"])
def whatsapp_webhook():
    if request.method == "GET":
        return "WhatsApp Echo Bot is ready!"

    data = request.get_json()
    print(data)
    if data["event"] != "message":
        # We can't process other event yet
        return f"Unknown event {data['event']}"

    # Payload that we've got
    payload = data["payload"]
    # The text
    text = payload.get("body")
    if not text:
        # We can't process non-text messages yet
        print("No text in message")
        print(payload)
        return "OK"
    # Number in format 1231231231@c.us or @g.us for group
    chat_id = payload["from"]
    # Message ID - false_11111111111@c.us_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    message_id = payload['id']
    # IMPORTANT - Always send seen before sending new message
    respuesta = agent.procesar_mensaje_fb({"message": {"text": text}})

    agent.send_message(chat_id=chat_id, text=respuesta)

    # Send OK back
    return "OK"

# Iniciar servidor
def main():
      app.run(debug=True, host="0.0.0.0", port=85)

if __name__ == "__main__":
    main()
