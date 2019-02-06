# include <iostream>
using namespace std;

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
  cout << "Enter an integer n: ";
  cin >> n;
  int multiplesSum = multiplesOf3or5(n);
  // Print result
  cout << endl << "Sum of multiples of 3 or 5 below " << n << endl;
  cout << multiplesSum << endl;
  return 0;
}