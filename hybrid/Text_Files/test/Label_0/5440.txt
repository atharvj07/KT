#include <bits/stdc++.h>
using namespace std;
int main() {
  unsigned long long m, y, n, z;
  char b;
  cin >> n >> b;
  unsigned long long t = n % 4;
  if (t == 1 || t == 2) {
    z = n / 2;
    y = n - 1;
  }
  if (t == 3 || t == 0) {
    z = n / 2 - 1;
    y = n - 3;
    ;
  }
  m = z * 6 + y;
  if (b == 'a') m += 4;
  if (b == 'b') m += 5;
  if (b == 'c') m += 6;
  if (b == 'd') m += 3;
  if (b == 'e') m += 2;
  if (b == 'f') m += 1;
  cout << m;
}
