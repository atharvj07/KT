#include <bits/stdc++.h>
using namespace std;
int n, ns[100100], cnt;
int ble(int a) {
  while (a - (a & -a)) a -= a & -a;
  return a;
}
bool test(int v) {
  int a = -1;
  cnt = 0;
  for (int i = 0; i < n; ++i)
    if (ns[i] & (1 << v)) a &= ns[i], cnt++;
  return !(a % (1 << v));
}
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) scanf("%d", &ns[i]);
  for (int v = 30; v >= 0; v--)
    if (test(v)) {
      printf("%d\n", cnt);
      bool lol = 0;
      int bla = 1 << v;
      for (int i = 0; i < n; ++i)
        if (ns[i] & bla) {
          if (lol)
            printf(" ");
          else
            lol = 1;
          printf("%d", ns[i]);
        }
      puts("");
      break;
    }
  return 0;
}
