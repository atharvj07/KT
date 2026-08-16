#include <bits/stdc++.h>
using namespace std;
int a[110];
int d[110];
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &a[i], &d[i]);
  }
  int ans = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (a[i] >= a[j]) {
        if (a[i] < a[j] + d[j] || a[i] + d[i] < a[j]) {
          ans++;
          if (a[i] + d[i] >= a[j] + d[j]) ans++;
        } else if (a[i] + d[i] < a[j] + d[j])
          ans++;
      } else {
        if (a[i] + d[i] >= a[j] || a[i] >= a[j] + d[j]) {
          ans++;
          if (a[i] + d[i] < a[j] + d[j]) ans++;
        } else if (a[i] + d[i] >= a[j] + d[j])
          ans++;
      }
    }
  }
  printf("%d\n", ans);
  return 0;
}
