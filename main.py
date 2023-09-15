import os
from dotenv import load_dotenv
import chainlit as cl
from langchain.llms import AzureOpenAI
from langchain import PromptTemplate, LLMChain

load_dotenv()



@cl.on_chat_start
def main():
    llm = AzureOpenAI(
        deployment_name=os.getenv("DEPLOYMENT_NAME"),
        model_name=os.getenv("MODEL_NAME"),
        streaming=True
    )
    template="""Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(
        prompt=prompt,
        llm=llm,
        verbose=True,
    )
    cl.user_session.set("llm_chain",llm_chain)


@cl.on_message
async def main(message: str):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(message, callbacks = [cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()