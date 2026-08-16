#include <bits/stdc++.h>
using namespace std;
long long Cal(long long a, long long b) {
  if (a == 1) return b;
  if (a % b == 0) return a / b;
  long long res = 0;
  if (a > b) {
    long long t = a / b;
    res += t;
    res += Cal(a - b * t, b);
  } else
    res += Cal(b, a);
  return res;
}
int main() {
  long long a, b;
  cin >> a >> b;
  cout << Cal(a, b) << endl;
}
