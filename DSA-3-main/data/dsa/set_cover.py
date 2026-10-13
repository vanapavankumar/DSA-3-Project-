import json


def load_patents():
    with open("data/patents.json", "r", encoding="utf-8") as file:
        return json.load(file)


def set_cover(target_keywords, patents):
    uncovered = set(target_keywords)
    selected = []

    while uncovered:
        best_patent = None
        best_covered = set()

        for patent in patents:
            patent_keywords = set(patent["keywords"])
            covered = uncovered.intersection(patent_keywords)

            if len(covered) > len(best_covered):
                best_covered = covered
                best_patent = patent

        if best_patent is None or not best_covered:
            break

        selected.append(best_patent["patent_id"])
        uncovered -= best_covered

    return selected, uncovered


if __name__ == "__main__":
    patents = load_patents()

    target = patents[0]

    selected, uncovered = set_cover(
        target["keywords"],
        patents[1:]
    )

    print("SET COVER ANALYSIS")
    print("------------------")
    print("Target Patent:", target["patent_id"])
    print("Target Keywords:", target["keywords"])
    print("Selected Patents:", selected)
    print("Uncovered Keywords:", list(uncovered))
