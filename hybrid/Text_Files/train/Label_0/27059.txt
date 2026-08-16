#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);
static const ll MOD = 10007;

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define DEC(i, s) for (int i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())

int n;
int edge[100010][2];
int cost[100010][2];
bool visit[10010];

ll dfs(int where, int parent, int lmax, ll ans) {
  if (visit[where]) { return ans; }
  visit[where] = true;
  REP(j, 2) {
    int to = edge[where][j];
    if (to == parent) { continue; }
    if (cost[where][j] == lmax) { ans++; }
    else if (cost[where][j] > lmax) {
      lmax = cost[where][j];
      ans = 1;
    }
    return dfs(to, where, lmax, ans);
  }
  assert(false);
  return 0;
}

int main() {
  while (scanf("%d", &n), n) {
    REP(i, n) {
      REP(j, 2) {
        scanf("%d %d", &edge[i][j], &cost[i][j]);
      }
    }
    MEMSET(visit, false);
    ll ans = 1;
    REP(i, n) {
      if (visit[i]) { continue; }
      ans = (ans * dfs(i, i, 0, 0)) % MOD;
    }
    printf("%lld\n", ans);
  }
}