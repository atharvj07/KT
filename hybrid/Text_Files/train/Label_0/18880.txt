#include <bits/stdc++.h>
int n;
long long a[(200010)], b[(200010)], c[(200010)], cnt[(31)];
int main() {
  srand((unsigned)time(NULL));
  scanf("%d", &n);
  long long sum = 0, suma;
  for (int i = 1; i <= n; ++i) {
    scanf("%I64d", b + i);
    sum += b[i];
  }
  for (int i = 1; i <= n; ++i) {
    scanf("%I64d", c + i);
    sum += c[i];
  }
  if (sum % (2 * n)) return printf("-1\n"), 0;
  suma = sum / (2 * n);
  for (int i = 1; i <= n; ++i) {
    if ((b[i] + c[i] - suma) % n) return printf("-1\n"), 0;
    a[i] = (b[i] + c[i] - suma) / n;
    for (int j = 0; j < (31); ++j) {
      cnt[j] += (a[i] >> j) & 1;
    }
  }
  for (int i = 1; i <= n; ++i) {
    long long sumb = 0, sumc = 0;
    for (int j = 0; j < (31); ++j) {
      if ((a[i] >> j) & 1) {
        sumb += (1ll << j) * cnt[j];
        sumc += (1ll << j) * n;
      } else {
        sumc += (1ll << j) * cnt[j];
      }
    }
    if (sumb != b[i] || sumc != c[i]) return printf("-1\n"), 0;
  }
  for (int i = 1; i <= n; ++i) {
    printf("%I64d%c", a[i], " \n"[i == n]);
  }
  return 0;
}
