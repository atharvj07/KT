#include <bits/stdc++.h>
using namespace std;
int a[100010];
int gg[100010];
int main() {
  int n;
  while (~scanf("%d", &n)) {
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]);
      if (a[i - 1] < a[i])
        gg[i] = gg[i - 1] + 1;
      else
        gg[i] = 1;
    }
    int big = 0;
    int ans = 0;
    for (int i = n - 1; i >= 0; i--) {
      big = max(big, gg[i - 1] + 1);
      big = max(big, ans + 1);
      if (i == 0 || i == n - 1 || a[i - 1] + 1 < a[i + 1])
        big = max(big, gg[i - 1] + ans + 1);
      if (a[i] < a[i + 1])
        ans++;
      else
        ans = 1;
    }
    printf("%d\n", big);
  }
  return 0;
}
