#include <bits/stdc++.h>
using namespace std;
const int N = 110;
int ri[N];
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 0; i <= m; i++) ri[i] = i;
  for (int i = 1; i <= n; i++) {
    int l, r;
    scanf("%d%d", &l, &r);
    for (int j = l; j <= r; j++)
      if (ri[j] < r) ri[j] = r;
  }
  int now = 0;
  while (now != m) {
    if (ri[now] == now) break;
    now = ri[now];
  }
  if (now == m)
    printf("YES\n");
  else
    printf("NO\n");
  return 0;
}
