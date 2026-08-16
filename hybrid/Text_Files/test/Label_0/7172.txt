#include <bits/stdc++.h>

using namespace std;

const void chmax(double &a, double b)
{
  a = max(a, b);
}


struct edge
{
  int to, cost, v;
};

int main()
{
  int N, M, P;
  vector< edge > g[200];

  cin >> N >> M >> P;
  for(int i = 0; i < M; i++) {
    int s, t, d, v;
    cin >> s >> t >> d >> v;
    --s, --t;
    g[s].emplace_back((edge) {t, d, v});
    g[t].emplace_back((edge) {s, d, v});
  }

  double dp[1001][200];
  fill_n(*dp, 1001 * 200, -1);
  dp[0][0] = 0;
  for(int i = 0; i < P; i++) {
    for(int j = 0; j < N; j++) {
      if(dp[i][j] < 0) continue;
      for(auto &e : g[j]) {
        chmax(dp[i + 1][j], dp[i][j] + (double) e.v / e.cost);
        if(i + e.cost <= P)
          chmax(dp[i + e.cost][e.to], dp[i][j] + e.v);
      }
    }
  }

  cout << fixed << setprecision(10) << dp[P][0] << endl;
}