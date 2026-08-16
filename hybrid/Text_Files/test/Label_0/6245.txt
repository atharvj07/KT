#include <bits/stdc++.h>
using namespace std;
char str[20];
int main() {
  int n;
  while (scanf("%d", &n) != EOF) {
    while (n--) {
      scanf("%s", str);
      int k = strlen(str + 4);
      long long ans = atoi(str + 4);
      int F = 0;
      int ten = 10;
      for (int i = 1; i < k; i++) {
        F += ten;
        ten *= 10;
      }
      while (ans < F + 1989) ans += ten;
      cout << ans << endl;
    }
  }
  return 0;
}
