var isPowerOfThree = function(n) {
    if (n == 1 || n == 3)
        return true
    
    let ans = n / 3
    console.log(ans)
    if (ans == 3) {
        return true
    } else if (ans > 3) {
        return isPowerOfThree(ans)
    } else {
        return false
    }
};
