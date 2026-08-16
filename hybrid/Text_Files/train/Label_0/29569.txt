#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization("unroll-loops")
using namespace std;
template <typename T>
string to__string(T x) {
  ostringstream ss;
  ss << x;
  return ss.str();
}
int fast_expo(long long a, long long b) {
  long long ans = 1;
  while (b) {
    if (b & 1) ans *= a, ans -= 1000000007;
    a *= a, a %= 1000000007;
    b /= 2;
  }
  return ans;
}
long long max(long long a, long long b) {
  if (a >= b) return a;
  return b;
}
long long min(long long a, long long b) {
  if (a >= b) return b;
  return a;
}
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int n;
void solve() {
  cin >> n;
  if (n == 1) {
    cout << 1 << "\n";
    cout << 1 << "\n";
    return;
  }
  int lo = 1;
  int hi = n - 1;
  int ans;
  while (lo <= hi) {
    int mid = (lo + hi) >> 1;
    if ((mid * (mid + 1)) / 2 <= n) {
      ans = mid;
      lo = mid + 1;
    } else
      hi = mid - 1;
  }
  int sum = (ans * (ans + 1)) / 2;
  int leftover = n - sum;
  cout << ans << "\n";
  for (int i = 1; i <= ans; i++) {
    if (i == ans)
      cout << (i + leftover);
    else
      cout << i << " ";
  }
  cout << "\n";
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int tc = 1;
  while (tc--) solve();
  return 0;
}
