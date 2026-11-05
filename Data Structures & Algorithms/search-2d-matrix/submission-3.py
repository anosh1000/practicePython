class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1

        while left <= right:
            row = (left + right) // 2

            if target >= matrix[row][0] and target <= matrix[row][-1]:
                left = 0 
                right = len(matrix[row])-1

                while left <= right:
                    middle = (left + right) // 2

                    if matrix[row][middle] == target:
                        return True
                    elif matrix[row][middle] > target:
                        right = middle - 1
                    else: 
                        left = middle + 1
                return False

            elif target < matrix[row][0]:
                right = row - 1
            else: 
                left = row + 1
        return False
