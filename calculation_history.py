"module 4"
class History:
    def __init__(self):
        self.records=[]
    def add(self, expression, result):
        self.records.append({
            "expression": expression,
            "result": result })
    def get_all(self):
        return self.records.copy()
    def clear(self):
        self.records.clear()