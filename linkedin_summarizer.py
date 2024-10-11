# Libraries
# ------------------------------------------------------------------------------
from typing import Tuple

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from agents.linkedin_lookup_agent import lookup as linkedin_look_agent
from third_party.linkedin import scrape_linkedin_profile

from output_parsers import Summary, summary_parser



# Code
# ------------------------------------------------------------------------------
def linkedin_summarizer(name: str) -> Tuple[Summary, str]:

    # Get LinkedIn Profile URL
    linkedin_username = linkedin_look_agent(name=name)

    # Get information about a LinkedIn Profile
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username,
        mock=True
    )

    # Template
    summary_template = """
        Given the following information {information} about a person, I want you to return:
        1. A brief summary
        2. Two interesting facts about the person
        
        The output must follow the following format {format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    # Instance LLM
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Instance Chain
    # chain = summary_prompt_template | llm | StrOutputParser()
    chain = summary_prompt_template | llm | summary_parser

    # Invoke Chain
    res:Summary = chain.invoke(input={"information": linkedin_data})

    print(res)
    print(linkedin_data.get("profile_pic_url"))

    return res, linkedin_data.get("profile_pic_url")



# Run
if __name__ == "__main__":
    print("LinkedIn Summarizer:")
    print(50*"_")
    linkedin_summarizer("Guillermo Machín Romero")


