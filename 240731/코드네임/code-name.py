import sys

class agent:
    def __init__(self, code, score):
        self.code = code
        self.score = score

agents = []

for i in range(5):
    code, score = tuple(input().split())
    score = int(score)
    agents.append(agent(code,score))

min_score = sys.maxsize
min_code = 0

for i in range(5):
    if agents[i].score < min_score:
        min_code = agents[i].code
        min_score = agents[i].score

print(min_code, min_score)