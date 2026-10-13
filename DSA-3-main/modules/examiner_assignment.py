import json


EXAMINERS = [
    {"name": "Dr. Rao", "expertise": "Artificial Intelligence", "workload": 2},
    {"name": "Dr. Sharma", "expertise": "Computer Vision", "workload": 4},
    {"name": "Dr. Khan", "expertise": "Deep Learning", "workload": 1},
    {"name": "Dr. Patel", "expertise": "Artificial Intelligence", "workload": 5}
]


def load_patents():
    with open("data/patents.json", "r", encoding="utf-8") as file:
        return json.load(file)


def assign_examiner(patent):
    suitable = []

    for examiner in EXAMINERS:
        if examiner["expertise"].lower() == patent["technology"].lower():
            suitable.append(examiner)

    if not suitable:
        return None

    suitable.sort(key=lambda x: x["workload"])

    return suitable[0]


if __name__ == "__main__":
    patents = load_patents()

    print("EXAMINER ASSIGNMENT")
    print("-------------------")

    for patent in patents:
        examiner = assign_examiner(patent)

        if examiner:
            print(
                patent["patent_id"],
                "->",
                examiner["name"],
                "| Expertise:",
                examiner["expertise"],
                "| Workload:",
                examiner["workload"]
            )
        else:
            print(patent["patent_id"], "-> No suitable examiner")
