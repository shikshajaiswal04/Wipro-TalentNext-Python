'''
1. Create a dictionary that contains a list of of people and one interesting fact about each of them. Display each person and his or her interesting fact to teh screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of peopleand facts. Run the program multiple times and noticeif the order changes.
'''

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane.",
}

for person, fact in people_facts.items():
    print(f"{person}: {fact}")


people_facts["Jeff"] = "Is afraid of heights."

people_facts["David"] = "Plays the piano."

people_facts["Jason"] = "Can fly an airplane."


for person, fact in people_facts.items():
    print(f"{person}: {fact}")


'''
2. Given the participants's score sheet for your University Sports Day, you are required to find teh runner-up score. You have scores. Store them in a list and find the score of the runner-up
'''
scores = [75, 80, 92, 86, 92, 70]

highest = max(scores)
scores_without_max = [score for score in scores if score != highest]
runner_up = max(scores_without_max)


print("Runner-up score is:", runner_up)


'''
3. You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary data type.
'''
student_records = {}

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    math = float(input("Enter Math marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))

    student_records[name] = {
        "Math": math,
        "Physics": physics,
        "Chemistry": chemistry
    }

print("\nStudent Records:")
for name, marks in student_records.items():
    print(f"{name} - Math: {marks['Math']}, Physics: {marks['Physics']}, Chemistry: {marks['Chemistry']}")

'''
4. Given a string of n words, help Alex to find out how mant times his name appears in the string.
'''
text = input("Enter a string of words: ")
text_lower = text.lower()
name_count = text_lower.split().count("alex")

print(name_count)
