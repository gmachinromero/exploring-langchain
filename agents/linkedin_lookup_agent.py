import os

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """
    Given the full name: {person_full_name}.
    
    I want you to get it me a link to their Linkedin profile page.
    
    Your answer should contain only a URL, and you must ensure that the URL has
    a structure similar to: https://www.linkedin.com/in/<name>/.
    
    Where <name> is a nick of {person_full_name}.
    """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["person_full_name"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need get the Linkedin Page URL."
        )
    ]

    # Prompts developed by the LangChain community
    react_prompt = hub.pull("hwchase17/react")

    # Instantiate the agent
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    # Agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(person_full_name=name)}
    )

    linkedin_profile_url = result["output"]

    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Guillermo Machín Romero")
    print(linkedin_url)