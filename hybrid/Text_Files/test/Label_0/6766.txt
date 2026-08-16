#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
const int Q = ((int)1e5) + 5;
const int INF = 0x7F7F7F7F;
const long long LINF = 0x7F7F7F7F7F7F7F7Fll;
const double eps = 1e-6;
const int mod = 1e9 + 7;
const double pi = acos(-1);
int B, q, b, n;
long long t[Q];
int ans[Q];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
struct Node {
  int x, y, k;
  Node(int _x = 0, int _y = 0, int _k = 0) : x(_x), y(_y), k(_k) {
    if (k == 'U') k = 0;
    if (k == 'D') k = 1;
    if (k == 'L') k = 2;
    if (k == 'R') k = 3;
  }
  Node nxt() {
    int _x = x + dx[k];
    _x = max(0, _x);
    _x = min(_x, b);
    int _y = y + dy[k];
    _y = max(0, _y);
    _y = min(_y, b);
    return Node(_x, _y, k);
  }
  int id() { return (x * B + y) * 4 + k; }
} nxt[N * N * 4];
int to[2][N * N * 4];
int main() {
  scanf("%d%d", &n, &b);
  B = b + 1;
  for (int i = 0; i < B; ++i)
    for (int j = 0; j < B; ++j)
      for (int k = 0; k < 4; ++k) {
        Node a = Node(i, j, k);
        nxt[a.id()] = a.nxt();
      }
  for (int i = 0; i < n; ++i) {
    int x1, x2, y1, y2, d;
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    if (x1 == x2)
      if (y2 > y1)
        d = 0;
      else
        d = 1;
    else if (x2 < x1)
      d = 2;
    else
      d = 3;
    int len = abs(y2 - y1) + abs(x2 - x1);
    for (int j = 0; j < len + 1; ++j) {
      int x, y;
      x = x1 + dx[d] * j;
      y = y1 + dy[d] * j;
      for (int k = 0; k < 4; ++k)
        nxt[Node(x, y, k).id()] = nxt[Node(x, y, d).id()];
    }
  }
  scanf("%d", &q);
  for (int i = 0; i < q; ++i) {
    int x, y;
    char ch;
    long long t0;
    scanf("%d %d %c %lld", &x, &y, &ch, t + i);
    ans[i] = Node(x, y, ch).id();
  }
  int ALL = 4 * B * B;
  for (int i = 0; i < ALL; ++i) to[0][i] = nxt[i].id();
  for (int i = 0; i < 50; ++i) {
    for (int j = 0; j < q; ++j)
      if (t[j] & (1ll << i)) ans[j] = to[0][ans[j]];
    for (int j = 0; j < ALL; ++j) to[1][j] = to[0][to[0][j]];
    for (int j = 0; j < ALL; ++j) to[0][j] = to[1][j];
  }
  for (int i = 0; i < q; ++i) {
    int x, y;
    x = ans[i] / 4 / B;
    y = ans[i] / 4 % B;
    printf("%d %d\n", x, y);
  }
}
