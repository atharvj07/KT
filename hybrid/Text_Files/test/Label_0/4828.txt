#include <bits/stdc++.h>
using namespace std;
char c[100 + 5][100 + 5];
int main() {
  int i, j, m, n, f;
  while (~scanf("%d %d", &n, &m)) {
    getchar();
    for (int i = (0); i < (n); i++) gets(c[i]);
    f = 0;
    for (int i = (0); i < (n); i++)
      for (int j = (1); j < (m); j++)
        if (f == 0 && c[i][j] != c[i][j - 1]) f = 1;
    for (int j = (0); j < (m); j++)
      for (int i = (1); i < (n); i++)
        if (f == 0 && c[i][j] == c[i - 1][j]) f = 1;
    if (f == 1)
      puts("NO");
    else
      puts("YES");
  }
  return 0;
}
