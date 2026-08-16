#include <bits/stdc++.h>
using namespace std;
const int MAXV = 510;
struct node {
  int x, y, t;
};
int N, M;
vector<int> adj[MAXV];
int D[MAXV][MAXV][2];
node P[MAXV][MAXV][2];
int main() {
  int x, y, x2, y2, t;
  scanf("%d %d", &N, &M);
  for (int i = 0; i < M; i++) {
    scanf("%d %d", &x, &y);
    adj[x].push_back(y);
    adj[y].push_back(x);
  }
  memset(D, -1, sizeof(D));
  D[1][N][0] = 0;
  P[1][N][0] = (node){-1, -1, -1};
  queue<node> q;
  q.push((node){1, N, 0});
  bool ok = 0;
  while (!q.empty()) {
    node u = q.front();
    q.pop();
    x = u.x, y = u.y;
    t = u.t;
    if (t == 0 && x == N && y == 1) {
      ok = 1;
      break;
    }
    if (t == 0) {
      for (int i = 0; i < adj[x].size(); i++) {
        x2 = adj[x][i];
        if (D[x2][y][1] != -1) continue;
        D[x2][y][1] = D[x][y][0];
        P[x2][y][1] = u;
        q.push((node){x2, y, 1});
      }
    } else {
      for (int i = 0; i < adj[y].size(); i++) {
        y2 = adj[y][i];
        if (x == y2 || D[x][y2][0] != -1) continue;
        D[x][y2][0] = D[x][y][1] + 1;
        P[x][y2][0] = (node){P[x][y][1].x, y, 0};
        q.push((node){x, y2, 0});
      }
    }
  }
  if (!ok)
    puts("-1");
  else {
    int K = D[N][1][0];
    printf("%d\n", K);
    vector<int> RET1, RET2;
    x = N, y = 1;
    while (K--) {
      RET1.push_back(x);
      RET2.push_back(y);
      int x2 = P[x][y][0].x, y2 = P[x][y][0].y;
      x = x2;
      y = y2;
    }
    reverse(RET1.begin(), RET1.end());
    reverse(RET2.begin(), RET2.end());
    printf("1");
    for (int i = 0; i < RET1.size(); i++) printf(" %d", RET1[i]);
    printf("\n%d", N);
    for (int i = 0; i < RET2.size(); i++) printf(" %d", RET2[i]);
    putchar('\n');
  }
  return 0;
}
