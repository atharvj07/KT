#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

ll gcd(ll a, ll b) {
  if (b == 0) { return a; }
  return gcd(b, a % b);
}
ll lcm(ll a, ll b) {
  return a / gcd(a, b) * b;
}

//a x + b y = gcd(a, b)
long long extgcd(long long a, long long b, long long &x, long long &y) {
  long long g = a; x = 1; y = 0;
  if (b != 0) g = extgcd(b, a % b, y, x), y -= (a / b) * x;
  return g;
}


ll Mul(ll a, ll b, ll mod) {
  a %= mod;
  b %= mod;
  if (mod < 2e+9) { return a * b % mod; }
  ll ret = 0;
  while (b > 0) {
    if (b & 1) { ret = (ret + a) % mod; }
    a = (a + a) % mod;
    b >>= 1;
  }
  return ret;
}

// need extgcd
pair<ll, ll> PairChineseRemainderTherom(ll ans1, ll mod1, ll ans2, ll mod2) {
  ll g = gcd(mod1, mod2);
  ans1 %= mod1; ans1 = (ans1 + mod1) % mod1;
  ans2 %= mod2; ans2 = (ans2 + mod2) % mod2;
  if (ans1 % g != ans2 % g) { return make_pair(-1, -1); }
  const ll anss[2] = { ans1 / g, ans2 / g };
  const ll mods[2] = { mod1 / g, mod2 / g };
  ll all = mods[0] * mods[1];
  assert(all * g / g / mods[0] == mods[1]);
  ll ret = 0;
  for (int i = 0; i < 2; i++) {
    ll x, y;
    extgcd(mods[i], all / mods[i], x, y);
    y = (y + all) % all;
    ll v = Mul(y, anss[i], all);
    v = Mul(v, all / mods[i], all);
    ret = (ret + v) % all;
    assert(ret >= 0);
  }
  ret = ret * g + ans1 % g;
  return make_pair(ret, all * g);
}

// solve A x == B mod M
ll Divide(ll A, ll B, ll M) {
  A %= M; A = (A + M) % M;
  B %= M; B = (B + M) % M;
  ll g = gcd(A, M);
  if (B % g != 0) { return -1; }
  ll x, y;
  extgcd(A, M, x, y);
  ll n = x * B / g;
  ll dn = M / g;
  n -= n / dn * dn;
  if (n < 0) { n += dn; }
  return n;
}


pair<ll, ll> PairLinearCongruence(ll A1, ll B1, ll M1, ll A2, ll B2, ll M2) {
  A1 %= M1; A1 = (A1 + M1) % M1;
  B1 %= M1; B1 = (B1 + M1) % M1;
  A2 %= M2; A2 = (A2 + M2) % M2;
  B2 %= M2; B2 = (B2 + M2) % M2;
  if (A1 == 0 && B1 != 0) { return make_pair(-1, -1); }
  if (A2 == 0 && B2 != 0) { return make_pair(-1, -1); }
  if (A1 == 0 && A2 == 0) { return make_pair(0, 1); }
  if (A1 == 0) {
    swap(A1, A2);
    swap(B1, B2);
    swap(M1, M2);
  }
  ll g1 = gcd(A1, gcd(B1, M1));
  A1 /= g1; B1 /= g1; M1 /= g1;
  ll v1 = Divide(A1, B1, M1);
  if (v1 == -1) { return make_pair(-1, -1); }
  if (A2 == 0) {
    if (v1 == 0) { v1 = M1; }
    return make_pair(v1, M1);
  }
  ll g2 = gcd(A2, gcd(B2, M2));
  A2 /= g2; B2 /= g2; M2 /= g2;
  ll v2 = Divide(A2, B2, M2);
  if (v2 == -1) { return make_pair(-1, -1); }
  pair<ll, ll> ret = PairChineseRemainderTherom(v1, M1, v2, M2);
  if (ret.first == 0) { ret.first = ret.second; }
  return ret;
}


ll n, m, a, b, c, d;
int main() {
  while (scanf("%lld %lld %lld %lld %lld %lld", &m, &n, &a, &b, &c, &d) > 0) {
    a %= m; c %= m;
    b %= n; d %= n;
    ll e = 0;
    if (a == 0 && b == 0) {
      swap(a, c);
      swap(b, d);
    }
    if (a == 0 && b == 0) {
      puts("0");
      continue;
    } else if (a == 0) {
      e = n / gcd(b, n);
    } else if (b == 0) {
      e = m / gcd(a, m);
    } else {
      e = lcm(m / gcd(a, m), n / gcd(b, n));
    }
    if (c == 0 && d == 0) {
      printf("%lld\n", e - 1);
      continue;
    }

    ll sqnm = sqrt(n * m) + EPS;
    ll f = 1LL << 60;
    if (e <= sqrt(n * m)) {
      REP(g, e) {
        ll v = PairLinearCongruence(c, g * a % m, m, d, g * b % n, n).first;
        if (v == -1) { continue; }
        assert(v > 0);
        f = min(f, v);
      }
    } else {
      f = 1;
      FOREQ(i, 1, sqnm + 5) {
        ll v = PairLinearCongruence(a, i * c % m, m, b, i * d % n, n).first;
        if (v == -1) { continue; }
        f = i;
        break;
      }
    }
    printf("%lld\n", e * f - 1);
  }
}