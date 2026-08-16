#include <bits/stdc++.h>
using namespace std;
int p[110];
char str[110];
int main() {
  int i, n, res;
  p[0] = 1;
  for (i = 1; i < 110; i++) p[i] = 2 * p[i - 1] % 1000000007;
  scanf("%s ", str);
  n = strlen(str);
  res = 0;
  for (i = 0; i < n; i++)
    if (str[i] == '1')
      res = (res + (long long)p[i] * p[n - i - 1] % 1000000007 * p[n - i - 1]) %
            1000000007;
  printf("%d\n", res);
  return 0;
}
