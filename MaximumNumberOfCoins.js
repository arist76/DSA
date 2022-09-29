var maxCoins = function(piles) {
    let sorted_piles = piles.sort((a,b)=>a-b)
    let sum = 0
    let pile_length = sorted_piles.length/3
    for (let i = 0; i < pile_length; i++) {
        console.log(i)
        sorted_piles.pop()
        sum += sorted_piles.pop()
        sorted_piles.splice(0,1)
    }
    return sum
};
