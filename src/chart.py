import matplotlib.pyplot as plt

def salary_chart(jobs):
    top = jobs.head(10)

    plt.figure(figsize=(10,5))
    plt.bar(top["Company"], top["Salary"])
    plt.title("Top 10 Job Salaries")
    plt.xlabel("Company")
    plt.ylabel("Salary")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def skill_chart(jobs):
    skills = jobs["Skills"].str.split(",").explode()
    top_skills = skills.value_counts().head(10)

    plt.figure(figsize=(10,5))
    plt.bar(top_skills.index, top_skills.values)
    plt.title("Top 10 Skills")
    plt.xlabel("Skills")
    plt.ylabel("Number of Jobs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()