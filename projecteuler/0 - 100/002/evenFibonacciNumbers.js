function evenFibonacciNumbers(){
    // Setup
    let n = document.getElementById("inputN").value;
    let fib = [1, 2];
    // Generate Fibonacci Sequence
    for(let i = 2; i < n; i++){
      if(fib[i - 1] + fib[i - 2] > n){ break; }
      else{ fib.push(fib[i - 1] + fib[i - 2]); }
    }
    // Calculate Even Sum
    let sum = 0;
    fib.forEach(function(element){
      if(element % 2 == 0) { sum += element; }
    });
    // Display Answer
    let answer = `Sum of even-valued fibonacci terms below ${n}<br>${sum}`;
    document.getElementById("answer").innerHTML = answer;
  }