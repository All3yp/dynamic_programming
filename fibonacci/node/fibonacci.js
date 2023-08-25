function fibonacci(n) {
    if (n < 2) return n
    return fibonacci(n - 1) + fibonacci(n - 2)
}

const n = 9;
console.log(n + "th Fibonacci Number: " + fibonacci(n));
