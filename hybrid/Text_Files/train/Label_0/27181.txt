#include <bits/stdc++.h>
using namespace std;
const int N = 54;
char s[N];
int main() {
  int n;
  scanf("%s", s + 1);
  int i, cnt = 0;
  n = strlen(s + 1);
  for (i = 1; i <= n; i++) {
    if (s[i] == 'a') cnt++;
  }
  printf("%d\n", min(2 * cnt - 1, n));
  return 0;
}
