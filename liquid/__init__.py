from aqua import Aqua

aqua_instance = Aqua(
    {
        "type": "user",
        "user": os.environ.get("AQUA_USER"),
        "password": os.environ.get("AQUA_PASS"),
        "url": os.environ.get("AQUA_URL"),
        "ssl_verify": os.environ.get("AQUA_SSL_VERIFY"),
    }
)

client = aqua_instance.client("cwp")
client.create_image_assurance_policy()
