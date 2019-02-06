<?php
  // Check if a number is prime
  function isPrime($n){
    for ($i = 2; $i < $n; $i++) {
      if($n % $i == 0){ return False; }
    }
    return True;
  }
  // Find the largest prime number below n
  function largestPrime($n){
    $largestPrime = 1;
    for ($i = 1; $i < $n ; $i++) {
      if (isPrime($i) && $i > $largestPrime && $n % $i == 0){ $largestPrime = $i; }
    }
    return $largestPrime;
  }
  // Get user input
  $prompt = "Enter an integer n: ";
  $n = readline($prompt);
  $largestPrime = largestPrime($n);
  // Print results
  echo "\nLargest Prime below $n";
  echo "\n$largestPrime\n"
?>