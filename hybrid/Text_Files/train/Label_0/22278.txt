#include <bits/stdc++.h>
using namespace std;
const int maxn = int(4e5) + 100;
int n, m;
int a[maxn], b[maxn], d[maxn], diff[maxn], fail[maxn];
vector<int> ans;
void read() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
}
void solve() {
  if (n == 1) {
    puts("1");
    printf("%d\n", a[1] * 2 % m);
    return;
  }
  for (int i = 1; i <= n; ++i) b[i] = (m - a[n - i + 1]);
  for (int i = 1; i <= n; ++i) b[n + i] = b[i] + m;
  for (int i = 1; i < n * 2; ++i) d[i] = b[i + 1] - b[i];
  for (int i = 1; i < n; ++i) diff[i] = a[i + 1] - a[i];
  fail[1] = 0;
  for (int i = 2, j = 0; i < n; ++i) {
    while (j > 0 && diff[j + 1] != diff[i]) j = fail[j];
    if (diff[j + 1] == diff[i]) ++j;
    fail[i] = j;
  }
  for (int i = 1, j = 0; i < n * 2 - 1; ++i) {
    while (j > 0 && diff[j + 1] != d[i]) j = fail[j];
    if (diff[j + 1] == d[i]) ++j;
    if (j == n - 1) {
      ans.push_back((a[j] - b[i] + m) % m);
      j = fail[j];
    }
  }
  sort(ans.begin(), ans.end());
  printf("%d\n", ans.size());
  for (auto &i : ans) printf("%d ", i);
}
int main() {
  read();
  solve();
  return 0;
}
