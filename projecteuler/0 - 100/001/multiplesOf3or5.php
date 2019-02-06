<?php
  // Calculation function
  function multiplesOf3or5($n){
    $sum = 0;
    for($i = 0; $i < $n; $i++){
      if($i % 3 == 0 || $i % 5 == 0){
        $sum += $i;
      }
    }
    return $sum;
  }
  // Get User input
  $prompt="Enter an integer n: ";
  $n = readline($prompt);
  $multiplesSum = multiplesOf3or5($n);
  // Return Result
  echo "\nSum of multiples of 3 or 5 below $n\n";
  echo "$multiplesSum\n";
?>