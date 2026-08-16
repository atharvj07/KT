#include <bits/stdc++.h>
using namespace std;
const int Max = 2e6 + 10;
const int Mod = 1e9 + 7;
const long long int Inf = 1LL << 62;
int ar[Max];
int main() {
  int t, n, k;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; tc++) {
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++) {
      scanf("%d", &ar[i]);
    }
    sort(ar + 1, ar + n + 1);
    long long int tot = 0;
    int ans = 0;
    for (int i = n; i >= 1; i--) {
      for (int j = i; ar[i] == ar[j] && j; j--) {
        i = j;
      }
      if (ar[i] - tot <= 0) {
        break;
      }
      ans++;
      tot += k;
    }
    printf("%d\n", ans);
  }
  return 0;
}
