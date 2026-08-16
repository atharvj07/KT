#include <bits/stdc++.h>
using namespace std;
char s[100005];
int n, m;
int main(void) {
  scanf("%d%d%s", &n, &m, s);
  long long sol = (long long)n * m - n;
  for (int i = 1; i < n; ++i)
    sol += (s[i] != s[i - 1]) * ((long long)n * m - n);
  int curr = 1;
  for (int i = 1; i < n; ++i) {
    if (curr == 1) {
      if (s[i] == s[i - 1]) continue;
      ++curr;
    } else {
      if (s[i] == s[i - 2]) {
        ++curr;
      } else {
        sol -= (long long)curr * (curr - 1) / 2;
        curr = 1 + (s[i] != s[i - 1]);
        ;
      }
    }
  }
  sol -= (long long)curr * (curr - 1) / 2;
  printf("%lld\n", sol);
  return 0;
}
