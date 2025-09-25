import json

class Solution:
    def max_concurrent_learners(self, data: json) -> json:
        data = json.load(data)
        count = 1
        max_concurrent = count

        # Sort by start time
        data = sorted(data, key=lambda x: x[1])

        print(data) # Debug stuffs

        if data is None:
            return json.dumps({"The maximum number of concurrent learners is": 0})
        interval = data[0][1], data[0][2]

        for entry in data[1:]:
            window = entry[1], entry[2]
            # Overlap
            if interval[1] > window[0]:
                count += 1
                if window[0] >= interval[0]:
                    interval = window[0], interval[1]
            # New overlap
            else:
                interval = window
                count = 1
            if count > max_concurrent:
                max_concurrent = count

        return json.dumps({"The maximum number of concurrent learners is:": max_concurrent})

if __name__ == '__main__':
    solution = Solution()
    print(solution.max_concurrent_learners(open('./test-3.json', 'r', encoding='utf-8')))




