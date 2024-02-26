from flask import Flask,request
import pathlib
import textwrap
from flask_cors import CORS
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import json

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

app = Flask(__name__)
CORS(app)
genai.configure(api_key="AIzaSyDmAwQFPywA1zrNQQkBpfdOjL-1H0I_g_c")
# models/gemini-1.0-pro
# models/gemini-1.0-pro-001
# models/gemini-1.0-pro-latest
# models/gemini-1.0-pro-vision-latest
# models/gemini-pro
# models/gemini-pro-vision
model = genai.GenerativeModel('gemini-1.0-pro')

# paragraph = "India, a vibrant tapestry of culture and diversity, captivates with its rich history and dynamic present. Nestled in South Asia, it spans awe-inspiring landscapes from the majestic Himalayas to the sun-kissed beaches of Goa. Boasting a population that surpasses a billion, India is a melting pot of languages, religions, and traditions, harmoniously coexisting. Its ancient heritage, reflected in landmarks like the Taj Mahal, harmonizes with the hustle of modern cities like Mumbai and Bangalore. The country's cuisine is a sensory explosion, with spices dancing in every dish. India's influence extends globally, from Bollywood's cinematic allure to its prowess in technology."
json_result= """
"id":1,
"result":[{
"relevance":0.00,
"grammar":0.00,
"feedback":"enter feedback max 15 words"
}]
}
"""
# keywords="India,rich culture"

def generateResponse(paragraph,keywords):
   prompt = f"can you evaluate this \"{paragraph}\" and generate a grammar and relevancy score percentage , the paragraph's keywords are \"{keywords}\"'. Generate results in this format \"{json_result}\" "
   response = model.generate_content(prompt)
   print(response.text)
   return response

@app.route("/postResults", methods=['POST'])
def postResults():
    # print("hi",request.get_json())
    req=json.loads(request.data)
    paragraph=req['paragraph']
    keywords=req['keywords']
    res=generateResponse(paragraph,keywords)
    return res.text,200

if __name__ == '__main__':
    app.run(debug=True)