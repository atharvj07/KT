#include <bits/stdc++.h>
using namespace std;
inline int ri() {
  int x;
  scanf("%d", &x);
  return x;
}
template <typename T>
inline bool smax(T& a, T b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}
template <typename T>
inline bool smin(T& a, T b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
template <typename T>
inline T pw(T a, long long b) {
  T c = 1;
  while (b) {
    if (b & 1) c = (c * a);
    a = a * a;
    b >>= 1;
  }
  return c;
}
struct mint {
  const static long long mod = 1e9 + 7;
  long long x;
  mint() : x(0) {}
  mint(long long x) : x(((x % mod) + mod) % mod){};
  mint operator+=(const mint& a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint operator-=(const mint& a) {
    if ((x += mod - a.x) >= mod) x -= mod;
    return *this;
  }
  mint operator*=(const mint& a) {
    (x *= a.x) %= mod;
    return *this;
  }
  mint operator+(const mint& a) const { return mint(*this) += a; }
  mint operator-(const mint& a) const { return mint(*this) -= a; }
  mint operator*(const mint& a) const { return mint(*this) *= a; }
  bool operator==(const mint& a) const { return x == a.x; }
};
const long long mod = 1e9 + 7;
template <typename T>
T inv(T a) {
  return pw(a, mod - 2);
}
const int maxn = 300010;
int p[maxn], cnt[maxn], n;
mint res, c[maxn], s[maxn];
vector<int> g[maxn];
mint f(int l, int r) {
  if (r < l || r < 0 || l > n - 2) return 0;
  if (l < 0) l = 0;
  if (r > n - 2) r = n - 2;
  return s[r] - (l == 0 ? 0 : s[l - 1]);
}
void calc(vector<int>& v) {
  v[0] = n;
  for (int i = (1); i < (20); i++) v[0] -= v[i];
  int sum = 0, num = 0;
  for (int i = 0; i < (20); i++) {
    res += f(num, v[i] + num - 1) * (num * i - sum);
    res += f(num - 1, v[i] + num - 2) * (num * i - sum);
    num += v[i];
    sum += v[i] * i;
  }
  sum = 0;
  num = 0;
  for (int i = 19; i >= 0; i--) {
    res += f(num, v[i] + num - 1) * (sum - num * i);
    res += f(num + 1, v[i] + num) * (sum - num * i);
    num += v[i];
    sum += v[i] * i;
  }
}
int main() {
  n = ri();
  for (int i = 0; i < (n); i++) cnt[ri()]++;
  c[0] = s[0] = 1;
  for (int i = 0; i < (n - 2); i++)
    c[i + 1] = c[i] * inv(mint(i + 1)) * (n - 2 - i),
          s[i + 1] = c[i + 1] + s[i];
  for (int i = (2); i < (maxn); i++) {
    if (p[i]) continue;
    for (int j = i; j < maxn; j += i)
      if (!p[j]) {
        p[j] = i;
      }
  }
  for (int i = 0; i < (maxn); i++)
    if (cnt[i]) {
      int x = i;
      while (x > 1) {
        int t = p[x], cur = 0;
        while (x % t == 0) x /= t, cur++;
        if (g[t].empty()) g[t].resize(20);
        g[t][cur] += cnt[i];
      }
    }
  for (int i = 0; i < (maxn); i++)
    if (!g[i].empty()) calc(g[i]);
  cout << res.x << endl;
  return 0;
}
