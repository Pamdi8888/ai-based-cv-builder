# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#
# tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
# model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")

# from ..config import Config
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
# from template import query_template


# def enhance_text(prompt, max_length=100, num_beams=5, early_stopping=True):
#     input_ids = tokenizer.encode(prompt, return_tensors='pt')
#     output = model.generate(input_ids, max_length=max_length, num_beams=num_beams, early_stopping=early_stopping)
#     text = tokenizer.decode(output[0], skip_special_tokens=True)
#     return text


# user_query = input("Enter your query: ")

# generated_text = enhance_text(user_query)

# print("Generated Text:", generated_text)

def get_mistral(user_message, model="mistral-large-latest", is_json=False):
    # client = MistralClient(api_key=Config.MISTRAL_API_KEY)
    client = MistralClient(api_key="PejOUYV6i8evvlfEWpWF3JUvk1CnrYZi")
    messages = [ChatMessage(role="user", content=user_message)]

    if is_json:
        chat_response = client.chat(
            model=model, messages=messages, response_format={"type": "json_object"}
        )
    else:
        chat_response = client.chat(model=model, messages=messages)

    return chat_response.choices[0].message.content

# sample = {'full_name': 'Param Gandhi', 'date_of_birth': '2004-04-26', 'mail': 'paramagandhi@gmail.com', 'marital_status': '', 'hobbies': '', 'dream_sector1': 'Research', 'dream_sector2': 'Software Engineer', 'career_plans': 'Interested in doing research in the field of AI', 'additional_info': 'Experienced in Coding in Python ', 'minor_course_details': 'No Minor Course', 'skills': 'Python, Java, C++, AIML, Deep Learning', 'transaction_id': '', 'prof_summary': "I am currently doing an internship in Greatwall Technologies. I am developing an AI application that  builds CV's.", 'languages': [{'language': 'Python', 'proficiency': 'Expert'}, {'language': 'Java', 'proficiency': 'Expert'}, {'language': 'C/C++', 'proficiency': 'Expert'}, {'language': 'Scratch', 'proficiency': 'Expert'}, {'language': 'English', 'proficiency': 'Fluent'}, {'language': 'Marathi', 'proficiency': 'Native'}, {'language': 'Hindi', 'proficiency': 'Native'}, {'language': 'German', 'proficiency': 'Intermidiate'}], 'education': [{'grade_year': '', 'grad_year': 2020, 'percentage_cgpa': '100%', 'specialization': '10th', 'institution': 'Maharashtra State Board of Secondary Education'}, {'grade_year': '', 'grad_year': 2022, 'percentage_cgpa': '100%', 'specialization': '12th - PCM', 'institution': 'Maharashtra State Board of Higher Education'}, {'grade_year': '', 'grad_year': 2026, 'percentage_cgpa': '10', 'specialization': 'Computer Science', 'institution': 'BITS Goa'}], 'projects': [{'title': 'Web Trained Chatbot', 'domain': 'Machine Learning & Large Language Models', 'duration': 'Oct 2023 - Oct 2023', 'description': "Made an AI Chatbot that is trained and finetuned on data scraped from a website\nWeb Scraping a website from sitemap.xml\nGenerated Vector Embeddings using all-mpnet-base-v2 and storing in FAISS Vector Storage Database\nUsed Keyword Based Search for processing queries\nUsed Mistral AI's LLM locally to generate intelligent answers based on queries and search results", 'url': 'www.github.com'}, {'title': 'Course Allocation Using Maximum Bipartite Matching', 'domain': 'Graph Optimization', 'duration': 'Aug 2023 - Nov 2023', 'description': 'Course Allocation for Professors using Maximum Unweighted Bipartite Matching according to Professor Preferences\nGraph Optimization using Enumerating Maximum Matchings Algorithm (EMMA) and NetworkX library in Python\nConverted a Many-Many Weighted Bipartite Matching Problem to One-One Maximum Unweighted Bipartite Matching Problem', 'url': 'www.github.com'}], 'social_accounts': [{'name': 'Instagram', 'url': 'www.instagram.com'}], 'work_experience': [{'role': 'Intern Developer', 'cause': '', 'description': 'Developed a AI-based CV Builder\nWorked on AI application, Backend using Flask, Dynamic HTML templating using Jinja2', 'organization': 'Greatwall Technologies'}], 'internships': [{'role': '', 'cause': '', 'description': '', 'organization': ''}], 'volunteer_activities': [{'role': 'Beach Cleaning', 'cause': '', 'description': 'Went for a Beach Cleaning Drive along with Nirmaan club of BITS Goa', 'organization': 'Nirmaan, BITS Goa'}], 'accomplishments': [{'name': 'Won XYZ Award', 'description': '', 'date': '2024-07-24', 'organization': 'ABC organization'}], 'positions_of_responsibility': [{'role': 'Chief Coordinator', 'cause': '', 'description': 'Conducted multiple treks with over 50 people successfully', 'organization': 'Trekking Club, BITS Goa'}], 'extra_curriculars': [{'name': 'Trekking', 'category': 'Sports', 'description': ''}, {'name': 'Swimming', 'category': 'Sports', 'description': ''}, {'name': 'Piano', 'category': 'Arts/Music', 'description': ''}, {'name': 'Capture the FLag (CTF) Competitions', 'category': 'Cybersecurity', 'description': "Participated in many Capture The Flag competitions which consist of Cybersecurity Challenges\nProficient in solving challenges belonging to the categories of Cryptography, Forensics, Open Source Intelligence, Steganography,\nReverse Engineering, and Binary Exploitation\nActive member of my college's Cybersecurity & Ethical Hacking club: BITSkrieg (Country Rank: 1, International Rank: 27)"}], 'certifications': [{'name': 'Goethe-Zertifikat A2', 'date': '', 'organization': 'Goethe Institute'}, {'name': 'Goethe-Zertifikat A1 ', 'date': '', 'organization': 'Goethe Institute'}], 'competitions': [{'name': '', 'date': '', 'position': '', 'organization': ''}], 'conferences_workshops': [{'name': '', 'date': '', 'description': '', 'organization': ''}], 'test_scores': [{'name': 'BITSAT', 'date': '', 'score': '287/390'}], 'patents_publications': [{'name': '', 'date': '', 'description': '', 'organization': ''}], 'scholarships': [{'name': 'Scholarship for Youth Course in Germany', 'date': '2019-05-05', 'description': 'Won schloarship to attend Geraman Language (B1) Youth Course in Germany (Jugendkurse in Deutschland)\nGot selected for this schloarship after Very Good (Sehr Gut) rating in A1 exam and 2 rounds of interviews in German', 'organization': 'Goethe Institute & PASCH'}], 'photograph': ''}
#
# formatted_query = query_template.template.format(query=sample)

# print(get_mistral(str(formatted_query)))