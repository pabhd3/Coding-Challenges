function isPrime(n){
    for(let i = 2; i < n; i++){
      if(n % i === 0){ return false; }
    }
    return true;
  }
  function largestPrimeFactor(){
    // Setup
    let n = document.getElementById("inputN").value;
    let largestPrime = 1;
    for(let i = 1; i < n; i++){
      if(isPrime(i) && i > largestPrime && n % i == 0){ largestPrime = i; }
    }
    let answer = `Largest Prime below ${n}<br>${largestPrime}`;
    document.getElementById("answer").innerHTML = answer;
  }