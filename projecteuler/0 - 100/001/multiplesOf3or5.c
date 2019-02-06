#include <stdio.h>

// Function to make calculation
int multiplesOf3or5(int n){
  int sum = 0;
  for(int i = 0; i < n; i++){
    if(i % 3 == 0 || i % 5 == 0){ sum += i; }
  }
  return sum;
}

int main(){
  // Get user input
  int n;
  printf("Enter an integer n: ");
  scanf("%d", &n);
  int multiplesSum = multiplesOf3or5(n);
  // Print result
  printf("\nSum of multiples of 3 or 5 below %d\n%d", n, multiplesSum);
  return 0;
}