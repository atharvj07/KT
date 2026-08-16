#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  scanf("%d", &n);
  vector<long long> v(n);
  for (int i = 0; i < n; i++) {
    scanf("%I64d", &v[i]);
  }
  vector<char> ans(n);
  ans[n - 1] = '+';
  long long now = v[n - 1];
  for (int i = n - 2; i >= 0; i--) {
    if (v[i] >= now) {
      ans[i] = '+';
      now = v[i] - now;
    } else {
      ans[i] = '-';
      now -= v[i];
    }
  }
  bool change = false;
  for (int i = 0; i < n; i++) {
    if (change) {
      if (ans[i] == '+') {
        printf("-");
      } else {
        printf("+");
      }
    } else {
      printf("%c", ans[i]);
    }
    if (ans[i] == '+') {
      change = !change;
    }
  }
  printf("\n");
  return 0;
}
