#include <bits/stdc++.h>
int main() {
  int n, cnt = 0;
  scanf("%d", &n);
  int a[n];
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  int maxx = a[0];
  int minn = a[0];
  for (int i = 0; i < n; i++) {
    if (a[i] > maxx) {
      maxx = a[i];
      cnt++;
    }
    if (a[i] < minn) {
      minn = a[i];
      cnt++;
    }
  }
  printf("%d\n", cnt);
  return 0;
}
