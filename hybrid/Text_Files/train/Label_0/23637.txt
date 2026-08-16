#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000000007;
long long powmod(long long a, long long b) {
  long long res = 1;
  a %= mod;
  assert(b >= 0);
  for (; b; b >>= 1) {
    if (b & 1) res = res * a % mod;
    a = a * a % mod;
  }
  return res;
}
namespace Factor {
const int N = 1010000;
long long C, fac[10010], n, mut, a[1001000];
int T, cnt, i, l, prime[N], p[N], psize, _cnt;
long long _e[100], _pr[100];
vector<long long> d;
inline long long mul(long long a, long long b, long long p) {
  if (p <= 1000000000)
    return a * b % p;
  else if (p <= 1000000000000ll)
    return (((a * (b >> 20) % p) << 20) + (a * (b & ((1 << 20) - 1)))) % p;
  else {
    long long d = (long long)floor(a * (long double)b / p + 0.5);
    long long ret = (a * b - d * p) % p;
    if (ret < 0) ret += p;
    return ret;
  }
}
void prime_table() {
  int i, j, tot, t1;
  for (i = 1; i <= psize; i++) p[i] = i;
  for (i = 2, tot = 0; i <= psize; i++) {
    if (p[i] == i) prime[++tot] = i;
    for (j = 1; j <= tot && (t1 = prime[j] * i) <= psize; j++) {
      p[t1] = prime[j];
      if (i % prime[j] == 0) break;
    }
  }
}
void init(int ps) {
  psize = ps;
  prime_table();
}
long long powl(long long a, long long n, long long p) {
  long long ans = 1;
  for (; n; n >>= 1) {
    if (n & 1) ans = mul(ans, a, p);
    a = mul(a, a, p);
  }
  return ans;
}
bool witness(long long a, long long n) {
  int t = 0;
  long long u = n - 1;
  for (; ~u & 1; u >>= 1) t++;
  long long x = powl(a, u, n), _x = 0;
  for (; t; t--) {
    _x = mul(x, x, n);
    if (_x == 1 && x != 1 && x != n - 1) return 1;
    x = _x;
  }
  return _x != 1;
}
bool miller(long long n) {
  if (n < 2) return 0;
  if (n <= psize) return p[n] == n;
  if (~n & 1) return 0;
  for (int j = 0; j <= 7; j++)
    if (witness(rand() % (n - 1) + 1, n)) return 0;
  return 1;
}
long long gcd(long long a, long long b) {
  long long ret = 1;
  while (a != 0) {
    if ((~a & 1) && (~b & 1))
      ret <<= 1, a >>= 1, b >>= 1;
    else if (~a & 1)
      a >>= 1;
    else if (~b & 1)
      b >>= 1;
    else {
      if (a < b) swap(a, b);
      a -= b;
    }
  }
  return ret * b;
}
long long rho(long long n) {
  for (;;) {
    long long X = rand() % n, Y, Z, T = 1, *lY = a, *lX = lY;
    int tmp = 20;
    C = rand() % 10 + 3;
    X = mul(X, X, n) + C;
    *(lY++) = X;
    lX++;
    Y = mul(X, X, n) + C;
    *(lY++) = Y;
    for (; X != Y;) {
      long long t = X - Y + n;
      Z = mul(T, t, n);
      if (Z == 0) return gcd(T, n);
      tmp--;
      if (tmp == 0) {
        tmp = 20;
        Z = gcd(Z, n);
        if (Z != 1 && Z != n) return Z;
      }
      T = Z;
      Y = *(lY++) = mul(Y, Y, n) + C;
      Y = *(lY++) = mul(Y, Y, n) + C;
      X = *(lX++);
    }
  }
}
void _factor(long long n) {
  for (int i = 0; i < cnt; i++) {
    if (n % fac[i] == 0) n /= fac[i], fac[cnt++] = fac[i];
  }
  if (n <= psize) {
    for (; n != 1; n /= p[n]) fac[cnt++] = p[n];
    return;
  }
  if (miller(n))
    fac[cnt++] = n;
  else {
    long long x = rho(n);
    _factor(x);
    _factor(n / x);
  }
}
void dfs(long long x, int dep) {
  if (dep == _cnt)
    d.push_back(x);
  else {
    dfs(x, dep + 1);
    for (int i = 1; i <= _e[dep]; i++) dfs(x *= _pr[dep], dep + 1);
  }
}
void norm() {
  sort(fac, fac + cnt);
  _cnt = 0;
  for (int i = 0; i < cnt; i++)
    if (i == 0 || fac[i] != fac[i - 1])
      _pr[_cnt] = fac[i], _e[_cnt++] = 1;
    else
      _e[_cnt - 1]++;
}
vector<long long> getd() {
  d.clear();
  dfs(1, 0);
  return d;
}
vector<long long> factor(long long n) {
  cnt = 0;
  _factor(n);
  norm();
  return getd();
}
vector<pair<long long, long long> > factorG(long long n) {
  cnt = 0;
  _factor(n);
  norm();
  vector<pair<long long, long long> > d;
  for (int i = 0; i < _cnt; i++) d.push_back(make_pair(_pr[i], _e[i]));
  return d;
}
bool is_primitive(long long a, long long p) {
  assert(miller(p));
  vector<pair<long long, long long> > D = factorG(p - 1);
  for (int i = 0; i < ((int)(D).size()); i++)
    if (powl(a, (p - 1) / D[i].first, p) == 1) return 0;
  return 1;
}
long long simplify(long long n) {
  vector<pair<long long, long long> > d = factorG(n);
  long long c = 1;
  for (auto p : d) c = c * p.first;
  return c;
}
}  // namespace Factor
const int N = 1010000;
int n, v[N], simp[N], tr[N];
map<pair<int, int>, int> hs;
map<int, int> h2;
pair<int, int> big[N];
int main() {
  Factor::init(1000000);
  scanf("%d", &n);
  for (int i = 1; i < n + 1; i++) scanf("%d", v + i);
  for (int i = 1; i < n + 1; i++)
    if ((long long)i * i > n && Factor::miller(i)) {
      for (int j = i; j <= n; j += i) big[j] = make_pair(i, j / i);
    }
  for (int i = 1; i < n + 1; i++) simp[i] = Factor::simplify(i);
  big[1] = make_pair(1, 1);
  for (int i = 1; i < n + 1; i++) {
    if (big[i] == make_pair(0, 0))
      hs[make_pair(0, simp[i])]++;
    else {
      hs[make_pair(big[i].first, simp[big[i].second])]++;
      if (big[i].second == 1) {
        int c = n / i;
        if (i == 1) c = 1;
        h2[c]++;
      }
    }
  }
  for (int i = 1; i < n + 1; i++)
    if (v[i] != 0) {
      if ((big[i] == make_pair(0, 0)) != (big[v[i]] == make_pair(0, 0))) {
        puts("0");
        return 0;
      }
      if (big[i] == make_pair(0, 0) && big[v[i]] == make_pair(0, 0)) {
        if (simp[i] != simp[v[i]]) {
          puts("0");
          return 0;
        }
        hs[make_pair(0, simp[i])]--;
      } else {
        assert(big[i] != make_pair(0, 0) && big[v[i]] != make_pair(0, 0));
        int p1 = big[i].first, p2 = big[v[i]].first;
        int c1 = n / p1;
        if (p1 == 1) c1 = 1;
        int c2 = n / p2;
        if (p2 == 1) c2 = 1;
        if (c1 != c2) {
          puts("0");
          return 0;
        }
        if (tr[p1] != 0 && tr[p1] != p2) {
          puts("0");
          return 0;
        }
        if (tr[p1] == 0) h2[c1]--, tr[p1] = p2;
        if (simp[big[i].second] != simp[big[v[i]].second]) {
          puts("0");
          return 0;
        }
        hs[make_pair(big[i].first, simp[big[i].second])]--;
      }
    }
  long long way = 1;
  for (auto p : hs) {
    for (int i = 1; i < p.second + 1; i++) way = way * i % mod;
  }
  for (auto p : h2) {
    for (int i = 1; i < p.second + 1; i++) way = way * i % mod;
  }
  printf("%lld\n", way);
}
