import pynecone as pc

config = pc.Config(
    app_name="pc_chat_gpt",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
