#include <bits/stdc++.h>
using namespace std;
struct po {
  int num, count;
} ss[400020];
int main() {
  int t;
  scanf("%d", &t);
  while (t--) {
    int g = 0, s = 0, b = 0;
    int n, k = 0;
    scanf("%d", &n);
    for (int i = 0; i <= n + 10; i++) {
      ss[i].num = 0;
      ss[i].count = 0;
    }
    int flag = 0;
    scanf("%d", &ss[k].num);
    ss[k].count++;
    for (int i = 1; i < n; i++) {
      int x;
      scanf("%d", &x);
      if (ss[k].num != x) {
        if (flag == 0) {
          flag++;
          g = ss[k].count;
        } else if (flag == 1) {
          flag++;
          s = s + ss[k].count;
          if (g >= s) flag = 1;
        } else if (flag == 2 && i <= n / 2) {
          b = b + ss[k].count;
        }
        k++;
        ss[k].num = x;
        ss[k].count++;
      } else
        ss[k].count++;
    }
    if (g == 0 || s == 0 || b == 0 || g >= s || g >= b)
      printf("0 0 0\n");
    else
      printf("%d %d %d\n", g, s, b);
  }
}
