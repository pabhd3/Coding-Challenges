<?php
  // Check if a number is prime
  function isPrime($n){
    for ($i = 2; $i < $n; $i++) {
      if($n % $i == 0){ return False; }
    }
    return True;
  }
  // Find the nth prime number
  function nthPrime($n){
    $i = 2; $count = 0;
    while(True){
      if(isPrime($i)){
        $count++;
        if($count == $n){ return $i; }
      }
      $i++;
    }
  }
  // Get user input
  $prompt = "Enter an integer n: ";
  $n = readline($prompt);
  $nthPrime = nthPrime($n);
  // Print results
  echo "\nThe $n-th prime is";
  echo "\n" . $nthPrime . "\n";
?>