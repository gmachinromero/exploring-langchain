# Libraries
# ------------------------------------------------------------------------------
from typing import List, Dict, Any

from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser



# Code
# ------------------------------------------------------------------------------
class Summary(BaseModel):
    """
    Represents a summary with interesting facts.

    This class defines the structure for storing a summary and a list of
    related interesting facts. It is used in conjunction with LangChain
    to process and structure language model outputs.

    Attributes:
        summary (str): The summary text.
        facts (List[str]): A list of interesting facts related to the summary.

    Methods:
        to_dict(): Converts the instance to a dictionary.
    """

    # Attributes
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts")

    # Methods
    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Summary instance to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary with 'summary' and 'facts' keys.
        """
        return {"summary": self.summary, "facts": self.facts}


summary_parser = PydanticOutputParser(pydantic_object=Summary)