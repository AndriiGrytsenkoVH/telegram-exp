import spacy
import re

# load the English language model
nlp = spacy.load('xx_ent_wiki_sm')

# define the raw text of the job posting
# raw_text = "We are looking for a Senior Software Engineer to join our team in San Francisco. The position requires at least 5 years of experience in Python, Java, and C++. The salary range is $100,000-$150,000 per year."
raw_text = "Data Scientist в GoPuff 📍US remote 💸$129 200-$205 275 в год + equity 💎От 3 лет опыта в DS 🚀Ко-фаундер – Рафаэль Илишаев GoPuff – сервис быстрой доставки еды и бытовых товаров в США и Европе. Размер команды – 1000+ | $3400M🔥 Узнать подробнее и откликнуться: тут Другие вакансии в GoPuff: – Product Manager – Principal Data Engineer – Full Stack Engineer #ml #gopuff"
# raw_text = re.sub(r'[/W]', "")
# process the raw text with Spacy
doc = nlp(raw_text)

# extract data from the processed text
# position = ""
# level = ""
# salary = ""
# location = ""
# description = ""
# tech_stack = ""
# experience = ""

# for ent in doc.ents:
#     if ent.label_ == "POSITION":
#         position = ent.text
#     elif ent.label_ == "LEVEL":
#         level = ent.text
#     elif ent.label_ == "SALARY":
#         salary = ent.text
#     elif ent.label_ == "GPE":
#         location = ent.text
#     elif ent.label_ == "DESCRIPTION":
#         description = ent.text
#     elif ent.label_ == "TECH_STACK":
#         tech_stack = ent.text
#     elif ent.label_ == "EXPERIENCE":
#         experience = ent.text

# print the extracted data
# print("Position:", position)
# print("Level:", level)
# print("Salary:", salary)
# print("Location:", location)
# print("Description:", description)
# print("Tech Stack:", tech_stack)
# print("Experience:", experience)

for ent in doc.ents:
    print(ent.text, '==>',ent.label_)
