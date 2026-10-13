import json


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.patents = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, patent_id):
        node = self.root

        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

        if patent_id not in node.patents:
            node.patents.append(patent_id)

    def search_prefix(self, prefix):
        node = self.root

        for char in prefix.lower():
            if char not in node.children:
                return {}

            node = node.children[char]

        results = {}
        self._collect(node, prefix.lower(), results)

        return results

    def _collect(self, node, word, results):
        if node.is_end:
            results[word] = node.patents

        for char, child in node.children.items():
            self._collect(child, word + char, results)


def load_patents():
    with open("data/patents.json", "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":

    patents = load_patents()

    trie = Trie()

    for patent in patents:
        for keyword in patent["keywords"]:
            trie.insert(keyword, patent["patent_id"])

    prefix = input("Enter keyword prefix: ")

    results = trie.search_prefix(prefix)

    print("\nTRIE SEARCH RESULTS")
    print("-------------------")

    if results:
        for keyword, patent_ids in results.items():
            print(keyword, "->", patent_ids)
    else:
        print("No matching keywords found.")
