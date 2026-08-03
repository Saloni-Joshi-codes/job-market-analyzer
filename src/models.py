class JobPosting:
    def __init__(self, title, company, location, salary, skills):
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.skills = skills

    def __str__(self):
        return (
            f"{self.title} | {self.company} | "
            f"{self.location} | ₹{self.salary} | {self.skills}"
        )