#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repr(i, n) for (int i = (n); i >= 0; --i)
#define FOR(i, m, n) for (int i = (m); i < (n); ++i)
#define FORR(i, m, n) for (int i = (m); i >= (n); --i)
#define equals(a, b) (fabs((a) - (b)) < EPS)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ll mod = 1000000007;
//const ll mod = 998244353;
const int inf = 1e9 + 10;
const ll INF = 1e18;
const ld EPS = 1e-10;
const int dx[8] = {1, 0, -1, 0, 1, -1, -1, 1};
const int dy[8] = {0, 1, 0, -1, 1, 1, -1, -1};
template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }

//マンハッタン距離計算
ll calc(ll x0, ll y0, ll x1, ll y1) {
  return abs(x0 - x1) + abs(y0 - y1);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(25);

  //inputs
  int n;
  ll m, w, t;
  cin >> n >> m >> w >> t;
  map<string, ll> s;
  vector<ll> v(m), p(m);
  rep(i, m) {
    string si;
    cin >> si >> v[i] >> p[i];
    s[si] = i;
  }
  vector<ll> l(n), x(n), y(n);
  vector<vector<ll>> r(n), q(n);
  rep(i, n) {
    cin >> l[i] >> x[i] >> y[i];
    rep(j, l[i]) {
      string rij;
      ll qij;
      cin >> rij >> qij;
      r[i].push_back(s[rij]);
      q[i].push_back(qij);
    }
  }

  //preprocessing, qijを転売することで得られる利益に変換、負数になる場合は便宜上0にする。
  rep(i, n) {
    rep(j, l[i]) {
      q[i][j] = p[r[i][j]] - q[i][j];
      chmax(q[i][j], 0LL);
      //cout << q[i][j] << '\n';
    }
  }
  //立ち寄る街を決め打ちした際の最小移動距離, 最大利益
  vector<ll> dist((1 << n), INF), maxv((1 << n), 0);
  //bitが立っていたら寄る、そうでなければよらないで全探索
  FOR(i, 1, (1 << n)) {
    //街の集合
    vector<int> vs;
    //商品の{重さ、利益}
    vector<pair<ll, ll>> product(m);
    rep(j, m) product[j] = {v[j], 0};
    //訪れた街で商品を買った場合の利益を更新
    rep(j, n) {
      if (i >> j & 1) {
        vs.push_back(j);
        rep(k, l[j]) {
          chmax(product[r[j][k]].second, q[j][k]);
        }
      }
    }
    int vsn = vs.size();
    //ナップザック問題1:重さwの制限で利益を最大化
    vector<ll> dp(w + 1, 0);
    rep(j, m) {
      rep(k, w + 1 - product[j].first) {
        chmax(dp[k + product[j].first], dp[k] + product[j].second);
      }
    }
    maxv[i] = dp[w];
    //cout << maxv[i] << '\n';
    //最小距離を計算、全探索
    while (1) {
      ll resdist = calc(0, 0, x[vs[0]], y[vs[0]]) + calc(0, 0, x[vs[vsn - 1]], y[vs[vsn - 1]]);
      rep(i, vsn - 1) resdist += calc(x[vs[i]], y[vs[i]], x[vs[i + 1]], y[vs[i + 1]]);
      chmin(dist[i], resdist);
      if (!next_permutation(vs.begin(), vs.end())) break;
    }
    //cout << dist[i] << '\n';
  }
  //ナップザック問題２:時間tの制限で利益を最大化
  vector<ll> dp(t + 1, 0);
  FOR(i, 1, (1 << n)) {
    rep(j, t + 1 - dist[i]) {
      chmax(dp[j + dist[i]], dp[j] + maxv[i]);
    }
  }
  //output
  cout << dp[t] << '\n';



  







  
  return 0;
}
