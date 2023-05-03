import pynecone as pc

config = pc.Config(
    app_name="pc_chat_gpt",
    port=3000,
    app_name="app",
    api_url="0.0.0.0:8000",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
)
