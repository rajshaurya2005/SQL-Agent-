from langchain.agents import create_react_agent, AgentExecutor, tool
from llm import llm
from prompt import prompt_template
from db import execute_query

@tool
def mysql_database_tool(query):
    """Use this tool to execute queries against the mysql database and retrieve data if needed"""
    return execute_query(query)

tools = [mysql_database_tool]

agent = create_react_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def invoke_agent(query):
    return agent_executor.invoke({"input": query})
