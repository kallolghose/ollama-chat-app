import ollama

def fetch_response(q=""):
    response = ollama.chat(model='llama3', messages=[{
        'role':'user',
        'content': q
    }])
    return response['message']['content']


if __name__=="__main__":
    question = input("What do you want to ask the chatbot: ")
    print('Response from Ollama : ', fetch_response(question))