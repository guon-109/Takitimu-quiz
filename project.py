score=0
quiz_data = [
    {"question": "Tākitimu was renowned as a highly ________ waka. A.sacred B. narrow C. fast D. heavy ", "answer": "A"}
    ]
for item in quiz_data:
    
    user_response = input(f"{item['question']} ")
    if user_response.strip().lower() == item['answer'].lower():
        print("Correct!")
        score += 1
