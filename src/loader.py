import pandas as pd

def load_jobs():
    try:
        jobs = pd.read_csv("data/jobs.csv")
        return jobs
    except FileNotFoundError:
        print("Error: jobs.csv not found!")
        return pd.DataFrame()
    except Exception as e:
        print("Something went wrong:", e)
        return pd.DataFrame()