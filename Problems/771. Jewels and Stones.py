"""
771. Jewels and Stones (Easy, 83.0%)

You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone_dict = {}
        
        for s in S:
            if s in stone_dict:
                stone_dict[s] += 1
            else:
                stone_dict[s] = 1
                
        num_jewels = 0
        for j in J:
            if j in stone_dict:
                num_jewels += stone_dict[j]
                
        return num_jewels

def test_case(J: str, S: str):
    ans = Solution().numJewelsInStones(J, S)
    print("I found {0} jewels.".format(ans))

if __name__ == "__main__":
    test_case("aA", "aAAbbbb")

"""
Runtime: 32 ms, faster than 99.57% of Python3 online submissions for Jewels and Stones.
Memory Usage: 13.2 MB, less than 5.25% of Python3 online submissions for Jewels and Stones.
"""