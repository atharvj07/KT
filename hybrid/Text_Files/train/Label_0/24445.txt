#include <bits/stdc++.h>
using namespace std;
int g[102];
int a[102];
int find(int i) {
  if (i != g[i]) g[i] = find(g[i]);
  return g[i];
}
int main() {
  int n;
  cin >> n;
  for (int i = 0; i <= n; i++) g[i] = i;
  for (int i = 1; i <= n; i++) cin >> a[i];
  for (int i = 1; i <= n; i++) {
    int d;
    cin >> d;
    if (i + d <= n) g[find(i)] = find(i + d);
    if (i - d > 0) g[find(i)] = find(i - d);
  }
  for (int i = 1; i <= n; i++)
    if (find(i) == i) {
      int c[102];
      memset(c, 0, sizeof(c));
      for (int j = 1; j <= n; j++)
        if (find(j) == i) {
          c[j]++;
          c[a[j]]--;
        }
      for (int j = 1; j <= n; j++)
        if (c[j]) {
          cout << "NO";
          return 0;
        }
    }
  cout << "YES";
  return 0;
}
