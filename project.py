score=0
#put all questions in a list
quiz_data = [
    #1
    {"question": "Tākitimu was renowned as a highly ________ waka.\n"
    "A.sacred \nB.narrow \nC.fast \nD.heavy",
    'guide':'Please enter your '
    'answer with A, B, C or D below.\n', "answer": "A"}, 

    {"question": "Only ________ were permitted to travel aboard this waka.\n"
    "A.women \nB.food \nC.specific chiefs and priests \nD.cooked food", 
    'guide':'Please enter your '
    'answer with A, B, C or D below.\n', "answer": "C"},

    {"question": "The sacredness of Te Awhiorangi"
    " (the famous adze associated with Tākitimu) was such that it "
    "was never used for ________.\n"
    "A.ceremonial purposes \nB.utilitarian purposes \nC.religious tasks \n"
    "D.carving new waka ", 'guide':'Please enter your '
    'answer with A, B, C or D below.\n', "answer": "B"},

    {"question": "Tākitimu was taken to the great waters "
    "of ________ to test the seaworthiness of the vessel.\n"
    "A.Piko-piko-i-whiti \nB.Lake Wairarapa \nC.Hawaiki \n"
    "D.Te Moana-nui-a-Kiwa", 'guide':'Please enter your '
    'answer with A, B, C or D below.\n', "answer": "A"},

    {"question": "Which high priest (tohunga) was said to have carried "
    "the sacred knowledge (whare wānanga) aboard Tākitimu?\n"
    "A.Ngātoroirangi \nB.Ruawharo \nC.Tūtāmure \nD.Hoturapa",
    'guide':'Please enter your '
    'answer with A, B, C or D below.\n', "answer": "B"},
    #6
    {"question": "According to tradition, which physical feature did "
     "Tākitimu turn into after arriving in Aotearoa? \n"
    "A.A large pā (fortress) \nB.A sacred lake \n"
    "C.A mountain range in Southland \nD.A giant kauri tree ", 
    'guide':'Please enter your '
    'answer with A, B, C or D below.\n',"answer": "C"},

    {"question": "Which of the following was strictly forbidden on Tākitimu "
    "during its voyage to maintain its sanctity?\n"
    "A.Women \nB.Cooked food \nC.Any form of metal \nD.Dogs",
    'guide':'Please enter your '
    'answer with A, B, C or D below.\n', "answer": "B"},

    {"question": "What was the name of the sacred stone (mauri) placed on "
    "Tākitimu to protect the waka and its crew?\n"
    "A.Te Whatu o Tākitimu \nB.Hine-tākihia \nC.Te Puna o Te Ao \nD."
    "Rangiātea ",'guide':'Please enter your '
    'answer with A, B, C or D below.\n', "answer": "A"},

    {"question": "According to certain oral traditions, why did Tākitimu "
    "depart from Hawaiki? \n"
    "A.A sudden food shortage \nB.A dispute over sacred adzes and tapu violations \n"
    "C.To escape a great flood \nD.To follow the seasonal migration of birds ", 
    'guide':'Please enter your '
    'answer with A, B, C or D below.\n',"answer": "B"},

    {"question": "Which modern Māori iwi (tribe), alongside Ngāti Kahungunu, traces its primary "
    "ancestry back to Tākitimu through the priest Ruawharo?\n"
    "A.Ngāti Porou \nB.Ngāi Tūhoe \nC.Ngāti Raukawa \nD.Ngāti Rangitāne", 
    'guide':'Please enter your '
    'answer with A, B, C or D below.\n',"answer": "D"},
    ]
#Using a for loop to collect user's answers.
for item in quiz_data: 
    while True:
        user_input = input(f"{item['question']}\n{item['guide']} ")
#Checking if the answers are in a,b,c or d.
        if user_input.strip().lower() in ['a', 'b', 'c', 'd']:
            break
        else:
          print('Please enter with A, B C or D.')
          print()
#Determine if the answer is correct and accumulate the score.
    if user_input.strip().lower() == item['answer'].lower():
        score += 1
        print("Correct!")
        print()
    else:
        print(f"Almost there! The correct answer is {item['answer']}.")
        print()
print('Congratulations on completing this!')
#print the result
print(f'Your score is {score} out of 10.') 
if score == 0: 
    print('Review it again before you try again. You can do it! Keep it up!')
elif score > 0 and score < 6:
    print('Review them and do them again, you will get a higher gread!')
elif score < 10:
    print('You got most of it right! Reviewing it will give you a much better result!')
else:
    print("You're a real expert! You got all the questions right!")