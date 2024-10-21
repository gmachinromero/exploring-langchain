from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:

    template = """
    Given the full name: {person_full_name}.
    
    I want you to get it me a link to their Linkedin profile page.
    
    Your answer should contain only a URL, and you must ensure that the URL has
    a structure similar to: https://www.linkedin.com/in/<name>/. Where <name>
    is a possible nick of {person_full_name}.
    
    Avoid these kind of structures: https://www.linkedin.com/pub/dir/.
    """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["person_full_name"]
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need get the Linkedin Page URL."
        )
    ]

    # Prompts developed by the LangChain community
    #react_prompt = hub.pull(
    #    owner_repo_commit="hwchase17/react",
    #    api_url="https://api.smith.langchain.com" # Change for US or Europe
    #)

    # Define a ReAct Prompt
    react_prompt = PromptTemplate.from_template(
        """Answer the following questions as best you can. You have access to the following tools:
    
        {tools}
    
        Use the following format:
    
        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question
    
        Begin!
    
        Question: {input}
        Thought: {agent_scratchpad}"""
    )



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
        handle_parsing_error=True,
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