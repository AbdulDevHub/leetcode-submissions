class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for n in range(numRows):
            row = [1] # First element is always 1
            current_val = 1
            for k in range(1, n + 1):
                # Compute the next element in the row mathematically
                current_val = current_val * (n - k + 1) // k
                row.append(current_val)
            triangle.append(row)
            
        return triangle
