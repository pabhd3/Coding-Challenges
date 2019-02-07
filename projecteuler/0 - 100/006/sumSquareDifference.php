<?php
  // Calculate the Sum of the squares
  function squareSum($n){
    $sum = 0;
    for($i = 1; $i < $n + 1; $i++){ $sum += pow($i, 2); }
    return $sum;
  }
  // Calculate the Square of the sum
  function sumSquares($n){
    $sum = 0;
    for($i = 1; $i < $n + 1; $i++){ $sum += $i; }
    return pow($sum, 2);
  }
  // Get user input
  $prompt = "Enter an integer n: ";
  $n = readline($prompt);
  $sumSquareDifference = sumSquares($n) - squareSum($n);
  // Print results
  echo "Difference between the sum of squares of the first $n natural numbers and the square of the sum";
  echo "\n" . $sumSquareDifference . "\n";
?>