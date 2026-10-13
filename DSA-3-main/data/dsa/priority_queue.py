import heapq


class PatentPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, patent_id, score):
        heapq.heappush(self.heap, (-score, patent_id))

    def pop(self):
        if not self.heap:
            return None

        score, patent_id = heapq.heappop(self.heap)
        return patent_id, -score

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == "__main__":
    pq = PatentPriorityQueue()

    pq.push("P001", 0.40)
    pq.push("P002", 0.75)
    pq.push("P003", 0.90)
    pq.push("P004", 0.30)

    print("PATENT PRIORITY QUEUE")
    print("---------------------")

    while not pq.is_empty():
        patent_id, score = pq.pop()
        print(patent_id, "->", score)
