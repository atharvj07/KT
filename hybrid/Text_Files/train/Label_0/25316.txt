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
 
 
struct Edge {
  bool ban;
  char src;
  char dest;
  int flag;
  int cost;
  Edge(int src, int dest, int flag, int cost) : ban(0), src(src), dest(dest), flag(flag), cost(cost) {;}
  Edge(int ban, int src, int dest, int flag, int cost) : ban(ban), src(src), dest(dest), flag(flag), cost(cost) {;}
  bool operator<(const Edge &rhs) const {
    return cost > rhs.cost;
  }
};
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;
typedef vector<int> Array;
typedef vector<Array> Matrix;
 
void PrintMatrix(const Matrix &matrix) {
  for (int y = 0; y < (int)matrix.size(); y++) {
    for (int x = 0; x < (int)matrix[y].size(); x++) {
      printf("%d ", matrix[y][x]);
    }
    puts("");
  }
}
 
const ll INF = 1e+7;
int dist[15][1 << 22];
int lm[20];
int lf[20];
int ln;
int n;
int m;
int indexs[20];
 
int mapto[20][20];
Graph lg[20];
Graph g;
 
void Clear(int n, int m) {
  REP(i, n) {
    memset(dist[i], 0x0f, sizeof(int) * (1 << m));
  }
}
 
void TSP(const Graph &g, int s, int ini, int ef, int end) {
  queue<Edge> que;
  que.push(Edge(s, s, ini, 0));
  dist[s][ini] = 0;
  while (!que.empty()) {
    Edge e = que.front();
    que.pop();
    int from = e.dest;
    if (dist[from][e.flag] != e.cost) { continue; }
    if (from == end && e.flag == ef) { break; }
    FORIT(it, g[from]) {
      if (e.flag & it->flag) { continue; }
      int nfrom = from;
      int nto = it->dest;
      int nflag = e.flag | it->flag;
      int ncost = e.cost + it->cost;
      if (dist[nto][nflag] <= ncost) { continue; }
      dist[nto][nflag] = ncost;
      que.push(Edge(nfrom, nto, nflag, ncost));
    }
  }
}
 
int START;
int TSP2(int ban, int from, int flag) {
  int ret = INF;
  FORIT(it, g[from]) {
    if (flag & it->flag) { continue; }
    int nban = (it->flag >= (1 << n)) ? 1 : 0;
    int to = it->dest;
    if (ban && nban) { continue; }
    int nflag = flag | it->flag;
    if (to == START && nflag == (1 << m) - 1) { ret = it->cost; break; }
    if (to == START) { continue; }
    if (!nban && dist[to][nflag] != 0x0f0f0f0f) {
      ret = min(ret, dist[to][nflag] + it->cost);
    } else {
      ret = min(ret, TSP2(nban, to, nflag) + it->cost);
    }
  }
  if (!ban) {
    dist[from][flag] = ret;
  }
  return ret;
}
 
void CalcMoveCost3(int c, int s, int e, int n1, int n2, int n3) {
  int bit = (1 << lm[c]) - 1;
  bit ^= 7;
  bit |= (1 << (lm[c] + s));
  if (n1) { bit |= 1; }
  if (n2) { bit |= 2; }
  if (n3) { bit |= 4; }
  int cost = dist[e][bit];
 
  int offset = mapto[c][0];
  int from = mapto[c][s];
  int to = mapto[c][e];
  int flag = (1 << m) | (n1 << (offset + 0)) | (n2 << (offset + 1)) | (n3 << (offset + 2));
  if (cost >= INF) { return; }
  g[from].push_back(Edge(from, to, flag, cost));
}
 
void CalcMoveCost4(int c, int s, int e, int n1, int n2, int n3, int n4) {
  int bit = (1 <<lm[c]) - 1;
  bit ^= 15;
  bit |= (1 << (lm[c] + s));
  if (n1) { bit |= 1; }
  if (n2) { bit |= 2; }
  if (n3) { bit |= 4; }
  if (n4) { bit |= 8; }
  int cost = dist[e][bit];
 
  int offset = mapto[c][0];
  int from = mapto[c][s];
  int to = mapto[c][e];
  int flag = (3 << m) | (n1 << (offset + 0)) | (n2 << (offset + 1)) | (n3 << (offset + 2)) | (n4 << (offset + 3));
  if (cost >= INF) { return; }
  g[from].push_back(Edge(from, to, flag, cost));
}
 
void CalcMoveCost4Divide(int c, int s1, int e1, int s2, int e2) {
  int left = (1 << (lm[c] + s1)) | (1 << e1);
  int right = (1 << (lm[c] + s2)) | (1 << e2);
  assert((left & right) == 0);
  int mask = ((1 << lm[c]) - 1) ^ 15;
  int cost = INF;
  FOREQ(i, 0, mask) {
    if ((mask | i) != mask) { continue; }
    int div  = mask ^ i;
    cost = min(cost, dist[e1][left | i] + dist[e2][right | div]);
  }
  int offset = mapto[c][0];
  int f1 = mapto[c][s1];
  int t1 = mapto[c][e1];
  int f2 = mapto[c][s2];
  int t2 = mapto[c][e2];
  int flag1 = (1 << m) | (1 << (offset + e1));
  int flag2 = (1 << m) | (1 << (offset + s1));
  int flag3 = (2 << m) | (1 << (offset + e2));
  int flag4 = (2 << m) | (1 << (offset + s2));
  if (cost >= INF) { return; }
  g[f1].push_back(Edge(f1, t1, flag1, cost));
  g[t1].push_back(Edge(t1, f1, flag2, cost));
  g[f2].push_back(Edge(f2, t2, flag3, 0));
  g[t2].push_back(Edge(t2, f2, flag4, 0));
 
  //cout << f1 << " " << t1 << " " << flag1 << " " << f2 << " " << t2 << " " << flag3 << endl;
  //cout << cost << endl;
}
 
void MakeInnerEdge(int c) {
  Clear(lm[c], lm[c] + lf[c]);
  REP(i, lf[c]) {
    TSP(lg[c], i, 1 << (lm[c] + i), -1, -1);
  }
  indexs[c] = m;
  if (lf[c] == 2) {
    int from = mapto[c][0];
    int to = mapto[c][1];
    int cost = dist[1][(((1 << lm[c]) - 1) ^ 1) | (1 << lm[c])];
    g[from].push_back(Edge(from, to, (1 << m) | (1 << to), cost));
    g[to].push_back(Edge(to, from, (1 << m) | (1 << from), cost));
    m++;
  } else if (lf[c] == 3) {
    REP(s, 3) {
      REP(e, 3) {
        if (s == e) { continue; }
        REP(n1, 2) {
         if (s == 0 && n1) { continue; }
         if (e == 0 && !n1) { continue; }
          REP(n2, 2) {
            if (s == 1 && n2) { continue; }
            if (e == 1 && !n2) { continue; }
            REP(n3, 2) {
              if (s == 2 && n3) { continue; }
              if (e == 2 && !n3) { continue; }
              CalcMoveCost3(c, s, e, n1, n2, n3);
            }
          }
        }
      }
    }
    m++;
  } else if (lf[c] == 4) {
    // a -> some -> b -> other -> c -> rest -> d
    REP(s, 4) {
      REP(e, 4) {
        if (s == e) { continue; }
        REP(n1, 2) {
          if (s == 0 && n1) { continue; }
          if (e == 0 && !n1) { continue; }
          REP(n2, 2) {
            if (s == 1 && n2) { continue; }
            if (e == 1 && !n2) { continue; }
            REP(n3, 2) {
              if (s == 2 && n3) { continue; }
              if (e == 2 && !n3) { continue; }
              REP(n4, 2) {
                if (s == 3 && n4) { continue; }
                if (e == 3 && !n4) { continue; }
                CalcMoveCost4(c, s, e, n1, n2, n3, n4);
              }
            }
          }
        }
      }
    }
 
    // a -> some -> b, c -> rest -> d
    CalcMoveCost4Divide(c, 0, 1, 2, 3);
    CalcMoveCost4Divide(c, 0, 2, 1, 3);
    CalcMoveCost4Divide(c, 0, 3, 1, 2);
    m += 2;
  } else {
    assert(false);
  }
}
 
int main() {
  int k;
  while (scanf("%d %d", &ln, &k) > 0) {
    int minValue = 5;
    int minIndex = -1;
    g.clear();
    REP(i, 20) { lg[i].clear(); }
    MEMSET(mapto, 0xdf);
    n = 0;
    REP(i, ln) {
      scanf("%d", &lm[i]);
      lg[i] = Graph(lm[i]);
    }
    REP(i, ln) {
      scanf("%d", &lf[i]);
      if (lf[i] < minValue) {
        minValue = lf[i];
        minIndex = i;
      }
      REP(j, lf[i]) {
        mapto[i][j] = n++;
      }
    }
    g = Graph(n);
    REP(i, k) {
      int fl, fs, tl, ts, c;
      scanf("%d %d %d %d %d", &fl, &fs, &tl, &ts, &c);
      fl--; fs--; tl--; ts--;
      if (mapto[fl][fs] >= 0 && mapto[tl][ts] >= 0) {
        int f = mapto[fl][fs];
        int t = mapto[tl][ts];
        g[f].push_back(Edge(f, t, 1 << t, c));
        g[t].push_back(Edge(t, f, 1 << f, c));
      }
      if (fl == tl) {
        lg[fl][fs].push_back(Edge(fs, ts, 1 << ts, c));
        lg[fl][ts].push_back(Edge(ts, fs, 1 << fs, c));
      }
    }
    m = n;
    int ans = INF;
    if (ln == 1) {
      Clear(lm[0], lm[0]);
      TSP(lg[0], 0, 0, (1 << lm[0]) - 1, 0);
      ans = dist[0][(1 << lm[0]) - 1];
      if (lm[0] == 1) { ans = 0; }
    } else {
      REP(i, ln) {
        if (lm[i] == lf[i]) { continue; }
        if (lf[i] == 1) { goto ANS; }
        MakeInnerEdge(i);
      }
      assert(m <= 22);
      // if (m >= 22) {
      //   Clear(n, m);
      //   srand(time(NULL));
      //   START = mapto[minIndex][rand() % minValue];
      //   ans = min(ans, TSP2(g, 0, START, 0));
      // } else {
        REP(i, max(minValue - 1, 1)) {
          Clear(n, m);
          START = mapto[minIndex][i];
          dist[START][(1 << m) - 1] = 0;
          ans = min(ans, TSP2(0, START, 0));
        }
      //}
    }
ANS:
    if (ans < INF) {
      printf("%d\n", ans);
    } else {
      puts("-1");
    }
  }
}