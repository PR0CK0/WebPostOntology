import os
import requests
from bs4 import BeautifulSoup

from openai import OpenAI
openai.api_key = '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'

client = OpenAI()

scriptDir = os.path.dirname(os.path.abspath(__file__))
#ontology = os.path.join(scriptDir, 'wpo_v0.2.0-alpha.ttl')
terms = os.path.join(scriptDir, 'all_labels.txt')

file = client.files.create(
  file=open(terms, "rb"),
  purpose='assistants'
)

assistant = client.beta.assistants.create(
    name="John Byrne Classifier",
    instructions="You are a content classifier. You have two files. One is a Turtle file containing a taxonomy of terms. The other is a text file containing each of the taxonomy terms on a line. The Turtle file is better, because it is a large subclass hierarchy. When you are sent the content of some webpage, you should select 5 of the most appropriate owl:Class terms, using the skos:prefLabel for the string names. Essentially, you are picking the 5 best terms to categorize the webpage content under. Just provide the 5 terms as a list. Do not include any other information. DO NOT, ABSOLUTELY DO NOT, use terms that are not in the taxonomy given in the Turtle file. If you cannot pick 5 terms, just go with 2-3 that are in the taxonomy. I REPEAT, DO NOT USE, GENERATE OR CREATE NEW TERMS THAT ARE NOT IN THE TAXONOMY PROVIDED. VERIFY THAT THE TERMS YOU HAVE PICKED ARE IN THE TAXONOMY BY READING THE TERMS TEXT FILE. Your output should like like this, with nothing extra added: ```* Term 1\n* Term 2\n* Term 3\n* Term 4\n* Term 5```",
    tools=[{"type": "retrieval"}],
    model="gpt-3.5-turbo-1106",
    file_ids=[file.id]
)



htmlDump = ''
url = 'https://tampabayparenting.com/legoland-florida-annual-pass-flash-sale/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    htmlDump = soup.get_text()
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Classify the following post:\n" + htmlDump,
    }
  ]
)