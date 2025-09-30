class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        Queue=[]
        for person in people:
            heapq.heappush(Queue,(-person[0],person[1]))

        result=[]
        while Queue:
            person=heapq.heappop(Queue)
            result.insert(person[1],(-person[0],person[1]))
        return result