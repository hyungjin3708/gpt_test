import openai
import streamlit as st

openai.api_key = "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"

def BasicGeneration(userPrompt):
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  #prompt="Correct this to standard English:\n\nShe no went to the market.",
  messages = [
    {"role": "user", "content": userPrompt}
  ],
  max_tokens=1000
  )
  return completion.choices[0].message.content

#prompt = "Follow the rules and write an email encouraging me to buy an electric car Rule 1. Emphasize that there is only one chance Rule 2: Give one or the other Rule 3: Give lots of examples"
#response = BasicGeneration(prompt)
#print(response)

st.title("ChatGPT TEST")
user_input = st.text_input("Enter some text:")
response = BasicGeneration(user_input)
st.write("You entered:", response)