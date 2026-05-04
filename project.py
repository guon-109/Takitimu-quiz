score=0
#put all question in a list
quiz_data = [
    {"question": "Tākitimu was renowned as a highly ________ waka. "
    "A.sacred B. narrow C. fast D. heavy ", "answer": "A"},
    {"question": "Only ________ were permitted to travel aboard this waka. "
    "A.women B.food C. specific chiefs and priests D. cooked food", "answer": "C"},
    {"question": "The sacredness of Te Awhiorangi"
    " (the famous adze associated with Tākitimu) was such that it "
    "was never used for ________."
    "A. ceremonial purposes B. utilitarian purposes C. religious tasks "
    "D. carving new waka ", "answer": "B"},
    {"question": "Tākitimu was taken to the great waters "
    "of ________ to test the seaworthiness of the vessel."
    "A. Piko-piko-i-whiti B. Lake Wairarapa C. Hawaiki "
    "D. Te Moana-nui-a-Kiwa", "answer": "A"},
    {"question": "Which high priest (tohunga) was said to have carried "
    "the sacred knowledge (whare wānanga) aboard Tākitimu? "
    "A.sacred B. narrow C. fast D. heavy ", "answer": "A"},
    ]
#using a for loop to collect user's answer
for item in quiz_data:
    user_input = input(f"{item['question']} ")
    if user_input.strip().lower() == item['answer'].lower():
        score += 1
        print("Correct!")
    else:
        print(f"Almost there! The correct answer was {item['answer']}.")