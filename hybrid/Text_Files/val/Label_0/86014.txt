#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 10;
int n, k;
char s[N];
int chk(char s[]) {
  for (int i = 1; i <= n; i += k) {
    for (int j = 1; j <= k; j++) {
      if (i + j - 1 > n || i + j - 1 + k > n) break;
      if (s[i + j - 1] != s[i + j - 1 + k]) {
        if (s[i + j - 1] > s[i + j - 1 + k])
          return -1;
        else
          return 1;
      }
    }
  }
  return 0;
}
int main() {
  cin >> n >> k;
  scanf("%s", s + 1);
  int flag = chk(s);
  if (flag == 0) {
    printf("%d\n", n);
    printf("%s\n", s + 1);
    return 0;
  } else if (flag == -1) {
    for (int i = 1; i <= n; i += k) {
      for (int j = 1; j <= k; j++) {
        if (i + j - 1 > n || i + j - 1 + k > n) break;
        s[i + j - 1 + k] = s[i + j - 1];
      }
    }
    printf("%d\n", n);
    printf("%s\n", s + 1);
    return 0;
  } else {
    bool ff = 0;
    if (s[k] == '9')
      s[k] = '0', ff = 1;
    else
      s[k]++;
    if (ff) {
      for (int i = k - 1; i >= 1; i--) {
        if (s[i] == '9') {
          s[i] = '0';
          continue;
        }
        s[i]++;
        break;
      }
    }
    for (int i = 1; i <= n; i += k) {
      for (int j = 1; j <= k; j++) {
        if (i + j - 1 > n || i + j - 1 + k > n) break;
        s[i + j - 1 + k] = s[i + j - 1];
      }
    }
    printf("%d\n", n);
    printf("%s\n", s + 1);
    return 0;
  }
  return 0;
}
