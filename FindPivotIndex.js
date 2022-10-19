/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    prefixed_sum = [nums[0]]
    for (let i = 1; i < nums.length; i++)
        prefixed_sum.push(nums[i] + prefixed_sum[i-1])
    
    for (var j=0; j < nums.length; j++){
        if (
            (j == nums.length - 1 && prefixed_sum[nums.length-2] == 0) ||
            (j == 0 && prefixed_sum[nums.length-1] - prefixed_sum[j] == 0) ||
            (prefixed_sum[nums.length-1] - prefixed_sum[j] == prefixed_sum[j-1])
        )
            return j
    }
    
    return -1
};
