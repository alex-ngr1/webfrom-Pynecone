import pynecone as pc

class ProjcppConfig(pc.Config):
    pass

config = ProjcppConfig(
    app_name="ProjCpp",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
