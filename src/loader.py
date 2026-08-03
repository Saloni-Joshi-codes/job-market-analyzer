import pandas as pd

def load_jobs():
    jobs = pd.read_csv("data/jobs.csv")
    return jobs