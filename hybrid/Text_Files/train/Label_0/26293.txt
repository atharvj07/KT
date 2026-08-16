#include <bits/stdc++.h>
int dp[222222], size;
int main(int argc, char const *argv[]) {
  int n, in, index;
  int l, r, m;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &in);
    l = 0, r = size;
    while (l <= r) {
      m = (l + r) / 2;
      if (dp[m] < in) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    }
    if (l > size) size++;
    dp[l] = in;
  }
  printf("%d\n", size);
  return 0;
}
