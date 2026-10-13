import json


class PatentHashMap:
    def __init__(self):
        self.index = {}

    def build_index(self, patents):
        for patent in patents:
            patent_id = patent["patent_id"]

            for keyword in patent["keywords"]:
                keyword = keyword.lower()

                if keyword not in self.index:
                    self.index[keyword] = []

                self.index[keyword].append(patent_id)

    def search(self, keyword):
        keyword = keyword.lower()
        return self.index.get(keyword, [])

    def display_index(self):
        for keyword, patents in self.index.items():
            print(keyword, "->", patents)


def load_patents():
    with open("data/patents.json", "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    patents = load_patents()

    patent_map = PatentHashMap()
    patent_map.build_index(patents)

    print("HASHMAP INDEX")
    print("----------------")

    patent_map.display_index()

    print("\nSEARCH RESULTS")
    print("----------------")

    keyword = input("Enter keyword: ")

    results = patent_map.search(keyword)

    if results:
        print("Patents containing", keyword, ":", results)
    else:
        print("No patents found.")
