import json

class Solution:
    def easiest_question(self, answers: json, correct: json) -> json:
        answers = json.loads(answers)
        correct = json.loads(correct)

