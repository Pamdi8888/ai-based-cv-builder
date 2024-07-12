from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")

from ..config import Config
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def enhance_text(prompt, max_length=100, num_beams=5, early_stopping=True):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_beams=num_beams, early_stopping=early_stopping)
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text

# user_query = input("Enter your query: ")

# generated_text = enhance_text(user_query)

# print("Generated Text:", generated_text)

def get_mistral(user_message, model="mistral-large-latest", is_json=False):
        client = MistralClient(api_key=Config.MISTRAL_API_KEY)
        messages = [ChatMessage(role="user", content=user_message)]

        if is_json:
            chat_response = client.chat(
                model=model, messages=messages, response_format={"type": "json_object"}
            )
        else:
            chat_response = client.chat(model=model, messages=messages)

        return chat_response.choices[0].message.content