#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k, a[100005], num = 0;
  cin >> n >> k;
  for (int i = 0; i < n; i++) cin >> a[i];
  sort(a, a + n);
  for (int i = 0; i < n; i++) {
    if (k * 2 < a[i]) {
      while (k * 2 < a[i]) {
        k = k * 2;
        num++;
      }
      k = max(k, a[i]);
    }
    k = max(k, a[i]);
  }
  printf("%d\n", num);
  return 0;
}
