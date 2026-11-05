class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            length = len(row) - 1
            if target >= row[0] and target <= row[length]:
                left = 0 
                right = len(row)-1

                while left <= right:
                    middle = (left + right) // 2
                    if row[middle] == target:
                        return True
                    elif row [middle] > target:
                        right = middle - 1
                    else: 
                        left = middle + 1
                return False
        return False
