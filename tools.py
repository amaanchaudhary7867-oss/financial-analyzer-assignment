from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader

@tool("Financial Document Reader")
def read_data_tool(file_path: str) -> str:
    """
    Reads financial PDF and returns limited text to avoid token overflow
    """

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    full_text = ""

    for doc in docs[:5]:
        full_text += doc.page_content + "\n"

    return full_text