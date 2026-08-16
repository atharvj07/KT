#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2e5 + 5;
char str[MAXN];
int n;
int t;
int main() {
  scanf("%d", &t);
  while (t--) {
    scanf("%d", &n);
    scanf("%s", str);
    int n = strlen(str);
    int cur = 0;
    for (int i = 0; i < n; i++) {
      if (str[i] == 'B') {
        if (cur > 0)
          cur--;
        else
          cur++;
      } else
        cur++;
    }
    printf("%d\n", cur);
  }
  return 0;
}
