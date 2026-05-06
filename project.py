score=0
#put all question in a list
quiz_data = [
    #1
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
    "A. Ngātoroirangi B. Ruawharo C. Tūtāmure D. Hoturapa ", "answer": "B"},
    #6
    {"question": "  According to tradition, which physical feature did "
     "Tākitimu turn into after arriving in Aotearoa? "
    "A. A large pā (fortress) B. A sacred lake "
    "C. A mountain range in Southland D. A giant kauri tree ", "answer": "C"},
    {"question": "Which of the following was strictly forbidden on Tākitimu "
    "during its voyage to maintain its sanctity?"
    "A. Women B. Cooked food C. Any form of metal D. Dogs", "answer": "B"},
    {"question": "What was the name of the sacred stone (mauri) placed on "
    "Tākitimu to protect the waka and its crew?"
    "A. Te Whatu o Tākitimu B. Hine-tākihia C. Te Puna o Te Ao D. "
    "Rangiātea ", "answer": "A"},
    {"question": "According to certain oral traditions, why did Tākitimu "
    "depart from Hawaiki? "
    "A. A sudden food shortage B. A dispute over sacred adzes and tapu violations "
    "C. To escape a great flood D. To follow the seasonal migration of birds ", "answer": "B"},
    {"question": "Which modern Māori iwi (tribe), alongside Ngāti Kahungunu, traces its primary "
    "ancestry back to Tākitimu through the priest Ruawharo?"
    "A. Ngāti Porou B. Ngāi Tūhoe C. Ngāti Raukawa D. Ngāti Rangitāne", "answer": "D"},
    ]
#using a for loop to collect user's answer and give feedback
for item in quiz_data:
    #print(item)
    user_input = input(f"{item['question']} ")
    while True:
        if user_input.strip().lower() in ['a', 'b', 'c', 'd']:
          user_input = True
          break
        else:
          print('Please enter with A, B C or D.')
      
    if user_input.strip().lower() == item['answer'].lower() :
        score += 1
        print("Correct!")
    else:
        print(f"Almost there! The correct answer is {item['answer']}.")
      
#print the result
if score == 0:
    print('Review it again before you try again. You can do it! Keep it up!')
elif score>0 and score<6:
    print('You got a lot of questions right. Review them and do them again, you will get a higher gread!')
elif score > 5 and score < 10:
    print('You got most of it right! Reviewing it will give you a much better result!')
else:
    print("You're a real expert! You got all the questions right!")