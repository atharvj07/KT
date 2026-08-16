#include <cmath>
#include <iostream>
using namespace std;
int main() {
  double a, b = 0.0, c = INFINITY;
  while (cin >> a) {
    if (a > b) b = a;
    if (a < c) c = a;
  }
  cout << (b - c) << endl;
  return 0;
}