from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI


load_dotenv()

class Config:
    model = os.getenv("OPENAI_MODEL")
    llm = OpenAI(temperature=0)


cfg = Config()


if __name__ == "__main__":
    print("llm: ", cfg.llm)