import google.generativeai as genai
"pip install google.generativeai"
def Exam():
    genai.configure(api_key="AIzaSyBmLsm-Noz_3K8bTx0jFXkG0CesWR4wRic")
    model = genai.GenerativeModel('gemini-pro')

    
    chat = model.start_chat()
    
    while True:
        
        prompt = input("You: ")
        if prompt == "e":
            break
        response = chat.send_message(prompt)
        print(response.text)
        
      
        
        
        
 
    # response = model.generate_content(prompt)
    with open(f"responcetext.{type}",'w') as file:
        file.write(response.text)
    return response.text

Exam()