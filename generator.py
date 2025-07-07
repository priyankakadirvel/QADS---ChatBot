from transformers import pipeline

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(question, context):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = qa_pipeline(prompt, max_length=256)
    return response[0]['generated_text']
