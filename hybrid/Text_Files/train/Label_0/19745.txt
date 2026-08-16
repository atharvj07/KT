#include <bits/stdc++.h>
using namespace std;
const int maxn = 15;
int a[maxn];
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  bool flag = 0;
  for (int i = 1; i < n; i++)
    if (abs(a[i + 1] - a[i]) >= 2) {
      flag = 1;
      break;
    }
  printf("%s\n", flag ? "NO" : "YES");
  return 0;
}
