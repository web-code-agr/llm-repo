import os
import chainlit as cl
from pschat_utils import ChatCompletion


@cl.on_message
async def main(message: str = "hello!"):
    answer = ChatCompletion().create(message=message).json()["data"]["messages"][-1]["content"]
    await cl.Message(content=answer).send()