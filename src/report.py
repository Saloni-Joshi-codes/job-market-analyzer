def generate_report(jobs):
    with open("output/report.txt", "w") as file:
        file.write("===== JOB MARKET REPORT =====\n\n")
        file.write(f"Total Jobs: {len(jobs)}\n\n")

        file.write("Top 10 Jobs:\n")
        file.write("-" * 60 + "\n")

        for index, row in jobs.head(10).iterrows():
            file.write(
                f"{row['Job Title']} | "
                f"{row['Company']} | "
                f"{row['Location']} | "
                f"{row['Salary']}\n"
            )

    print("Report generated successfully!")