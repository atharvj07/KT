#include <bits/stdc++.h>
const int MAXN = 111111;
bool v[2][MAXN];
char s[2][MAXN];
int n, k, r;
struct state {
  int x, y, t;
} q[MAXN << 1];
inline void insert(int x, int y, int t) {
  if (y >= n) {
    puts("YES");
    exit(0);
  }
  if (y < t || s[x][y] == 'X' || v[x][y]) return;
  v[x][y] = true;
  q[++r].x = x;
  q[r].y = y;
  q[r].t = t;
}
int main() {
  scanf("%d%d%s%s", &n, &k, s[0], s[1]);
  v[0][0] = true;
  for (int l = 0; l <= r; ++l) {
    insert(q[l].x, q[l].y + 1, q[l].t + 1);
    insert(q[l].x, q[l].y - 1, q[l].t + 1);
    insert(q[l].x ^ 1, q[l].y + k, q[l].t + 1);
  }
  puts("NO");
  return 0;
}
