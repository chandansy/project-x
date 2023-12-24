import os
import openai
from openai import OpenAI
import configparser
from llm_api.prompts import MAIL_GEN_PROMPT, COMPANY_DETAILS_PROMPT
from llm_api.openai_utils import *


config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

# Adding API key
print(config['API_KEYS']['OPENAI_API_KEY'])

if "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" == str(config['API_KEYS']['OPENAI_API_KEY']):
    print("The retried api key is correct")
else:
    print("The retried api key is incorrect")
    print("correct key is ", type("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"))
    print("retieved key is ", type(config['API_KEYS']['OPENAI_API_KEY']))


client = OpenAI(api_key = str(config['API_KEYS']['OPENAI_API_KEY']))


# Setting up the prompt
SYSTEM_PROMPT = MAIL_GEN_PROMPT
chat_history = [{"role":"system", "content":SYSTEM_PROMPT}]


def set_system_prompt(NEW_PROMPT):
    global chat_history
    chat_history = [{"role": "system", "content": NEW_PROMPT}]



def fetch_openai_response(user_prompt: str):
    try:
        global chat_history
        chat_history.append({"role": "user", "content": user_prompt})
        
        print("waiting for response")

        MODEL_NAME = MODEL_GPT_35_TURBO

        openai_response = client.chat.completions.create(
            model = MODEL_NAME,
            messages = chat_history
        )

        reply = openai_response.choices[0].message.content
        completion_tokens = openai_response.usage.completion_tokens
        prompt_tokens = openai_response.usage.prompt_tokens
        total_tokens = openai_response.usage.total_tokens
        print("OpenAi Paid API reply: ", reply)
        print("completion_tokens", completion_tokens)
        print("prompt_tokens", prompt_tokens)
        print("total_tokens", total_tokens)
        total_cost = cost_calculator(MODEL_NAME, prompt_tokens, completion_tokens)
        print(f"Total cost: {total_cost:.4f} $ & {total_cost*83:.4f} rs")
        chat_history.append({"role": "assistant", "content": reply})
        print("wait over")
        return reply
    
    
    except Exception as e:
        print("Exception occurred while fetching response from openai", e)
        # Handle the exception and return a 500 status code
        error_message = f"An error occurred: {str(e)}"


