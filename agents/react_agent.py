from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description
from langchain_openai import ChatOpenAI

load_dotenv()

from langchain.agents import tool


@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    text = text.strip("'\n").strip('"')
    return len(text)


if __name__ == "__main__":
    print("Hello ReAct LangChain!")

    tools = [get_text_length]
    tool_names = ", ".join([tool.name for tool in tools])

    template = """
    Answer the following questions as best you can. You have access to the following tools: {tools}

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
    Thought:
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=tool_names
    )

    llm = ChatOpenAI(
        temperature=0,
        stop=["\nObservation"]
    )