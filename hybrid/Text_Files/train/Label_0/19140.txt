#include <bits/stdc++.h>
using namespace std;
const int MAXN = 262144;
const int MOD = 998244353;
inline void ADD(int& x, int y) {
  x += y;
  if (x >= MOD) x -= MOD;
}
inline void DEC(int& x, int y) {
  x -= y;
  if (x < 0) x += MOD;
}
inline int add(int x, int y) { return x + y < MOD ? x + y : x + y - MOD; }
inline int dec(int x, int y) { return x < y ? x - y + MOD : x - y; }
long long q_pow(long long a, long long b, long long p = MOD) {
  long long ret = 1;
  for (; b; a = a * a % p, b >>= 1)
    if (b & 1) ret = ret * a % p;
  return ret;
}
long long q_inv(long long x, long long p = MOD) { return q_pow(x, p - 2, p); }
int LIM, L, rev[MAXN];
void NTT(int* f, int op) {
  for (int i = 0; i < LIM; ++i)
    rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (L - 1));
  for (int i = 0; i < LIM; ++i)
    if (i < rev[i]) swap(f[i], f[rev[i]]);
  for (int l = 2; l <= LIM; l <<= 1) {
    int wn = q_pow(3, (MOD - 1) / l);
    if (op == -1) wn = q_inv(wn);
    for (int i = 0; i < LIM; i += l)
      for (int j = 0, g = 1; j < (l >> 1); ++j, g = 1ll * g * wn % MOD) {
        int x = f[i | j], y = 1ll * g * f[i | j | (l >> 1)] % MOD;
        f[i | j] = add(x, y), f[i | j | (l >> 1)] = dec(x, y);
      }
  }
  if (op == -1) {
    int iv = q_inv(LIM);
    for (int i = 0; i < LIM; ++i) f[i] = 1ll * f[i] * iv % MOD;
  }
}
int N;
long long M;
int fac[MAXN], ifac[MAXN];
int p[MAXN], tmp[MAXN];
int main() {
  scanf("%d%lld", &N, &M);
  LIM = 1, L = 0;
  while (LIM <= N * 2) LIM <<= 1, ++L;
  for (int i = 0; i <= N; ++i) scanf("%d", &p[i]);
  fac[0] = 1;
  for (int i = 1; i <= N; ++i) fac[i] = 1ll * fac[i - 1] * i % MOD;
  ifac[N] = q_inv(fac[N]);
  for (int i = N - 1; i >= 0; --i) ifac[i] = 1ll * ifac[i + 1] * (i + 1) % MOD;
  for (int i = 0; i <= N; ++i) p[i] = 1ll * p[i] * fac[i] % MOD;
  for (int i = 0; i < LIM; ++i) tmp[i] = 0;
  for (int i = 0; i <= N - i; ++i) swap(p[i], p[N - i]);
  for (int i = 0; i <= N; ++i) tmp[i] = ifac[i];
  NTT(tmp, 1);
  NTT(p, 1);
  for (int i = 0; i < LIM; ++i) p[i] = 1ll * p[i] * tmp[i] % MOD;
  NTT(p, -1);
  for (int i = 0; i <= N - i; ++i) swap(p[i], p[N - i]);
  for (int i = 0; i <= N; ++i) p[i] = 1ll * p[i] * ifac[i] % MOD;
  for (int i = N + 1; i < LIM; ++i) p[i] = 0;
  for (int i = 0; i <= N; ++i) p[i] = 1ll * p[i] * q_pow(q_inv(i + 1), M) % MOD;
  for (int i = 0; i <= N; ++i) p[i] = 1ll * p[i] * fac[i] % MOD;
  for (int i = 0; i < LIM; ++i) tmp[i] = 0;
  for (int i = 0; i <= N - i; ++i) swap(p[i], p[N - i]);
  for (int i = 0; i <= N; ++i) tmp[i] = i & 1 ? MOD - ifac[i] : ifac[i];
  NTT(tmp, 1);
  NTT(p, 1);
  for (int i = 0; i < LIM; ++i) p[i] = 1ll * p[i] * tmp[i] % MOD;
  NTT(p, -1);
  for (int i = 0; i <= N - i; ++i) swap(p[i], p[N - i]);
  for (int i = 0; i <= N; ++i) p[i] = 1ll * p[i] * ifac[i] % MOD;
  for (int i = N + 1; i < LIM; ++i) p[i] = 0;
  for (int i = 0; i <= N; ++i) printf("%d ", p[i]);
  return 0;
}
