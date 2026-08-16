#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  scanf("%d", &t);
  while (t--) {
    int n, m;
    scanf("%d", &n);
    long long odd1 = 0, even1 = 0;
    long long odd2 = 0, even2 = 0;
    for (int i = 0; i < n; i++) {
      scanf("%d", &m);
      if (m & 1)
        odd1++;
      else
        even1++;
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%d", &m);
      if (m & 1)
        odd2++;
      else
        even2++;
    }
    printf("%lld\n", odd1 * odd2 + even1 * even2);
  }
  return 0;
}
