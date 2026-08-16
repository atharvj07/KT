#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int w = 1, s = 0;
  char ch = getchar();
  while (!isdigit(ch)) {
    if (ch == '-') w = -1;
    ch = getchar();
  }
  while (isdigit(ch)) {
    s = s * 10 + ch - '0';
    ch = getchar();
  }
  return w * s;
}
int R[1010], C[1010], n, cnt, pos1[1010], pos2[1010];
pair<pair<int, int>, pair<int, int> > Ans[1010];
int main() {
  n = read();
  for (register int i = 1; i <= n; ++i) R[i] = read(), pos1[R[i]] = i;
  for (register int i = 1; i <= n; ++i) C[i] = read(), pos2[C[i]] = i;
  for (register int i = 1; i <= n; ++i) {
    int x = pos1[i], y = pos2[i];
    if (x == y && x == i) continue;
    Ans[++cnt] = make_pair(make_pair(x, i), make_pair(i, y));
    R[x] = R[i];
    C[y] = C[i];
    pos1[R[x]] = x;
    pos2[C[y]] = y;
  }
  cout << cnt << "\n";
  for (register int i = 1; i <= cnt; ++i) {
    cout << Ans[i].first.first << " " << Ans[i].first.second << " "
         << Ans[i].second.first << " " << Ans[i].second.second << "\n";
  }
  return 0;
}
