import pynecone as pc

config = pc.Config(
    app_name="pc_chat_gpt",
    port=3000,
    api_url="0.0.0.0:8000",
    db_url="sqlite:///pynecone.db",
)
