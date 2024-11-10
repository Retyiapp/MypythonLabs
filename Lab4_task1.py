import json
def task() -> float:
    file = "input.json"
    jData = json.load(open(file))
    Mysum = sum([i["score"] * i["weight"] for i in jData])
    return round(Mysum, 3)
print(task())
