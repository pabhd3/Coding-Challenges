<?php
  // Generate the Fibonacci Sequence
  function maxFibonacciValue($n){
    $fib = array(1, 2);
    for ($i=2; $i < $n; $i++) {
      $next = $fib[$i - 1] + $fib[$i - 2];
      if($next > $n){ break; }
      else{ array_push($fib, $next); }
    }
    return $fib;
  }
  // Calculate sum of even-valued terms
  function evenFibonacciNumbers($n){
    $sum = 0;
    $seq[] = maxFibonacciValue($n);
    foreach($seq[0] as $value){
      if($value % 2 == 0){ $sum += $value; }
    }
    return $sum;
  }
  // Get user input
  $prompt = "Enter a max fibonacci value n: ";
  $n = readline($prompt);
  $fibSum = evenFibonacciNumbers($n);
  // Print results
  echo "\nSum of even-valued fibonacci terms below $n";
  echo "\n$fibSum\n";
?>