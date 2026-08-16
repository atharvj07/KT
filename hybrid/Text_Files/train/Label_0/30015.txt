#include <bits/stdc++.h>
using namespace std;
struct node {
  long long y, nex;
} a[2 * 210000];
struct node1 {
  long long dep, par[20];
} t[210000];
long long fir[210000], len, n, m, z;
long long inf = 1ll << 60;
bool bo;
void ins(long long x, long long y) {
  a[++len].y = y;
  a[len].nex = fir[x];
  fir[x] = len;
}
void dfs(long long x, long long fa) {
  t[x].dep = t[fa].dep + 1;
  t[x].par[0] = fa;
  for (long long i = 1; i <= 18; i++)
    t[x].par[i] = t[t[x].par[i - 1]].par[i - 1];
  for (long long k = fir[x]; k; k = a[k].nex) {
    long long y = a[k].y;
    if (y == fa) continue;
    dfs(y, x);
  }
}
long long lca(long long x, long long y) {
  if (t[x].dep < t[y].dep) swap(x, y);
  for (long long i = 18; i >= 0; i--)
    if (t[t[x].par[i]].dep >= t[y].dep) x = t[x].par[i];
  if (x == y) return x;
  for (long long i = 18; i >= 0; i--)
    if (t[x].par[i] != t[y].par[i]) x = t[x].par[i], y = t[y].par[i];
  return t[x].par[0];
}
long long lower(long long x, long long y) {
  if (t[x].dep > t[y].dep) return x;
  return y;
}
long long dis(long long x, long long y) {
  long long u = lca(x, y);
  return t[x].dep + t[y].dep - 2 * t[u].dep;
}
long long exgcd(long long a, long long b, long long &x, long long &y) {
  if (b == 0) {
    x = 1;
    y = 0;
    return a;
  }
  long long t = a / b, g, xx, yy;
  g = exgcd(b, a % b, xx, yy);
  x = yy;
  y = xx - t * yy;
  return g;
}
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
long long same(long long t1, long long t2, long long f1, long long f2) {
  long long t = ((t2 - t1) % f2 + f2) % f2;
  long long p, q, g, m;
  g = exgcd(f1, f2, p, q);
  if (t % g) return inf;
  p *= t / g;
  q *= t / g;
  m = f2 / g;
  p = (p % m + m) % m;
  return p * f1 + t1;
}
long long G(long long M, long long D, long long L, long long R) {
  long long t = L / D;
  if (t * D < L) t++;
  if (t * D <= R) return t;
  if (2 * D > M) return G(M, M - D, M - R, M - L);
  long long k = G(D, ((-M % D) + D) % D, L % D, R % D);
  L += M * k;
  R += M * k;
  t = L / D;
  if (t * D < L) t++;
  return t;
}
long long make(long long M, long long D, long long L, long long R) {
  long long g = gcd(M, D);
  if ((L - 1) / g >= R / g) return inf;
  return G(M, D, L, R);
}
long long diff(long long t1, long long t2, long long f1, long long f2,
               long long d) {
  long long l = t2 - t1 - d, r = t2 - t1 + d;
  l = (l % f2 + f2) % f2;
  r = (r % f2 + f2) % f2;
  if (l % 2) return inf;
  if (l > r || l == 0) return t1 + r / 2;
  if (f2 == d * 2) return t1 + r / 2;
  long long p = make(f2, f1 % f2, l, r), q;
  if (p == inf) return inf;
  return p * f1 + t1 + d - (p * f1 % f2 - l) / 2;
}
long long solve() {
  long long x, y, u, v, a, b, p1, p2, p3, p4, p5, p6, p, d, t1, t2, t3, t4, f1,
      f2, d1, d2;
  z++;
  scanf("%lld%lld%lld%lld", &x, &y, &u, &v);
  if (bo && z == 143) printf("%lld %lld %lld %lld\n", x, y, u, v);
  p1 = lca(x, y);
  p2 = lca(u, v);
  p3 = lca(x, u);
  p4 = lca(x, v);
  p5 = lca(y, u);
  p6 = lca(y, v);
  p = lower(p1, p2);
  a = lower(p3, p4);
  b = lower(p5, p6);
  if (t[p].dep > t[a].dep && t[p].dep > t[b].dep) return -1;
  if (t[p].dep > t[a].dep)
    a = p;
  else if (t[p].dep > t[b].dep)
    b = p;
  d = dis(a, b);
  f1 = 2 * dis(x, y);
  f2 = 2 * dis(u, v);
  d1 = dis(x, a);
  d2 = dis(x, b);
  if (d1 < d2)
    t1 = d1, t2 = f1 - d2;
  else
    t1 = f1 - d1, t2 = d2;
  d1 = dis(u, a);
  d2 = dis(u, b);
  if (d1 < d2)
    t3 = d1, t4 = f2 - d2;
  else
    t3 = f2 - d1, t4 = d2;
  long long res = inf;
  res = min(same(t1, t3, f1, f2), res);
  res = min(same(t2, t4, f1, f2), res);
  res = min(diff(t1, t4, f1, f2, d), res);
  res = min(diff(t2, t3, f1, f2, d), res);
  if (res == inf) res = -1;
  return res;
}
int main() {
  scanf("%lld", &n);
  for (long long i = 1; i < n; i++) {
    long long x, y;
    scanf("%lld%lld", &x, &y);
    ins(x, y);
    ins(y, x);
  }
  dfs(1, 0);
  scanf("%lld", &m);
  while (m--) {
    long long ans = solve();
    if (bo == 0) printf("%lld\n", ans);
  }
  return 0;
}
