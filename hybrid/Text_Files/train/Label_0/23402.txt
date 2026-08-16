#include <bits/stdc++.h>
using namespace std;
using ll = long long;
template <class t, class u>
void chmax(t& first, u second) {
  if (first < second) first = second;
}
template <class t, class u>
void chmin(t& first, u second) {
  if (second < first) first = second;
}
template <class t>
using vc = vector<t>;
template <class t>
using vvc = vc<vc<t>>;
using pi = pair<ll, ll>;
using vi = vc<ll>;
template <class t, class u>
ostream& operator<<(ostream& os, const pair<t, u>& p) {
  return os << "{" << p.first << "," << p.second << "}";
}
template <class t>
ostream& operator<<(ostream& os, const vc<t>& v) {
  os << "{";
  for (auto e : v) os << e << ",";
  return os << "}";
}
using uint = unsigned;
using ull = unsigned long long;
template <class t, size_t n>
ostream& operator<<(ostream& os, const array<t, n>& first) {
  return os << vc<t>(first.begin(), first.end());
}
template <ll i, class T>
void print_tuple(ostream&, const T&) {}
template <ll i, class T, class H, class... Args>
void print_tuple(ostream& os, const T& t) {
  if (i) os << ",";
  os << get<i>(t);
  print_tuple<i + 1, T, Args...>(os, t);
}
template <class... Args>
ostream& operator<<(ostream& os, const tuple<Args...>& t) {
  os << "{";
  print_tuple<0, tuple<Args...>, Args...>(os, t);
  return os << "}";
}
template <class t>
void print(t x, ll suc = 1) {
  cout << x;
  if (suc == 1) cout << "\n";
  if (suc == 2) cout << " ";
}
ll read() {
  ll i;
  cin >> i;
  return i;
}
vi readvi(ll n, ll off = 0) {
  vi v(n);
  for (ll i = ll(0); i < ll(n); i++) v[i] = read() + off;
  return v;
}
pi readpi(ll off = 0) {
  ll first, second;
  cin >> first >> second;
  return pi(first + off, second + off);
}
template <class T>
void print(const vector<T>& v, ll suc = 1) {
  for (ll i = ll(0); i < ll(v.size()); i++)
    print(v[i], i == ll(v.size()) - 1 ? suc : 2);
}
string readString() {
  string s;
  cin >> s;
  return s;
}
template <class T>
T sq(const T& t) {
  return t * t;
}
void yes(bool ex = true) {
  cout << "Yes"
       << "\n";
  if (ex) exit(0);
}
void no(bool ex = true) {
  cout << "No"
       << "\n";
  if (ex) exit(0);
}
void possible(bool ex = true) {
  cout << "Possible"
       << "\n";
  if (ex) exit(0);
}
void impossible(bool ex = true) {
  cout << "Impossible"
       << "\n";
  if (ex) exit(0);
}
constexpr ll ten(ll n) { return n == 0 ? 1 : ten(n - 1) * 10; }
const ll infLL = LLONG_MAX / 3;
const ll inf = infLL;
ll topbit(signed t) { return t == 0 ? -1 : 31 - __builtin_clz(t); }
ll topbit(ll t) { return t == 0 ? -1 : 63 - __builtin_clzll(t); }
ll botbit(signed first) { return first == 0 ? 32 : __builtin_ctz(first); }
ll botbit(ll first) { return first == 0 ? 64 : __builtin_ctzll(first); }
ll popcount(signed t) { return __builtin_popcount(t); }
ll popcount(ll t) { return __builtin_popcountll(t); }
bool ispow2(ll i) { return i && (i & -i) == i; }
ll mask(ll i) { return (ll(1) << i) - 1; }
bool inc(ll first, ll second, ll c) { return first <= second && second <= c; }
template <class t>
void mkuni(vc<t>& v) {
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
}
ll rand_int(ll l, ll r) {
  static mt19937_64 gen(chrono::steady_clock::now().time_since_epoch().count());
  return uniform_int_distribution<ll>(l, r)(gen);
}
template <class t>
void myshuffle(vc<t>& first) {
  for (ll i = ll(0); i < ll(ll(first.size())); i++)
    swap(first[i], first[rand_int(0, i)]);
}
template <class t>
ll lwb(const vc<t>& v, const t& first) {
  return lower_bound(v.begin(), v.end(), first) - v.begin();
}
vvc<ll> readGraph(ll n, ll m) {
  vvc<ll> g(n);
  for (ll i = ll(0); i < ll(m); i++) {
    ll first, second;
    cin >> first >> second;
    first--;
    second--;
    g[first].push_back(second);
    g[second].push_back(first);
  }
  return g;
}
vvc<ll> readTree(ll n) { return readGraph(n, n - 1); }
struct modinfo {
  uint mod, root;
};
template <modinfo const& ref>
struct modular {
  static constexpr uint const& mod = ref.mod;
  static modular root() { return modular(ref.root); }
  uint v;
  modular(ll vv = 0) { s(vv % mod + mod); }
  modular& s(uint vv) {
    v = vv < mod ? vv : vv - mod;
    return *this;
  }
  modular operator-() const { return modular() - *this; }
  modular& operator+=(const modular& rhs) { return s(v + rhs.v); }
  modular& operator-=(const modular& rhs) { return s(v + mod - rhs.v); }
  modular& operator*=(const modular& rhs) {
    v = ull(v) * rhs.v % mod;
    return *this;
  }
  modular& operator/=(const modular& rhs) { return *this *= rhs.inv(); }
  modular operator+(const modular& rhs) const { return modular(*this) += rhs; }
  modular operator-(const modular& rhs) const { return modular(*this) -= rhs; }
  modular operator*(const modular& rhs) const { return modular(*this) *= rhs; }
  modular operator/(const modular& rhs) const { return modular(*this) /= rhs; }
  modular pow(ll n) const {
    modular res(1), x(*this);
    while (n) {
      if (n & 1) res *= x;
      x *= x;
      n >>= 1;
    }
    return res;
  }
  modular inv() const { return pow(mod - 2); }
  friend modular operator+(ll x, const modular& y) { return modular(x) + y; }
  friend modular operator-(ll x, const modular& y) { return modular(x) - y; }
  friend modular operator*(ll x, const modular& y) { return modular(x) * y; }
  friend modular operator/(ll x, const modular& y) { return modular(x) / y; }
  friend ostream& operator<<(ostream& os, const modular& m) {
    return os << m.v;
  }
  friend istream& operator>>(istream& is, modular& m) {
    ll x;
    is >> x;
    m = modular(x);
    return is;
  }
  bool operator<(const modular& r) const { return v < r.v; }
  bool operator==(const modular& r) const { return v == r.v; }
  bool operator!=(const modular& r) const { return v != r.v; }
  explicit operator bool() const { return v; }
};
extern constexpr modinfo base{1000000007, 0};
using mint = modular<base>;
const ll vmax = (1 << 21) + 10;
mint fact[vmax], finv[vmax], invs[vmax];
void initfact() {
  fact[0] = 1;
  for (ll i = ll(1); i < ll(vmax); i++) {
    fact[i] = fact[i - 1] * i;
  }
  finv[vmax - 1] = fact[vmax - 1].inv();
  for (ll i = vmax - 2; i >= 0; i--) {
    finv[i] = finv[i + 1] * (i + 1);
  }
  for (ll i = vmax - 1; i >= 1; i--) {
    invs[i] = finv[i] * fact[i - 1];
  }
}
mint choose(ll n, ll k) { return fact[n] * finv[n - k] * finv[k]; }
mint binom(ll first, ll second) {
  return fact[first + second] * finv[first] * finv[second];
}
mint catalan(ll n) {
  return binom(n, n) - (n - 1 >= 0 ? binom(n - 1, n + 1) : 0);
}
template <class N>
struct segtree {
  vc<N> buf;
  ll s;
  template <class t>
  segtree(vc<t> first) {
    ll n = first.size();
    s = 1;
    while (s < n) {
      s *= 2;
    }
    buf.resize(s * 2);
    for (ll i = ll(0); i < ll(n); i++) buf[s + i] = N(first[i]);
    for (ll i = ll(s) - 1; i >= ll(1); i--)
      buf[i] = N::merge(buf[i * 2], buf[i * 2 + 1]);
  }
  void set(ll i, const N& t) {
    i += s;
    buf[i] = t;
    while (i >>= 1) buf[i] = N::merge(buf[i * 2], buf[i * 2 + 1]);
  }
  N get(ll second, ll e) {
    assert(second <= e);
    N lf, rt;
    for (ll l = second + s, r = e + s; l < r; l >>= 1, r >>= 1) {
      if (l & 1) {
        lf = N::merge(lf, buf[l]);
        l++;
      }
      if (r & 1) {
        r--;
        rt = N::merge(buf[r], rt);
      }
    }
    return N::merge(lf, rt);
  }
  N getall() { return buf[1]; }
};
const ll id[3][4]{{-1, 0, 1, 2}, {-1, -1, 3, 4}, {-1, -1, -1, 5}};
using T = tuple<mint, mint, mint>;
struct N {
  mint buf[6];
  N(const T& t = T()) {
    buf[0] = get<0>(t);
    buf[3] = get<1>(t);
    buf[5] = get<2>(t);
  }
  static N merge(const N& x, const N& y) {
    N res;
    for (ll i = ll(0); i < ll(6); i++) res.buf[i] = x.buf[i] + y.buf[i];
    for (ll i = ll(0); i < ll(3); i++)
      for (ll j = ll(i + 1); j < ll(3); j++)
        for (ll k = ll(j + 1); k < ll(4); k++)
          res.buf[id[i][k]] += x.buf[id[i][j]] * y.buf[id[j][k]];
    return res;
  }
};
template <class t>
struct BIT {
  vc<t> buf;
  ll s;
  BIT(ll n = 0) { init(n); }
  void init(ll n) { buf.assign(s = n, 0); }
  void add(ll i, t v) {
    for (; i < s; i += (i + 1) & (-i - 1)) buf[i] += v;
  }
  t get(ll i) {
    t res = 0;
    for (; i >= 0; i -= (i + 1) & (-i - 1)) res += buf[i];
    return res;
  }
  t sum(ll second, ll e) { return get(e - 1) - get(second - 1); }
  ll kth(ll k) {
    ll res = 0;
    for (ll i = topbit(s); i >= 0; i--) {
      ll w = res + (1 << i);
      if (w <= s && buf[w - 1] <= k) {
        k -= buf[w - 1];
        res = w;
      }
    }
    return res;
  }
  ll kth_helper(ll k, ll i) { return kth(k + get(i - 1)); }
};
signed main() {
  cin.tie(0);
  ios::sync_with_stdio(0);
  cout << fixed << setprecision(20);
  ll n;
  cin >> n;
  vi first = readvi(n);
  vi vs = first;
  mkuni(vs);
  ll h = ll(vs.size());
  vc<segtree<N>> ss;
  vvc<T> rw;
  vvc<ll> idx(h);
  for (ll i = ll(0); i < ll(n); i++) idx[lwb(vs, first[i])].push_back(i);
  BIT<ll> bit(n);
  for (ll lv = ll(0); lv < ll(h); lv++) {
    ll s = ll(idx[lv].size());
    vc<T> tmp(s);
    for (ll i = ll(0); i < ll(s); i++) {
      tmp[i] =
          T(bit.sum(0, idx[lv][i]) + i, 1, bit.sum(idx[lv][i], n) + s - 1 - i);
    }
    for (ll i = ll(0); i < ll(s); i++) {
      bit.add(idx[lv][i], 1);
    }
    ss.emplace_back(tmp);
    rw.emplace_back(tmp);
  }
  mint ans = 0;
  for (ll lv = ll(0); lv < ll(h); lv++) ans += ss[lv].getall().buf[2];
  ll m;
  cin >> m;
  for (ll _ = ll(0); _ < ll(m); _++) {
    ll t, x;
    cin >> t >> x;
    x--;
    ll lv = lwb(vs, first[x]);
    ll i = lwb(idx[lv], x);
    ans -= ss[lv].getall().buf[2];
    if (t == 1) {
      ss[lv].set(i, N());
    } else {
      ss[lv].set(i, N(rw[lv][i]));
    }
    ans += ss[lv].getall().buf[2];
    print(ans);
  }
}
