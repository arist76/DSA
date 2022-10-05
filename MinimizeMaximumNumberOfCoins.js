var minPairSum = function(nums) {
    sorted_nums = nums.sort((a,b) => a-b)
    let max_temp = 0
    let j = nums.length - 1
    for(let i = 0; i < j; i++) {
        sum = nums[i] + nums[j]
        if (max_temp < sum)
            max_temp = sum
        j--
    }
    return max_temp
};
