#include <bits/stdc++.h>
int a[26];
char s[110];
int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  scanf("%s", s);
  for (int i = 0; i < n; i++) {
    a[s[i] - 'a']++;
    if (a[s[i] - 'a'] > m) {
      printf("NO");
      return 0;
    }
  }
  printf("YES");
  return 0;
}
