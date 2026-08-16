#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  vector<int> L(m);
  long long S = 0;
  for (int i = 0; i < m; i++) {
    scanf("%d", &L[i]);
    S += L[i];
    if (n - L[i] < i) {
      puts("-1");
      return 0;
    }
  }
  if (S < n) {
    puts("-1");
    return 0;
  }
  vector<int> ans(m + 1);
  ans[m] = n + 1;
  for (int i = m - 1; i >= 0; i--) ans[i] = max(ans[i + 1] - L[i], i + 1);
  for (int i = 0; i < m; i++) printf("%d ", ans[i]);
  return 0;
}
