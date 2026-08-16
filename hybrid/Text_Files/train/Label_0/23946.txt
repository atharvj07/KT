#include <bits/stdc++.h>
using namespace std;
bool cmp(int a, int b) { return a > b; }
int main() {
  int t, n, a, b, c, d;
  cin >> t;
  while (t--) {
    cin >> n;
    for (int i = 0; i < n; i++) {
      if (i == 0)
        scanf("%d", &a);
      else if (i == 1) {
        scanf("%d", &b);
      } else if (i == (n - 1)) {
        scanf("%d", &d);
      } else {
        scanf("%d", &c);
      }
    }
    if (a + b <= d)
      printf("1 2 %d\n", n);
    else
      printf("-1\n");
  }
}
