JavaScript_________NO RECURSION_____
function getfib(num) {
    let arr = [0, 1];
    for (let i = 2; i < num + 1; i++) {
        arr.push(arr[i - 1] + arr[i - 2]);
    }
    return arr[num];
}
console.log(getfib(10));



console.log('here', num2)
