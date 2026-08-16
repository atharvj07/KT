#include <bits/stdc++.h>
using namespace std;
long long int n, i, j, sum, lsbl, t;
long double lsbl1;
long double ksm(long double a, long long int b) {
  long double sumend = 1;
  while (b) {
    if (b % 2 == 1) sumend *= a;
    a *= a;
    b /= 2;
  }
  return sumend;
}
int main() {
  cin >> n >> t;
  lsbl1 = n * ksm(1.000000011, t);
  cout << fixed << setprecision(15) << n * ksm(1.000000011, t) << endl;
  return 0;
}
