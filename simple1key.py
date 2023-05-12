# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key="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"

completion= openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[{
    "role": "user", "content": "History of c++"}])

print(completion.choices[0].message.content)