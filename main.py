import os
import argparse
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from embedding_function import get_embedding_function

load_dotenv()

CHROMA_PATH = os.getenv('CHROMA_PATH')

PROMPT_TEMPLATE = """
### CONTEXT:
{context}
### INSTRUCTIONS:
You need to answer the question provided in the below based on the above context.
{question}.

do not provide a preamble.

### RESPONSE (NO PREAMBLE):
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_string", type=str, help="Type in your question")
    args = parser.parse_args()
    query = args.query_string
    get_answer = contextual_llm(query)
    print(get_answer)

def contextual_llm(query: str):
    db = Chroma(
            persist_directory=CHROMA_PATH, 
            embedding_function=get_embedding_function()
        )

    query_results = db.similarity_search_with_score(query, k=5)

    context_text = "\n\n======================\n\n".join([doc.page_content for doc, _score in query_results])

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)

    model = OllamaLLM(model="mistral")
    response = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in query_results]
    formatted_response = f"Answer: {response}\n\Context sources: {sources}"
    return formatted_response


if __name__ == "__main__":
    main()
