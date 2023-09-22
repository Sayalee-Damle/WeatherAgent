from langchain.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent,initialize_agent, AgentType
from langchain.llms import OpenAI
import templates
from config import Config
import weather_agent 

wrapper = DuckDuckGoSearchAPIWrapper()
search = DuckDuckGoSearchRun(api_wrapper=wrapper)

tools = [
    Tool(
        name="Weather",
        func=search.run,
        description="useful for when you need to see the current weather for a place",
        
    ),
]

loc = weather_agent.location()
ques = weather_agent.weather_loc(loc)
print(ques)


agent_chain = initialize_agent(
    tools=tools, llm=Config.llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, max_iterations = 3
)
#agent_chain = initialize_agent(tools, llm=Config.llm, verbose=True, agent_path= "./weather_agent/weather_agent.json")
agent_chain.run(ques)

#agent_chain.run("check whether temperature is being shown")