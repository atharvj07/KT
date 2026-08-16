#include <bits/stdc++.h>
using namespace std;
int n, s[200005], t[200005];
char ss[200005];
int main() {
  scanf("%s", ss);
  int n = strlen(ss);
  for (int i = 1; i <= n; i++) s[i] = ss[i - 1] - '0';
  int tot = 0;
  for (int i = n; i >= 1; i--) {
    if (tot && s[i])
      t[i] = 1;
    else
      t[i] = 0;
    if (s[i] == 0) tot++;
    if (s[i] == 1) tot--;
    tot = max(tot, 0);
  }
  for (int i = 1; i <= n; i++) printf("%d", t[i]);
  return 0;
}
