#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e9 + 7;
const long long MOD = 998244353;
inline long long add(long long x, long long y) {
  x += y;
  if (x >= mod) x -= mod;
  return x;
}
inline long long sub(long long x, long long y) {
  x -= y;
  if (x < 0) x += mod;
  return x;
}
inline long long mul(long long x, long long y) { return (x * 1ll * y) % mod; }
long long a, b, c, d;
signed main() {
  long long n, k;
  cin >> n >> k;
  long long arr[n];
  for (long long i = 0; i < n; i++) cin >> arr[i];
  sort(arr, arr + n);
  for (long long i = 0; i < n; i++) {
    long long j = i;
    for (j = i; j < n; j++)
      if (arr[i] != arr[j]) break;
    if (k > (j - i) * n) {
      k -= (j - i) * n;
      i = j - 1;
      continue;
    }
    for (long long m = 0; m < n; m++) {
      if (k > (j - i))
        k -= (j - i);
      else {
        cout << arr[j - 1] << " " << arr[m] << endl;
        return 0;
      }
    }
  }
}
