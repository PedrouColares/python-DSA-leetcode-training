class TwoSum():

    def run(self, array, target):
        hasher = {}

        for i, v in enumerate(array):
            if (v in hasher):
                return [i, hasher[v]]
            
            hasher[target - v] = i

        return []