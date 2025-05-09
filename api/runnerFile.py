from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

if __name__=="__main__":
    completions = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
        
    )
    print(completions.choices[0].message)