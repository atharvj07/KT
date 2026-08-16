#include <bits/stdc++.h>
using namespace std;
const int N = 5000;
int a[N], b[N];
int main(int argc, const char* agrv[]) {
  int n, k;
  scanf("%d %d", &n, &k);
  if (k >= 2) {
    puts("Yes");
    return 0;
  }
  for (int i = 1; i <= n; ++i) {
    scanf("%d", a + i);
  }
  for (int i = 1; i <= k; ++i) {
    scanf("%d", b + i);
  }
  for (int i = 1; i <= n; ++i) {
    if (a[i] == 0) {
      a[i] = b[1];
    }
  }
  bool f = true;
  for (int i = 2; i <= n; ++i) {
    if (a[i] < a[i - 1]) f = false;
  }
  if (f)
    puts("No");
  else
    puts("Yes");
}
