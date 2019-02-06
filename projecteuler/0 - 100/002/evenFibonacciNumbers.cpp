#include <iostream>
#include <vector>
using namespace std;

// Generate the Fibonacci Sequence
std::vector<int> fibonacciSequence(int n){
  std::vector<int> sequence; int next;
  sequence.push_back(1); sequence.push_back(2);
  for(int i = 2; i < n; i++){
    next = sequence[i - 1] + sequence[i - 2];
    if(next > n){ break; }
    else{ sequence.push_back(next); }
  }
  return sequence;
}
// Calculate sum of even-valued terms
int evenFibonacciNumbers(int n){
  int sum = 0;
  std::vector<int> sequence = fibonacciSequence(n);
  for(int i = 0; i < sequence.size(); i++){
    if(sequence[i] % 2 == 0){ sum += sequence[i]; }
  }
  return sum;
}

int main(){
  // Get user input
  int n;
  cout << "Enter a max fibonacci value n: ";
  cin >> n;
  int fibSum = evenFibonacciNumbers(n);
  // Print results
  cout << "Sum of even-valued fibonacci terms below " << n << endl;
  cout << fibSum << endl;
  return 0;
}