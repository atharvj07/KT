#include <bits/stdc++.h>
#pragma comment(linker, "/stack:16777216")
using namespace std;
const int INF = 1000000000;
const int MAX = 100000;
const int MAX2 = 100000;
const int BASE = 1000000000;
const int LIM = 2000000;
struct edge {
  int a, b;
  int c, f;
  int rev;
  edge() {}
  edge(int _a, int _b, int _c, int _f, int _rev) {
    a = _a;
    b = _b;
    c = _c;
    f = _f;
    rev = _rev;
  }
};
int n, m, N, cnt;
int fA[MAX];
int fB[MAX];
int fC[MAX];
int L[MAX];
int R[MAX];
int T[MAX];
int W[MAX];
int Start[MAX2];
int Next[MAX2];
int P[MAX2];
int C[MAX2];
edge E[MAX2];
int getVal(int i, int x) { return fA[i] * x * x + fB[i] * x + fC[i]; }
void add_edge(int u, int v, int c) {
  E[cnt] = edge(u, v, c, 0, cnt + 1);
  Next[cnt] = Start[u];
  Start[u] = cnt;
  ++cnt;
  E[cnt] = edge(v, u, 0, 0, cnt - 1);
  Next[cnt] = Start[v];
  Start[v] = cnt;
  ++cnt;
}
int Flow(int s, int t) {
  int res = 0;
  while (1) {
    queue<int> Q;
    for (int i = (0); i < (N); ++i) P[i] = -1;
    Q.push(s);
    while (!Q.empty()) {
      int cur = Q.front();
      Q.pop();
      for (int i = Start[cur]; i != -1; i = Next[i]) {
        int to = E[i].b;
        if (P[to] == -1 && to != s && E[i].c - E[i].f > 0) {
          P[to] = i;
          Q.push(to);
        }
      }
    }
    if (P[t] == -1) break;
    int val = INF, x;
    x = t;
    while (x != s) {
      int id = P[x];
      val = min(val, E[id].c - E[id].f);
      x = E[id].a;
    }
    res += val;
    x = t;
    while (x != s) {
      int id = P[x];
      E[id].f += val;
      E[E[id].rev].f -= val;
      x = E[id].a;
    }
  }
  return res;
}
int main() {
  memset(Start, -1, sizeof(Start));
  scanf("%d %d", &n, &m);
  for (int i = (0); i < (n); ++i) {
    scanf("%d %d %d", &fA[i], &fB[i], &fC[i]);
  }
  for (int i = (0); i < (n); ++i) scanf("%d %d", &L[i], &R[i]);
  int sum = 0;
  for (int i = (0); i < (n); ++i) {
    T[i] = sum;
    W[i] = R[i] - L[i] + 2;
    sum += W[i];
  }
  for (int i = (0); i < (n); ++i)
    for (int j = (1); j < (W[i]); ++j)
      add_edge(T[i] + j - 1, T[i] + j, LIM - getVal(i, L[i] + j - 1));
  for (int i = (0); i < (m); ++i) {
    int u, v, d;
    scanf("%d %d %d", &u, &v, &d);
    --u;
    --v;
    for (int j = (0); j < (W[u] - 1); ++j) {
      int a = T[u] + j;
      if (L[u] + j - d >= L[v] && L[u] + j - d <= R[v] + 1) {
        int b = T[v] + ((L[u] + j - d) - L[v]);
        add_edge(a, b, INF);
      }
    }
  }
  N = sum;
  int s = N;
  int t = N + 1;
  N += 2;
  for (int i = (0); i < (n); ++i) add_edge(s, T[i], INF);
  for (int i = (0); i < (n); ++i) add_edge(T[i] + W[i] - 1, t, INF);
  int f = Flow(s, t);
  int res = LIM * n - f;
  printf("%d\n", res);
  return 0;
}
