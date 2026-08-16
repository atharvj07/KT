#include <bits/stdc++.h>
using namespace std;
const int nmax = 200005;
struct node {
  long long p, s, val;
} arb[4 * nmax];
const long long mod = 998244353;
set<pair<int, int> > s[nmax];
pair<int, int> P;
set<pair<int, int> >::iterator it, it1;
int n, M, st, dr, lst, i, tip, x;
long long tot;
void push(int nod, int l, int r) {
  int m = (l + r) / 2;
  if (l == r) {
    arb[nod].val = (1LL * arb[nod].val * arb[nod].p + arb[nod].s) % mod;
  } else {
    arb[2 * nod].p *= arb[nod].p;
    arb[2 * nod + 1].p *= arb[nod].p;
    arb[2 * nod].s = ((1LL * arb[2 * nod].s * arb[nod].p) + arb[nod].s) % mod;
    arb[2 * nod + 1].s =
        ((1LL * arb[2 * nod + 1].s * arb[nod].p) + arb[nod].s) % mod;
    arb[2 * nod].s %= mod;
    arb[2 * nod].p %= mod;
    arb[2 * nod + 1].s %= mod;
    arb[2 * nod + 1].p %= mod;
    long long lst = m - l + 1, ldr = r - m;
    arb[nod].val = (1LL * arb[2 * nod].val * arb[2 * nod].p % mod +
                    1LL * lst * arb[2 * nod].s % mod +
                    1LL * arb[2 * nod + 1].val * arb[2 * nod + 1].p % mod +
                    1LL * ldr * arb[2 * nod + 1].s % mod) %
                   mod;
  }
  arb[nod].p = 1;
  arb[nod].s = 0;
}
void update(int nod, int l, int r, int st, int dr, long long add,
            long long mul) {
  if (arb[nod].s || arb[nod].p != 1) {
    push(nod, l, r);
  }
  if (st <= l && r <= dr) {
    arb[nod].s = (arb[nod].s + add) % mod;
    if (mul) arb[nod].p = (arb[nod].p * mul) % mod;
    return;
  }
  int m = (l + r) / 2;
  if (st <= m) update(2 * nod, l, m, st, dr, add, mul);
  if (m < dr) update(2 * nod + 1, m + 1, r, st, dr, add, mul);
  long long lst = m - l + 1, ldr = r - m;
  arb[nod].val = (1LL * arb[2 * nod].val * arb[2 * nod].p % mod +
                  1LL * lst * arb[2 * nod].s % mod +
                  1LL * arb[2 * nod + 1].val * arb[2 * nod + 1].p % mod +
                  1LL * ldr * arb[2 * nod + 1].s % mod) %
                 mod;
}
void query(int nod, int l, int r) {
  if (arb[nod].s || arb[nod].p != 1) {
    push(nod, l, r);
  }
  if (st <= l && r <= dr) {
    tot += arb[nod].val;
    tot %= mod;
    return;
  }
  int m = (l + r) / 2;
  if (st <= m) query(2 * nod, l, m);
  if (m < dr) query(2 * nod + 1, m + 1, r);
  long long lst = m - l + 1, ldr = r - m;
  arb[nod].val = (1LL * arb[2 * nod].val * arb[2 * nod].p % mod +
                  1LL * lst * arb[2 * nod].s % mod +
                  1LL * arb[2 * nod + 1].val * arb[2 * nod + 1].p % mod +
                  1LL * ldr * arb[2 * nod + 1].s % mod) %
                 mod;
}
void add(int l, int r, int x) {
  it = s[x].lower_bound({l, r});
  lst = l;
  if (it != s[x].begin()) {
    it1 = it;
    it1--;
    if ((*it1).second >= l) it = it1;
  }
  if ((*it).first <= l && (*it).second >= r) {
    update(1, 1, n, l, r, 0, 2);
    return;
  }
  while (it != s[x].end() && (*it).first <= r) {
    P = (*it);
    if (P.first >= l && P.second <= r) {
      update(1, 1, n, P.first, P.second, 0, 2);
      if (lst <= P.first - 1) update(1, 1, n, lst, P.first - 1, 1, 0);
    }
    if (P.first < l && P.second >= l) {
      update(1, 1, n, l, P.second, 0, 2);
      l = P.first;
    }
    if (P.first <= r && P.second > r) {
      if (lst <= P.first - 1) update(1, 1, n, lst, P.first - 1, 1, 0);
      update(1, 1, n, P.first, r, 0, 2);
      r = P.second;
    }
    lst = P.second + 1;
    s[x].erase(P);
    it = s[x].lower_bound({l, r});
  }
  if (lst <= r) update(1, 1, n, lst, r, 1, 0);
  s[x].insert({l, r});
}
int main() {
  ios_base::sync_with_stdio(false);
  cin >> n >> M;
  for (i = 1; i <= 4 * n; i++) arb[i].p = 1;
  for (int cnt = 1; cnt <= M; cnt++) {
    cin >> tip >> st >> dr;
    if (tip == 1) {
      cin >> x;
      add(st, dr, x);
    } else {
      tot = 0;
      query(1, 1, n);
      cout << tot << '\n';
    }
  }
  return 0;
}
