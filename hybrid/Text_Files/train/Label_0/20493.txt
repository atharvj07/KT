#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const int N = 3 * 1e5 + 5;
int n, m;
int a[N], c[N];
vector<int> b[N];
void work() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i <= n - 1; ++i) scanf("%d", &a[i]);
  for (int i = 0; i <= m - 1; ++i) {
    int x, y;
    scanf("%d%d", &x, &y);
    b[y].push_back(x);
  }
  int ans = 0;
  for (int i = n - 1; i >= 0; --i) {
    if (c[a[i]] == n - 1 - i - ans && i != n - 1)
      ans++;
    else
      for (int f : b[a[i]]) c[f]++;
  }
  printf("%d\n", ans);
}
int main() {
  work();
  return 0;
}
