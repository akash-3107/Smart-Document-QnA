import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]  

def build_prompt(query, retrieved_chunks):
    context = ""
    for chunk in retrieved_chunks:
        context += f"(Page {chunk['page']}): {chunk['text']}\n"

    prompt = f"""
You are a helpful assistant.
Answer the question based only on the provided context.
If the answer is not available, say "Not available in the document."

Question: {query}
Context:
{context}
"""
    return prompt

def generate_answer(query, retrieved_chunks):
    prompt = build_prompt(query, retrieved_chunks)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # or gpt-4
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response["choices"][0]["message"]["content"]
