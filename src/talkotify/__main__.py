from .env import init_env, checked_get

init_env()
OPENAI_API_KEY: str = checked_get("OPENAI_API_KEY")

def run():
    init_env()
    print("hoy!")

if __name__ == "__main__":
    run()