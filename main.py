from src.loader import load_jobs
from src.search import search_by_skill
from src.chart import salary_chart, skill_chart
from src.analysis import highest_salary 

jobs = load_jobs()

while True:
    print("\n===== JOB MARKET ANALYZER =====")
    print("1. Show Total Jobs")
    print("2. Search Jobs by Skill")
    print("3. Salary Chart")
    print("4. Top Skills Chart")
    print("5. Highest Salary Job")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nTotal Jobs:", len(jobs))

    elif choice == "2":
        skill = input("Enter Skill: ")
        search_by_skill(jobs, skill)

    elif choice == "3":
        salary_chart(jobs)

    elif choice == "4":
        skill_chart(jobs)

    elif choice == "5":
        highest_salary(jobs)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")