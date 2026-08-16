#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  string cur, next;
  cin >> cur;
  int t = 0;
  int d = 1;
  long long ans = 0;
  for (int i = 1; i < n; i++) {
    cin >> next;
    if (cur[t] == '.' && next[t] == '.') {
      ans++;
      cur = next;
      continue;
    }
    int l = t - 1, r = t + 1;
    while (true) {
      if (d == 1) {
        while (r != m && cur[r] == '.' && next[r] != '.') r++;
      } else {
        while (l != -1 && cur[l] == '.' && next[l] != '.') l--;
      }
      ans += r - l - 1;
      if (d == 1 && r != m && cur[r] == '.' && next[r] == '.') {
        ans++;
        t = r;
        break;
      }
      if (d == -1 && l != -1 && cur[l] == '.' && next[l] == '.') {
        ans++;
        t = l;
        break;
      }
      if (d == 1 && r != m && cur[r] == '+')
        cur[r] = '.';
      else if (d == -1 && l != -1 && cur[l] == '+')
        cur[l] = '.';
      if ((l == -1 || cur[l] == '#') && (r == m || cur[r] == '#')) {
        printf("Never");
        return 0;
      }
      d *= -1;
    }
    cur = next;
  }
  printf("%I64d", ans);
};
