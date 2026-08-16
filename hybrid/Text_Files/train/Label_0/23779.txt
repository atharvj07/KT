#include <bits/stdc++.h>
using namespace std;
constexpr int INF = INT_MAX / 2;
constexpr int MAXN = 100;
constexpr int MAXSS = 1000;
constexpr int MAXBS = 1000;
static int N;
static int numSpaceships, numBases;
static int costAttacked, costFake;
static vector<int> hkp[MAXSS];
class Hopcroft {
 private:
  vector<int> A, B, lev;
  vector<int> used;
  vector<vector<int>> adj;
  vector<int> HT;
  queue<int> q;
  int n, m;
  void bfs() {
    for (int i = 1; i <= n; i++) {
      if (!used[i]) {
        lev[i] = 0;
        q.push(i);
      } else
        lev[i] = INF;
    }
    while (!q.empty()) {
      const int a = q.front();
      q.pop();
      for (auto b : adj[a]) {
        if (B[b] != -1 && lev[B[b]] == INF) {
          lev[B[b]] = lev[a] + 1;
          q.push(B[b]);
        }
      }
    }
    fill(HT.begin(), HT.end(), 0);
  }
  bool dfs(int a) {
    for (int &i = HT[a]; i < adj[a].size(); ++i) {
      const int b = adj[a][i];
      if (B[b] == -1 || lev[B[b]] == lev[a] + 1 && dfs(B[b])) {
        used[a] = 1;
        A[a] = b;
        B[b] = a;
        return 1;
      }
    }
    return 0;
  }

 public:
  Hopcroft(int n, int m)
      : n(n),
        m(m),
        A(n + 1, -1),
        lev(n + 1),
        used(n + 1),
        adj(n + 1),
        B(m + 1, -1),
        HT(n + 1) {}
  int solve() {
    int ret = 0;
    while (1) {
      bfs();
      int flow = 0;
      for (int i = 1; i <= n; i++)
        if (!used[i] and dfs(i)) flow++;
      if (flow == 0) break;
      ret += flow;
    }
    return ret;
  }
  void pushadj(int a, int b) { adj[a].push_back(b); }
};
static int64_t process1() {
  static int F[MAXN][MAXN];
  static int spaceships[MAXSS][3];
  static int bases[MAXBS][2];
  int m;
  cin >> N >> m;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      F[i][j] = (i == j ? 0 : 999);
    }
  }
  while (m--) {
    int x, y;
    cin >> x >> y;
    if (x == y) continue;
    --x;
    --y;
    F[x][y] = F[y][x] = 1;
  }
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      const int fji = F[j][i];
      if (j == i || fji == 999) continue;
      for (int k = 0; k < N; ++k) {
        const int c = fji + F[i][k];
        if (F[j][k] > c) F[j][k] = c;
      }
    }
  }
  cin >> numSpaceships >> numBases >> costAttacked >> costFake;
  for (int i = 0; i < numSpaceships; ++i) {
    int idx, a, f;
    cin >> idx >> a >> f;
    spaceships[i][0] = idx - 1;
    spaceships[i][1] = a;
    spaceships[i][2] = f;
  }
  for (int i = 0; i < numBases; ++i) {
    int idx, d;
    cin >> idx >> d;
    bases[i][0] = idx - 1;
    bases[i][1] = d;
  }
  Hopcroft hp(numSpaceships, numBases);
  for (int i = 0; i < numSpaceships; ++i) {
    const int idx1 = spaceships[i][0];
    const int power = spaceships[i][1];
    const int fuel = spaceships[i][2];
    for (int j = 0; j < numBases; ++j) {
      if (power < bases[j][1]) continue;
      const int idx2 = bases[j][0];
      const int dist = F[idx1][idx2];
      if (dist == 999) continue;
      if (dist > fuel) continue;
      hp.pushadj(i + 1, j + 1);
    }
  }
  const int ans = hp.solve();
  const int64_t curCost = ans * (int64_t)costAttacked;
  if (costFake > costAttacked) return curCost;
  const int64_t fakeCost = numSpaceships * (int64_t)costFake;
  return min(fakeCost, curCost);
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  const auto ans = process1();
  cout << ans << '\n';
}
