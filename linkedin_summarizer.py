# Libraries
# ------------------------------------------------------------------------------
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from third_party.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_look_agent


# Code
# ------------------------------------------------------------------------------
def linkedin_summarizer(name: str) -> str:

    # Get LinkedIn Profile URL
    linkedin_username = linkedin_look_agent(name=name)

    # Get information about LinkedIn Profile
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username,
        mock=True
    )

    # Template
    summary_template = """
        Given the following information {information} about a person, I want you to return:
        1. A brief summary
        2. Two interesting facts about the person
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # LLM
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Chain
    chain = summary_prompt_template | llm | StrOutputParser()

    # Invoke Chain
    res = chain.invoke(input={"information": linkedin_data})

    print(res)



# Run
if __name__ == "__main__":
    print("LinkedIn Summarizer:")
    print(50*"_")
    linkedin_summarizer("Guillermo Machín Romero")


