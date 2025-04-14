import openai

# Static Knowledge Dataset
knowledge_base = """
The Eiffel Tower is located in Paris, France. 
It was completed in 1889 and stands 1,083 feet tall.
"""

# Query Function with Cached Context
def query_with_cag(context, query):
    prompt = f"Context:\n{context}\n\nQuery: {query}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant with expert knowledge."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        temperature=0.2
    )
    return response['choices'][0]['message']['content'].strip()

# Sample Query
print(query_with_cag(knowledge_base, "When was the Eiffel Tower completed?"))
