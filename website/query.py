# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")

# Define a function to generate text
def generate_text(prompt, max_length=100, num_beams=5, early_stopping=True):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_beams=num_beams, early_stopping=early_stopping)
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text

# Get user input
user_query = input("Enter your query: ")

# Generate text using the model
generated_text = generate_text(user_query)

# Print the generated text
print("Generated Text:", generated_text)
