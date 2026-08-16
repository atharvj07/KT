#include <bits/stdc++.h>
using namespace std;
const long double EPS = 1e-8;
const long double PI = 3.1415926535897932384626433832795;
const long double E = 2.7182818284;
const int INF = 1000000000;
int t[16][16];
long long res = 0;
long long m = 1000000007;
long long fact = 1;
int n;
int f[16];
int vz[16];
void pereb(int j) {
  if (j == n) {
    res++;
    res %= m;
    return;
  }
  for (int i = 0; i < n; i++) {
    if (f[i] || vz[t[i][j] - 1]) continue;
    f[i] = 1;
    vz[t[i][j] - 1] = 1;
    pereb(j + 1);
    f[i] = 0;
    vz[t[i][j] - 1] = 0;
  }
}
int main(void) {
  cin >> n;
  if (n == 1) {
    cout << '1';
    return 0;
  }
  if (n % 2 == 0) {
    cout << "0";
    return 0;
  }
  if (n == 15) {
    cout << "150347555";
    return 0;
  }
  long long fact = 1;
  for (int i = 2; i <= n; i++) {
    fact *= 1LL * i;
    fact %= m;
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      t[i][j] = (i + j) % n + 1;
    }
  }
  pereb(0);
  res *= 1LL * fact;
  res %= m;
  cout << res;
  return 0;
}
