#include <bits/stdc++.h>
using namespace std;
int n, m, k, s1, s2, x;
char c;
char f[100005];
int b[100005], p[100005], k1[100005], k2[100005];
int main() {
  scanf("%d%d\n", &n, &m);
  for (int i = 1; i <= n; i++) {
    c = getchar();
    scanf("%d\n", &x);
    if (c == '-') {
      s1++;
      k1[x]++;
    } else {
      s2++;
      k2[x]++;
    }
    b[i] = x;
    f[i] = c;
  }
  k = 0;
  for (int i = 1; i <= n; i++) {
    if (k2[i] + s1 - k1[i] == m) {
      p[i] = 1;
      k++;
    }
  }
  for (int i = 1; i <= n; i++) {
    if (f[i] == '+') {
      if (p[b[i]] == 0)
        printf("Lie\n");
      else {
        if (k == 1)
          printf("Truth\n");
        else
          printf("Not defined\n");
      }
    } else {
      if (p[b[i]] == 0)
        printf("Truth\n");
      else {
        if (k == 1)
          printf("Lie\n");
        else
          printf("Not defined\n");
      }
    }
  }
  return 0;
}
