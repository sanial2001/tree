class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # Base case
        if label == 1:
            return [1]

        # Calculate the level that the label is present in
        level = 1
        while True:
            if (2 ** level - 1 >= label):
                break
            level += 1

        pathArray = [label]
        # reduce level by 1 since we have already added label to the path array
        level -= 1

        # Base case
        while level != 0:
            # calculating parent
            label = 2 ** (level - 1) + ((2 ** (level + 1) - 1 - label) // 2)
            # insert parent to the top
            pathArray.insert(0, label)
            level -= 1

        return pathArray
