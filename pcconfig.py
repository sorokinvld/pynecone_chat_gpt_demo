import pynecone as pc

config = pc.Config(
    app_name="pc_chat_gpt",
    port=8000,
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
