#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
const int inf = 1 << 30;
const int maxn = 300000 + 5;
inline int add(int x, int y) {
  x += y;
  return x >= mod ? x -= mod : x;
}
inline int sub(int x, int y) {
  x -= y;
  return x < 0 ? x += mod : x;
}
inline int mul(int x, int y) { return 1ll * x * y % mod; }
inline int qpow(int x, long long n) {
  int r = 1;
  while (n > 0) {
    if (n & 1) r = 1ll * r * x % mod;
    n >>= 1;
    x = 1ll * x * x % mod;
  }
  return r;
}
inline int inv(int x) { return qpow(x, mod - 2); }
int n, f[maxn];
pair<int, int> a[maxn];
int main() {
  f[0] = 1;
  scanf("%d", &n);
  map<int, int> mpa, mpb;
  for (int i = 1; i <= n; i++) {
    scanf("%d%d", &a[i].first, &a[i].second);
    mpa[a[i].first]++;
    mpb[a[i].second]++;
    f[i] = mul(f[i - 1], i);
  }
  int ans = f[n], tot = 1;
  for (auto& x : mpa) tot = mul(tot, f[x.second]);
  ans = sub(ans, tot);
  tot = 1;
  for (auto& x : mpb) tot = mul(tot, f[x.second]);
  ans = sub(ans, tot);
  sort(a + 1, a + 1 + n);
  int flag = 1;
  for (int i = 2; i <= n; i++) {
    if (a[i].first < a[i - 1].first || a[i].second < a[i - 1].second) {
      flag = 0;
      break;
    }
  }
  if (flag) {
    map<pair<int, int>, int> mp;
    for (int i = 1; i <= n; i++) {
      mp[a[i]]++;
    }
    tot = 1;
    for (auto& x : mp) tot = mul(tot, f[x.second]);
    ans = add(ans, tot);
  }
  printf("%d", ans);
  return 0;
}
