import json

class Solution:
    def next_most_common(self, data: json) -> json:
        data = json.load(data)
        course_dict = dict()

        # Check all sequences and map k-v: Course-[its next courses]
        for entry in data:
            if len(entry) < 2:
                continue
            for i in range(len(entry) - 1):
                if entry[i] not in course_dict:
                    course_dict[entry[i]] = list()
                course_dict[entry[i]].append(entry[i + 1])

        # Identify the most common course(s) in [its next courses]
        max_occurrences = 0
        for key, value in course_dict.items():
            course_dict[key] = self.count_common(value)
            # Find max occurrance (among all courses)
            if course_dict[key][0] > max_occurrences:
                max_occurrences = course_dict[key][0]

        most_common = dict()
        for key, value in course_dict.items():
            if value[0] == max_occurrences:
                most_common[key] = value[1]

        return json.dumps(most_common)

    def count_common(self, next_courses: list) -> tuple[int, None] | tuple[int, list[str]]:
        if next_courses is None:
            return 0, None
        most_common = dict()
        current = None
        count = 0
        max_count = count

        # Arrange all next courses in order
        sorted(next_courses)

        # Find the max occurrence (for its individual course)
        for course in next_courses:
            if current is None or current != course:
                # Reset for new next course count
                current = course
                count = 1
                most_common[current] = count
            else:
                count += 1
                most_common[current] = count
            if count > max_count:
                max_count = count
        # Re-loop to check all courses match max occurrence
        return max_count, [key for key, value in most_common.items() if value == max_count]



if __name__ == '__main__':
    solution = Solution()
    print(solution.next_most_common(open('./test-2.json', 'r', encoding='utf-8')))