from Service.CreateDocFromPDF import CreateDoc
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
import os

api_key=os.getenv("OPENAI_API_KEY")

def custom_summary(filename, custom_prompt, chain_type, num_summaries):
    docs = CreateDoc(filename)
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key)
    chain_type = "map_reduce"
    custom_prompt = custom_prompt + """: \n {text}"""

    combine_prompt = PromptTemplate(
        template=custom_prompt, input_variables=["text"]
    )

    map_prompt = PromptTemplate(
        template="Summarize:\n{text}", input_variables=["text"]
    )

    if chain_type == "map_reduce":
        chain = load_summarize_chain(llm, chain_type=chain_type,
                                     map_prompt=map_prompt,
                                     combine_prompt=combine_prompt)
    else:
        chain = load_summarize_chain(llm, chain_type=chain_type)
    
    for i in range(num_summaries):
        summary_output = chain({"input_documents": docs}, return_only_outputs=True)['output_text']
        yield summary_output