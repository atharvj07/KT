#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  int val = 1;
  for (int i = 0; i < n; i++) {
    if (val + 2 * n <= m) cout << val + 2 * n << " ";
    if (val <= m) cout << val << " ";
    if (val + 2 * n + 1 <= m) cout << val + 2 * n + 1 << " ";
    if (val + 1 <= m) cout << val + 1 << " ";
    val = val + 2;
  }
  return 0;
}
