#include <bits/stdc++.h>
using namespace std;
char input[100010];
bool check(int start, int tot, int length) {
  int cnt = 0;
  for (int i = start; i < tot && cnt < 5; i += length, cnt++) {
    if (input[i] != '*') return false;
  }
  if (cnt == 5)
    return true;
  else
    return false;
}
int main() {
  int i, j, n;
  while (scanf("%d%s", &n, input) != EOF) {
    bool ok = false;
    for (i = 0; i < n; i++)
      for (j = 1; j <= n; j++) {
        if (check(i, n, j)) ok = true;
      }
    if (ok)
      printf("yes\n");
    else
      printf("no\n");
  }
  return 0;
}
