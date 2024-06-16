from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")


def enhance_text(prompt, max_length=100, num_beams=5, early_stopping=True):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_beams=num_beams, early_stopping=early_stopping)
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text

# user_query = input("Enter your query: ")

# generated_text = enhance_text(user_query)

# print("Generated Text:", generated_text)
