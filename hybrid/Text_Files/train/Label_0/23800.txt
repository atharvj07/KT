#include <bits/stdc++.h>
using namespace std;
int a, b;
int L1[1 << 20], L2[1 << 20];
int pos[1 << 20];
int res = 0;
int main() {
  memset(pos, -1, sizeof(pos));
  scanf("%d%d", &a, &b);
  for (int i = 0; i < a; ++i) scanf("%d", &L1[i]);
  for (int i = 0; i < b; ++i) {
    scanf("%d", &L2[i]);
    pos[L2[i]] = i;
  }
  int cur = -1;
  int len = 0;
  for (int i = 0; i < a; ++i) {
    if (pos[L1[i]] == -1) {
      cur = -1;
      continue;
    }
    if (cur == -1) {
      cur = i;
      len = 1;
    }
    while (1) {
      if (pos[L1[(cur + 1) % a]] == -1) break;
      int dist = pos[L1[(cur + 1) % a]] - pos[L1[cur]];
      if (dist <= 0) dist += b;
      int p = pos[L1[i]] - pos[L1[cur]];
      if (p <= 0) p += b;
      if (dist >= p) break;
      cur = (cur + 1) % a;
      len++;
    }
    res = max(res, len);
    len--;
  }
  cout << res << endl;
  return 0;
}
