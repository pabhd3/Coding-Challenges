<?php
  function isPalindrome($n){
    $n = str_split($n);
    $nLen = count($n);
    for($i = 0; $i < ceil($nLen / 2); $i++){
      if($n[$i] != $n[$nLen - $i - 1]){ return False; }
    }
    return True;
  }
  function findStart($n){
    $i = 0;
    while(True){
      if(strlen($i) == $n){ return $i; }
      $i++;
    }
  }
  function largestPalindromicProduct($n){
    $largest = 0; $p1 = 0; $p2 = 0;
    $start = findStart($n);
    $i1 = $start;
    while(strlen($i1) <= $n){
      $i2 = $start;
      while(strlen($i2) <= $n){
        if(strlen($i1) == $n && strlen($i2) == $n){
          if(isPalindrome($i1 * $i2) && $i1 * $i2 > $largest){
            $largest = $i1 * $i2; $p1 = $i1; $p2 = $i2;
          }
        }
        $i2++;
      }
      $i1++;
    }
    return [$largest, $p1, $p2];
  }
  // Get user input
  $prompt = "Enter number of digits n: ";
  $n = readline($prompt);
  $results = largestPalindromicProduct($n);
  echo "\nLargest Palindromic Product of two $n-digit numbers\n";
  echo "$results[1] x $results[2] = $results[0]\n";
?>