// Team Sheeps :: Josephine Lee, Ivan Lam
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function fact (n){
    if (n == 0){
      return 1;
    }
    return (n * (fact(n-1)));
}

function fib (n){
    if (n <= 1){
        return n;
    }
    return (fib(n-1) + fib(n-2));
}