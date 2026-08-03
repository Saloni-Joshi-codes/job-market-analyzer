def search_by_skill(jobs, skill):
    result = jobs[jobs["Skills"].str.contains(skill, case=False)]

    if len(result) > 0:
        print(result)
    else:
        print("No jobs found!")