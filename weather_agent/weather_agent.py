from typing import List, Tuple, Any, Union
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
import templates



def location():
    loc = input("Enter the location for which you want to know the Weather: ")
    return loc

def weather_loc(loc):
    query = "What is the current temperaure and weather(Sunny/Rainy/Windy) in  "+ loc + " today?"
    return query

weather_agent = [{
  "load_from_llm_and_tools": True,
  "_type": "conversational-react-description",
  "prefix": "Assistant is a large language model trained for forecasting weather.\n\nAssistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives.\nAssistant should only obtain knowledge and take actions from using tools and never on your own.\nTOOLS:\n------\n\nAssistant has access to the following tools: ",
  "suffix": "Please make decisions based on the following policy: \n- If the user is asking for a weather forecast use the Weather Forecast tool\n- If the user does not provide a location, ask before checking for weather\n- Apologize if the user is angry or showing frustration\n- Answer with a friendly and professional tone.\n- Always end a response with a follow up question like 'what else can i help you with?', unless the user shows gratitude.",
  "ai_prefix": "AI Agent",
  "human_prefix": "Human"
}]