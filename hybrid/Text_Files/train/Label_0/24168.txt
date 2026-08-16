#include <bits/stdc++.h>

using namespace std;

#define int long long
#define all(v) begin(v), end(v)
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define reps(i, s, n) for(int i = (int)(s); i < (int)(n); i++)

template<class T1, class T2> void chmin(T1 &a, T2 b){if(a>b)a=b;}
template<class T1, class T2> void chmax(T1 &a, T2 b){if(a<b)a=b;}

using pint = pair<int, int>;
using tint = tuple<int, int, int>;
using vint = vector<int>;

const int inf = 1LL << 55;
const int mod = 1e9 + 7;

int n, m, l, s, t;
int graph[303][303];
int sta[16], e[16];

int dp[1<<16][16];

signed main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);

  while(cin >> n >> m >> l >> s >> t, n) {
    --s;
    rep(i, 303) rep(j, 303) graph[i][j] = (i == j ? 0 : inf);
    rep(i, m) {
      int a, b, c;
      cin >> a >> b >> c; --a, --b;
      graph[a][b] = graph[b][a] = c;
    }
    rep(i, n) rep(j, n) rep(k, n) {
      chmin(graph[j][k], graph[j][i] + graph[i][k]);
    }
    rep(i, l)  {
      cin >> sta[i] >> e[i]; --sta[i];
    }
    rep(i, 1<<16) rep(j, 16) dp[i][j] = inf;
    rep(i, l) dp[1<<i][i] = graph[s][sta[i]] + e[i];
    rep(i, 1<<l) rep(j, l) {
      if(dp[i][j] == inf) continue;
      rep(k, l) if(!((i>>k)&1)) {
	chmin(dp[i|(1<<k)][k], dp[i][j] + graph[sta[j]][sta[k]] + e[k]);
      }
    }
    int ans = 0;
    rep(i, 1<<l) rep(j, l) {
      if(dp[i][j] != inf && dp[i][j] + graph[sta[j]][s] <= t) {
	chmax(ans, __builtin_popcount(i));
      }
    }
    cout << ans << endl;
  }

  return 0;
}