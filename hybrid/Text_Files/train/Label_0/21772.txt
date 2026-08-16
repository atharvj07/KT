#include <bits/stdc++.h>
using namespace std;
int n, ans, tmp, is[2];
char s[100001], pr;
int main() {
  scanf("%d", &n);
  scanf("%s\n", s);
  ++ans;
  pr = s[0];
  tmp = 1;
  for (int i = (1); i < (n); ++i) {
    if (s[i - 1] == s[i])
      ++tmp;
    else {
      is[s[i - 1] - '0'] = max(is[s[i - 1] - '0'], tmp);
      tmp = 1;
    }
    if (pr != s[i]) {
      ++ans;
      pr = s[i];
    }
  }
  is[s[n - 1] - '0'] = max(is[s[n - 1] - '0'], tmp);
  if (is[0] > 1 || is[1] > 1) ans = min(n, ans + 2);
  printf("%d ", ans);
  return 0;
}
