#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<ll, ll> PLL;
#define _overload3(_1, _2, _3, name, ...) name
#define _rep(i, n) repi(i, 0, n)
#define repi(i, a, b) \
  for (int i = static_cast<int>(a); i < static_cast<int>(b); ++i)
#define rep(...) _overload3(__VA_ARGS__, repi, _rep, ) (__VA_ARGS__)  // NOLINT


const ull WILD_CARD = 8;
ull N;
vector<ull> s, t;

void setbit(vector<vector<ull>> &a, ull i, ull j, ull value) {
  if (a[i][j] == value || a[i][j] == WILD_CARD) {
    a[i][j] = value;
  } else {
    cout << -1 << endl;
    exit(0);
  }
}

vector<vector<ull>> solve(const vector<ull> &u, const vector<ull> &v) {
  vector<vector<ull>> a(N, vector<ull>(N, WILD_CARD));

  // phase #1
  rep(i, N) {
    if (s[i] != u[i]) {
      //cout << "i=" << i << endl;
      rep(j, N)
        setbit(a, i, j, u[i]);
    }
  }
  rep(j, N) {
    if (t[j] != v[j]) {
      //cout << "j=" << j << endl;
      rep(i, N)
        setbit(a, i, j, v[j]);
    }
  }
  //cout << "phase #1" << endl;
  //rep(i, N) {
  //  rep(j, N) {
  //    cout << a[i][j] << " ";
  //  }
  //  cout << endl;
  //}

  // phase #2
  bool changed;
  do {
    changed = false;
    rep(i, N) {
      if (s[i] != u[i]) continue; // 対象外
      map<ll, vector<ll>> mp;
      rep(j, N)
        mp[a[i][j]].push_back(j);
      //cout << "i=" << i << " " << mp[WILD_CARD].size() << endl;

      if (mp[u[i]].size() >= 1) continue; // すでにOK
      if (mp[WILD_CARD].size() == 0) { cout << -1 << endl; exit(0); } // NG
      if (mp[WILD_CARD].size() == 1) { changed = true; setbit(a, i, mp[WILD_CARD][0], u[i]); } // そこをUにする
      if (mp[WILD_CARD].size() >= 2) continue; // 何もしない
    }

    rep(j, N) {
      if (t[j] != v[j]) continue; // 対象外
      map<ll, vector<ll>> mp;
      rep(i, N)
        mp[a[i][j]].push_back(i);
      //cout << "j=" << j << " " << mp[WILD_CARD].size() << endl;

      if (mp[v[j]].size() >= 1) continue; // すでにOK
      if (mp[WILD_CARD].size() == 0) { cout << -1 << endl; exit(0); } // NG
      if (mp[WILD_CARD].size() == 1) { changed = true; setbit(a, mp[WILD_CARD][0], j, v[j]); } // そこをUにする
      if (mp[WILD_CARD].size() >= 2) continue; // 何もしない
    }

  } while (changed);

  //cout << "phase #2" << endl;
  //rep(i, N) {
  //  rep(j, N) {
  //    cout << a[i][j] << " ";
  //  }
  //  cout << endl;
  //}

  // phase #3
  set<int> is, js;
  rep(i, N) rep(j, N) {
    if (a[i][j] == WILD_CARD) {
      is.insert(i);
      js.insert(j);
    }
  }

  //cout << "is: "; for (auto i : is) { cout << i << " "; } cout << endl;
  //cout << "js: "; for (auto j : js) { cout << j << " "; } cout << endl;

  ull p = 0;
  for (auto i : is) {
    ull q = p;
    for (auto j : js) {
      setbit(a, i, j, q);
      q = 1 - q;
    }
    p = 1 - p;
  }

  //cout << "phase #3" << endl;
  //rep(i, N) {
  //  rep(j, N) {
  //    cout << a[i][j] << " ";
  //  }
  //  cout << endl;
  //}

  return a;
}

signed main() {
  cin >> N;
  s.resize(N);
  t.resize(N);
  vector<ull> u(N), v(N);
  rep(i, N) cin >> s[i];
  rep(i, N) cin >> t[i];
  rep(i, N) cin >> u[i];
  rep(i, N) cin >> v[i];

  vector<vector<ull>> a(N, vector<ull>(N, 0));

  rep(k, 64) {
    vector<ull> u2(N), v2(N);
    rep(i, N) {
      u2[i] = (u[i] >> k) & 1;
      v2[i] = (v[i] >> k) & 1;
    }
    auto a2 = solve(u2, v2);
    rep(i, N)
      rep(j, N)
        a[i][j] |= ((a2[i][j] & 1) << k);
  }

  rep(i, N) {
    rep(j, N) {
      cout << a[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
