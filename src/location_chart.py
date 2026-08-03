import matplotlib.pyplot as plt

def location_chart(jobs):
    locations = jobs["Location"].value_counts().head(10)

    plt.figure(figsize=(8,5))
    plt.bar(locations.index, locations.values)
    plt.title("Top Job Locations")
    plt.xlabel("Location")
    plt.ylabel("Number of Jobs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()