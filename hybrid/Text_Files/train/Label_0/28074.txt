#include <bits/stdc++.h>
using namespace std;
const int MAX_BUF_SIZE = 16384;
char BUFOR[MAX_BUF_SIZE];
int BUF_SIZE, BUF_POS;
char ZZZ;
const int MXN = 6 * 50010;
const int C = 262144;
const int INF = 1000000001;
namespace SAT2 {
vector<int> G[MXN], GT[MXN], H[MXN], vert[MXN];
int pre[MXN], skl[MXN];
vector<int> fu;
class SAT2 {
  SAT2() {}
  int n, czas, skla;
  int neg(int v1) { return (v1 + n) % (2 * n); }
  void addEdge(int v1, int v2) {
    G[neg(v1)].push_back(v2);
    GT[v2].push_back(neg(v1));
    G[neg(v2)].push_back(v1);
    GT[v1].push_back(neg(v2));
  }
  void dfs(int x) {
    pre[x] = ++czas;
    for (__typeof((G[x]).begin()) it = ((G[x]).begin()); it != (G[x]).end();
         ++it)
      if (!pre[*it]) dfs(*it);
    fu.push_back(x);
  }
  void dfs2(int x) {
    skl[x] = skla;
    vert[skla].push_back(x);
    for (__typeof((GT[x]).begin()) it = ((GT[x]).begin()); it != (GT[x]).end();
         ++it)
      if (!skl[*it]) dfs2(*it);
  }
  void dfs3(int x) {
    pre[x] = 1;
    for (__typeof((H[x]).begin()) it = ((H[x]).begin()); it != (H[x]).end();
         ++it)
      if (!pre[*it]) dfs3(*it);
    fu.push_back(x);
  }
  void clear() {
    fu.clear();
    for (int i = (0); i <= (2 * n); i++) pre[i] = skl[i] = 0;
    for (int i = (0); i <= (2 * n); i++) {
      G[i].clear();
      GT[i].clear();
      vert[i].clear();
      H[i].clear();
    }
  }

 public:
  SAT2(int _n) {
    czas = 0;
    skla = 0;
    n = _n;
  }
  void add(int v1, bool pos1, int v2, bool pos2) {
    addEdge((pos1 ? neg(v1) : v1), (pos2 ? neg(v2) : v2));
  }
  pair<bool, vector<bool> > solve() {
    for (int i = (0); i <= (2 * n - 1); i++)
      if (!pre[i]) dfs(i);
    for (int i = ((int)(fu).size() - 1); i >= (0); i--) {
      int w = fu[i];
      if (!skl[w]) {
        skla++;
        dfs2(w);
      }
    }
    skla++;
    for (int i = (0); i <= (n - 1); i++)
      if (skl[i] == skl[i + n]) {
        clear();
        return make_pair(false, vector<bool>());
      }
    for (int i = (0); i <= (2 * n - 1); i++) {
      for (__typeof((G[i]).begin()) it = ((G[i]).begin()); it != (G[i]).end();
           ++it)
        H[skl[i]].push_back(skl[*it]);
    }
    fu.clear();
    for (int i = (0); i <= (skla); i++) pre[i] = 0;
    for (int i = (0); i <= (skla - 1); i++)
      if (!pre[i]) dfs3(i);
    vector<bool> res(2 * n, 0);
    vector<int> tmp(skla + 1, -1);
    for (int i = ((int)(fu).size() - 1); i >= (0); i--) {
      int w = fu[i];
      if (tmp[w] == -1) tmp[w] = 0;
      if (tmp[w] == 1)
        for (__typeof((H[w]).begin()) it = ((H[w]).begin()); it != (H[w]).end();
             ++it)
          tmp[*it] = 1;
      for (__typeof((vert[w]).begin()) it = ((vert[w]).begin());
           it != (vert[w]).end(); ++it) {
        tmp[skl[neg(*it)]] = !tmp[w];
        res[*it] = tmp[w];
        res[neg(*it)] = !tmp[w];
      }
    }
    clear();
    return make_pair(true, res);
  }
};
}  // namespace SAT2
int n2, m;
vector<pair<int, pair<int, int> > > G2[MXN];
int c[MXN], t[MXN];
pair<bool, vector<bool> > check(int second) {
  SAT2::SAT2 SAT(3 * m);
  for (int i = (0); i <= (m - 1); i++)
    if (t[i] > second) SAT.add(i, 1, i, 1);
  for (int i = (1); i <= (n2); i++) {
    for (int j = (0); j <= ((int)(G2[i]).size() - 1); j++) {
      int iter = j;
      while (iter < (int)(G2[i]).size() && G2[i][j].first == G2[i][iter].first)
        iter++;
      if (iter - j > 2)
        return make_pair(false, vector<bool>());
      else if (iter - j == 2)
        SAT.add(G2[i][j].second.second, 0, G2[i][j + 1].second.second, 0);
      j = iter - 1;
    }
    int last = -1;
    for (int j = (0); j <= ((int)(G2[i]).size() - 1); j++) {
      int ei = G2[i][j].second.second;
      int pi = ei;
      if (i < G2[i][j].second.first)
        pi += m;
      else
        pi += 2 * m;
      SAT.add(pi, 1, ei, 1);
      if (last != -1) {
        SAT.add(ei, 1, last, 0);
        SAT.add(pi, 1, last, 0);
      }
      last = pi;
    }
  }
  return SAT.solve();
}
void test() {
  scanf("%d %d", &n2, &m);
  int mx = 0;
  for (int i = (1); i <= (m); i++) {
    int a, b;
    scanf("%d %d %d %d", &a, &b, &c[i - 1], &t[i - 1]);
    mx = max(mx, t[i - 1]);
    G2[a].push_back(make_pair(c[i - 1], make_pair(b, i - 1)));
    G2[b].push_back(make_pair(c[i - 1], make_pair(a, i - 1)));
  }
  for (int i = (1); i <= (n2); i++) sort((G2[i]).begin(), (G2[i]).end());
  int res = INF;
  int L = 0, R = mx;
  vector<bool> ans;
  while (L <= R) {
    int second = (L + R) / 2;
    pair<bool, vector<bool> > p1 = check(second);
    if (p1.first) {
      if (res > second) {
        res = second;
        ans = p1.second;
      }
      R = second - 1;
    } else
      L = second + 1;
  }
  if (res != INF) {
    printf("Yes\n");
    int cnt = 0;
    for (int i = (0); i <= (m - 1); i++)
      if (ans[i]) cnt++;
    printf("%d %d\n", res, cnt);
    for (int i = (0); i <= (m - 1); i++)
      if (ans[i]) printf("%d ", i + 1);
    printf("\n");
  } else
    printf("No\n");
}
int main() {
  int te = 1;
  while (te--) test();
  return 0;
}
