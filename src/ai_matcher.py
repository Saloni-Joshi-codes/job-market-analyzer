def ai_matcher(jobs):
    try:
        with open("src/sample_cv.txt", "r") as file:
            cv = file.read().lower()

        print("\n===== AI RESUME MATCHER =====")

        job_no = int(input("Enter Job Number (1-220): "))
        job = jobs.iloc[job_no - 1]

        job_skills = [skill.strip().lower() for skill in job["Skills"].split(",")]

        matched = []
        missing = []

        for skill in job_skills:
            if skill in cv:
                matched.append(skill)
            else:
                missing.append(skill)

        score = int((len(matched) / len(job_skills)) * 100)

        print(f"\nMatch Score: {score}%")

        print("\nMatching Skills:")
        for skill in matched:
            print("✓", skill)

        print("\nMissing Skills:")
        for skill in missing:
            print("✗", skill)

        print("\nResume Suggestions:")
        print("• Mention your Python projects.")
        print("• Add GitHub repository link.")
        print("• Highlight Machine Learning and SQL skills.")

    except FileNotFoundError:
        print("sample_cv.txt not found.")