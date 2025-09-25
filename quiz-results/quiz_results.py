import json

class Solution:
    def easiest_question(self, answers: json, correct: json) -> json:
        answers = json.load(answers)
        correct = json.load(correct)

        count = {i: 0 for i in range(len(correct))}

        index = range(len(correct))

        for ans in answers:
            check = zip(index, ans, correct)
            for pair in check:
                if pair[1] == pair[2]:
                    count[pair[0]] += 1

        return json.dumps(f"The easiest question is {max(count, key=lambda x: count[x])}")

if __name__ == '__main__':
    solution = Solution()
    print(solution.easiest_question(
        open('./test-3.json', 'r', encoding='utf-8'),
        open('./test-3-ans.json', 'r', encoding='utf-8')))