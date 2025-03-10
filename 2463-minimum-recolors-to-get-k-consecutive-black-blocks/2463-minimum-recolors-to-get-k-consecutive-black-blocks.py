class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        num_whites = 0
        min_change = float("inf")
        count = 0

        for end in range(len(blocks)):
            if blocks[end] == "W":
                num_whites += 1
            if end - start + 1 == k:
                min_change = min(num_whites, min_change)
                if blocks[start] == "W":
                    num_whites -= 1
                start += 1
        return min_change
        
