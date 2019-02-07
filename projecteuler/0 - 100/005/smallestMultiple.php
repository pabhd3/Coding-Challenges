<?php
  // Calculate the smallest Multiple
  function smallestMultiple($n){
    $smallestMultiple = 1;
    while(True){
      $evenMultiple = True;
      for($i = 1; $i < $n + 1; $i++){
        if($smallestMultiple % $i != 0){
          $evenMultiple = False;
          break;
        }
      }
      if($evenMultiple){ return $smallestMultiple; }
      $smallestMultiple++;
    }
  }
  // Get user input
  $prompt = "Enter an integer n: ";
  $n = readline($prompt);
  echo "Smallest positive number that is evenly divisible by all of the numbers from 1 to $n";
  echo "\n" . smallestMultiple($n) . "\n";
?>