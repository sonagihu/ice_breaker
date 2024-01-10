from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_community.llms import OpenAI

llm = OpenAI(temperature=0)

tool_names = ["serpapi"]
tools = load_tools(tool_names)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run("한국 대통령은 누구?")
