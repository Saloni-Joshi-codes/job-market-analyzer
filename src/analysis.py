def highest_salary(jobs):
    highest = jobs.loc[jobs["Salary"].idxmax()]

    print("\n===== Highest Salary Job =====")
    print(highest)