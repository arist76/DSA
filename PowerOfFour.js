
var isPowerOfFour = function(n) {
    if (n == 1 || n == 4)
        return true
    
    let ans = n / 4
    if (ans == 4)
        return true
    else if (ans > 4)
        return isPowerOfFour(ans)
    else
        return false
};

