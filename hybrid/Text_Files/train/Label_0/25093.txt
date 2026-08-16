#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization("unroll-loops")
long long int gcd(long long int a, long long int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int t;
  t = 1;
  while (t--) {
    long long int n;
    cin >> n;
    string s;
    cin >> s;
    long long int dig[n], idx = 0, dc = 0;
    for (long long int i = n - 1; i >= 0; i--) {
      if (s[i] == '0' || i == 0) {
        dig[idx] = dc;
        idx++;
        dc = 0;
      } else {
        dc++;
      }
    }
    dig[idx - 1]++;
    for (long long int i = idx - 1; i >= 0; i--) {
      cout << dig[i];
    }
  }
  return 0;
}
