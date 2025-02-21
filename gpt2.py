from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')  # Load a pre-trained language model

prompt = "Your prompt"
result = generator(prompt, max_length=100)
print(result[0]['generated_text'])
