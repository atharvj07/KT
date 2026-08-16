#include <bits/stdc++.h>
using namespace std;
long long TestCases, N, a, b;
int main() {
  cin >> TestCases;
  while (TestCases--) {
    cin >> N;
    a = 0;
    b = 0;
    while (N % 3 == 0) {
      N /= 3;
      b++;
      a++;
    }
    while (N % 2 == 0) {
      N /= 2;
      a--;
    }
    if (N != 1 || a < 0) {
      cout << -1 << endl;
    } else {
      cout << a + b << endl;
    }
  }
  return 0;
}
