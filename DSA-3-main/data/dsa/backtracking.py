import json


def load_patents():
    with open("data/patents.json", "r", encoding="utf-8") as file:
        return json.load(file)


def find_covers(target_keywords, patents):
    solutions = []

    def backtrack(index, selected, covered):
        if covered >= target_keywords:
            solutions.append(selected.copy())
            return

        if index == len(patents):
            return

        patent = patents[index]
        patent_keywords = set(patent["keywords"])

        # Include current patent
        backtrack(
            index + 1,
            selected + [patent["patent_id"]],
            covered | patent_keywords
        )

        # Exclude current patent
        backtrack(
            index + 1,
            selected,
            covered
        )

    backtrack(0, [], set())

    return solutions


if __name__ == "__main__":
    patents = load_patents()

    target = patents[0]
    target_keywords = set(target["keywords"])

    solutions = find_covers(
        target_keywords,
        patents[1:]
    )

    print("BACKTRACKING ANALYSIS")
    print("---------------------")
    print("Target Patent:", target["patent_id"])
    print("Target Keywords:", target["keywords"])
    print()

    if solutions:
        solutions.sort(key=len)

        print("Possible Cover Sets:")

        for solution in solutions:
            print(solution)

        print()
        print("Minimum Cover:", solutions[0])
    else:
        print("No complete cover found.")
