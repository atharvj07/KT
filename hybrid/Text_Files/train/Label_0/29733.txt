#include <iostream>
using namespace std;

int main() {
  long long S;
  cin >> S;
  cout << 0 << ' ';
  cout << 0 << ' ';
  cout << (S - 1) / 1000000000 + 1 << ' ';
  cout << 1 << ' ';
  cout << (1000000000000000000 - S) % 1000000000 << ' ';
  cout << 1000000000 << endl;
}