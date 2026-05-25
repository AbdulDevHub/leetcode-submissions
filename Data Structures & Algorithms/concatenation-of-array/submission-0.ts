class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        let ans: number[] = nums.concat(nums)
        return ans
    }
}
