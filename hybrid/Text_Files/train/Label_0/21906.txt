#include <bits/stdc++.h>
using namespace std;
const int MAX = 5e5 + 9;
char s[MAX], a[MAX], b[MAX];
int main() {
  int n, k, ans = 0, c1, c2;
  scanf("%d%d%s", &n, &k, &s);
  if (k == 2) {
    c1 = c2 = 0;
    for (int i = 0; i < n; i++)
      if (i % 2) {
        a[i] = 'A', c1 += (s[i] == 'B');
        b[i] = 'B', c2 += (s[i] == 'A');
      } else {
        a[i] = 'B', c1 += (s[i] == 'A');
        b[i] = 'A', c2 += (s[i] == 'B');
      }
    return !printf("%d\n%s", min(c1, c2), c1 < c2 ? a : b);
  }
  for (int i = 1; s[i]; i++)
    if (s[i] == s[i - 1]) {
      for (int j = 0; j < k; j++)
        if (s[i - 1] != (j + 'A') && s[i + 1] != (j + 'A')) {
          s[i] = j + 'A';
          break;
        }
      ans++;
    }
  printf("%d\n%s", ans, s);
}
