questions = [
    [
        "What is the capital city of France?", "Berlin", "Madrid", "Paris", "Rome", 3
    ],
    [
        "Who is known as the 'Father of the Nation' in India?", "Jawaharlal Nehru", "Bhagat Singh", "Subhas Chandra Bose", "Mahatma Gandhi", 4
    ],
    [
        "Which planet is known as the Red Planet?",
        "Earth", "Mars", "Jupiter", "Venus", 2
    ],
    [
        "What is the largest mammal in the world?",
        "Elephant", "Blue Whale", "Giraffe", "Rhinoceros", 2
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?",
        "William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen",
        1
    ],
    [
        "Which element has the chemical symbol 'O'?",
        "Gold", "Oxygen", "Osmium", "Oganesson",
        2
    ],
    [
        "What is the main ingredient in traditional Japanese miso soup?",
        "Miso paste", "Soy sauce", "Rice", "Seaweed", 1
    ],
    [
        "Which Indian cricketer is known as the 'God of Cricket'?",
        "Virat Kohli", "MS Dhoni", "Sachin Tendulkar", "Rahul Dravid", 3
    ],
    [
        "What is the smallest prime number?",
        "1", "2", "3", "5", 2
    ],
    [
        "Which festival is also known as the Festival of Lights?",
        "Holi", "Diwali", "Eid", "Christmas", 2
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")
