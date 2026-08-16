#include <bits/stdc++.h>
using namespace std;
int f[200000][3], N, K;
char s1[200000], s2[200000];
bool ok;
inline void dfs(int x, int y) {
  if (ok) return;
  int Nxt = x + K;
  if (Nxt > N) {
    ok = 1;
    return;
  }
  if (y == 1) {
    if (s2[Nxt] == '-' && f[x][1] + 1 < f[Nxt][2] && Nxt > f[x][1] + 1) {
      f[Nxt][2] = f[x][1] + 1;
      dfs(Nxt, 2);
    }
    if (s1[x + 1] == '-' && f[x][1] + 1 < f[x + 1][1]) {
      f[x + 1][1] = f[x][1] + 1;
      dfs(x + 1, 1);
    }
    if (s1[x - 1] == '-' && f[x][1] + 1 < f[x - 1][1] && x - 1 > f[x][1] + 1) {
      f[x - 1][1] = f[x][1] + 1;
      dfs(x - 1, 1);
    }
  } else {
    if (s1[Nxt] == '-' && f[x][2] + 1 < f[Nxt][1] && Nxt > f[x][2] + 1) {
      f[Nxt][1] = f[x][2] + 1;
      dfs(Nxt, 1);
    }
    if (s2[x + 1] == '-' && f[x][2] + 1 < f[x + 1][2]) {
      f[x + 1][2] = f[x][2] + 1;
      dfs(x + 1, 2);
    }
    if (s2[x - 1] == '-' && f[x][2] + 1 < f[x - 1][2] && x - 1 > f[x][2] + 1) {
      f[x - 1][2] = f[x][2] + 1;
      dfs(x - 1, 2);
    }
  }
}
int main() {
  ios ::sync_with_stdio(false);
  cin >> N >> K;
  cin >> s1 + 1;
  cin >> s2 + 1;
  memset(f, 0x7f, sizeof(f));
  f[1][1] = 0;
  dfs(1, 1);
  if (ok)
    puts("YES");
  else
    puts("NO");
  return 0;
}
