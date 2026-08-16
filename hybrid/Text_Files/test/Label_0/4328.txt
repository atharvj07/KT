#include <bits/stdc++.h>
using namespace std;
template <class T>
inline void read(T &x) {
  int f = 0;
  x = 0;
  char ch = getchar();
  for (; !isdigit(ch); ch = getchar()) f |= (ch == '-');
  for (; isdigit(ch); ch = getchar()) x = x * 10 + ch - '0';
  if (f) x = -x;
}
const int mod = 998244353;
namespace Poly {
const int N = (1 << 20) + 5, g = 3;
inline int power(int x, int p) {
  int res = 1;
  for (; p; p >>= 1, x = (long long)x * x % mod)
    if (p & 1) res = (long long)res * x % mod;
  return res;
}
inline int fix(const int x) { return x >= mod ? x - mod : x; }
void dft(vector<int> &A, int n) {
  static unsigned long long W[N << 1], *H[30], *las = W, mx = 0;
  for (; mx < n; mx++) {
    H[mx] = las;
    unsigned long long w = 1, wn = power(g, (mod - 1) >> (mx + 1));
    for (int i = (0); i < (1 << mx); i++) *las++ = w, w = w * wn % mod;
  }
  if (A.size() != (1 << n)) A.resize(1 << n);
  static unsigned long long a[N];
  for (int i = 0, j = 0; i < (1 << n); ++i) {
    a[i] = A[j];
    for (int k = 1 << (n - 1); (j ^= k) < k; k >>= 1)
      ;
  }
  for (int k = 0, d = 1; k < n; k++, d <<= 1)
    for (int i = 0; i < (1 << n); i += (d << 1)) {
      unsigned long long *l = a + i, *r = a + i + d, *w = H[k], t;
      for (int j = 0; j < d; j++, l++, r++) {
        t = (*r) * (*w++) % mod;
        *r = *l + mod - t, *l += t;
      }
    }
  for (int i = (0); i < (1 << n); i++) A[i] = a[i] % mod;
}
void idft(vector<int> &a, int n) {
  a.resize(1 << n), reverse(a.begin() + 1, a.end());
  dft(a, n);
  int inv = power(1 << n, mod - 2);
  for (int i = (0); i < (1 << n); i++) a[i] = (long long)a[i] * inv % mod;
}
vector<int> FIX(vector<int> a) {
  while (!a.empty() && !a.back()) a.pop_back();
  return a;
}
vector<int> mul(vector<int> &a, vector<int> &b, int t = 1) {
  if (t == 1 && a.size() + b.size() <= 24) {
    vector<int> c(a.size() + b.size(), 0);
    for (int i = (0); i < (a.size()); i++)
      for (int j = (0); j < (b.size()); j++)
        c[i + j] = (c[i + j] + (long long)a[i] * b[j]) % mod;
    return FIX(c);
  }
  int n = 1, aim = a.size() * t + b.size();
  while ((1 << n) <= aim) n++;
  dft(a, n), dft(b, n);
  if (t == 1)
    for (int i = (0); i < (1 << n); i++) a[i] = (long long)a[i] * b[i] % mod;
  else
    for (int i = (0); i < (1 << n); i++)
      a[i] = (long long)a[i] * a[i] % mod * b[i] % mod;
  idft(a, n), a.resize(aim);
  return FIX(a);
}
}  // namespace Poly
using namespace Poly;
int a[N], b[N], n, K, Q, op, x, y, z, w;
vector<int> solve(int l, int r) {
  if (l == r) return {1, b[l]};
  int mid = (l + r) >> 1;
  vector<int> L = solve(l, mid);
  vector<int> R = solve(mid + 1, r);
  return mul(L, R);
}
int main() {
  read(n), read(K);
  for (int i = (1); i <= (n); i++) {
    read(a[i]);
    a[i] %= mod;
  }
  read(Q);
  while (Q--) {
    read(op), read(x), read(y), read(z);
    for (int i = (1); i <= (n); i++) b[i] = a[i];
    if (op == 1) {
      b[y] = z % mod;
    } else {
      read(w);
      for (int i = (y); i <= (z); i++) b[i] = (b[i] + w) % mod;
    }
    for (int i = (1); i <= (n); i++) b[i] = (x + mod - b[i]) % mod;
    vector<int> res = solve(1, n);
    printf("%d\n", res[K]);
  }
  return 0;
}
