#include <bits/stdc++.h>
const int MOD = 10007;
const int MAXN = 110001;
int n, a[MAXN];
int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", a + i);
  std::sort(a + 1, a + n + 1);
  int answer = 0;
  for (int i = 1; i <= n; i++) {
    answer = (answer + 1ll * a[i] * a[n - i + 1] % MOD) % MOD;
  }
  printf("%d\n", answer);
}
