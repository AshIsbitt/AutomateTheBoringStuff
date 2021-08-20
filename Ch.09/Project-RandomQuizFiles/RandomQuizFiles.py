#Project - Random quiz files

#Create 35 different quizzes with questions and answers in random order along with the answer key

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
	#Create files
	quizFile = open(f'capitalsquiz{quizNum+1}.txt', 'w')
	answerKeyFile = open(f'capitalsQuiz_answers{quizNum+1}.txt', 'w')

	#Write out headers
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' '*20) + f'State Capitals Quiz (form. {quizNum+1})')
	quizFile.write('\n\n')

	#Shuffle order of quiz
	states = list(capitals.keys())
	random.shuffle(states)

	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]]
		wrongAsnwers = list(capitals.values())
		del wrongAsnwers[wrongAsnwers.index(correctAnswer)]

		wrongAsnwers = random.sample(wrongAsnwers, 3)
		answerOptions = wrongAsnwers + [correctAnswer]

		random.shuffle(answerOptions)

		quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

		for i in range(4):
			quizFile.write(f"      {'ABCD'[i]}. { answerOptions[i]}\n")
			quizFile.write("\n")

		answerKeyFile.write(f"{questionNum+1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
		answerKeyFile.write("\n")

quizFile.close()
answerKeyFile.close()