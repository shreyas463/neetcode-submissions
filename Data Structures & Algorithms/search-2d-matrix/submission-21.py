class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        l,r=0, n*m-1

        while l<=r:
            mid=l+((r-l)//2)
            i,j=mid//m,mid%m

            if matrix[i][j]> target:
                r=mid-1
            elif matrix[i][j]<target:
                l=mid+1
            else:
                return True
        return False
        


       
    # n, m = len(matrix), len(matrix[0])  # Get the number of rows (n) and columns (m)
    # l, r = 0, n * m - 1  # Initialize left (l) and right (r) pointers

    # while l <= r:
    #     mid = l + (r - l) // 2  # Calculate the mid index
    #     i, j = mid // m, mid % m  # Convert the 1D mid index to 2D indices (i, j)
        
    #     if matrix[i][j] < target:
    #         l = mid + 1  # Move the left pointer if the target is larger
    #     elif matrix[i][j] > target:
    #         r = mid - 1  # Move the right pointer if the target is smaller
    #     else:
    #         return True  # Target found, return True

    # return False  # Target not found, return False
    
# The code treats the 2D matrix as a single list
#  and uses binary search on it.
#  It converts the middle index back to row and column to access
#   the matrix. The search adjusts based on comparisons 
#   until the target is found or not.