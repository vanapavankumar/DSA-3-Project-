import json
import re


def get_words(text):
    return set(re.findall(r'\b[a-zA-Z]+\b', text.lower()))


def jaccard_similarity(claim1, claim2):
    words1 = get_words(claim1)
    words2 = get_words(claim2)

    intersection = words1.intersection(words2)
    union = words1.union(words2)

    if not union:
        return 0

    return len(intersection) / len(union)


def load_patents():
    with open("data/patents.json", "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    patents = load_patents()

    target = patents[0]

    print("TARGET PATENT:", target["patent_id"])
    print("TITLE:", target["title"])
    print()

    results = []

    for patent in patents[1:]:
        score = jaccard_similarity(
            target["claims"],
            patent["claims"]
        )
        results.append((patent["patent_id"], score))

    results.sort(key=lambda x: x[1], reverse=True)

    print("CLAIM SIMILARITY RESULTS")
    print("------------------------")

    for patent_id, score in results:
        print(patent_id, "->", round(score, 3))
