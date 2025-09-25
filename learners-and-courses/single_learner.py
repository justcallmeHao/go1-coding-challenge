import json

class Solution:
    def single_course_list(self, data: json) -> json:
        data = json.load(data)
        visited = set()
        unique = set()
        for learner in data:
            current = set(data[learner])
            visit_dup = current.intersection(visited)
            new_visited = current - visit_dup
            visited.update(new_visited)

            unique.update(new_visited)
            unique -= visit_dup
        return json.dumps(list(unique))

if __name__ == '__main__':
    solution = Solution()
    print(solution.single_course_list(open('./test-4.json', 'r', encoding='utf-8')))




