#include <bits/stdc++.h>
using namespace std;
inline int read() {
  int s = 0, w = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') w = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    s = (s << 3) + (s << 1) + (ch ^ 48);
    ch = getchar();
  }
  return s * w;
}
const long long mod = 998244353;
const int N = 2000100;
const double pi = acos(-1);
int n, m, s, t, w;
int a[N];
int main() {
  int T = read();
  while (T--) {
    n = read();
    int cnt = 1;
    int mark = 0;
    for (int i = 1; i <= n; i++) {
      a[i] = read();
      if (i != 1) {
        if (a[i] == a[i - 1]) {
          mark = 1;
          continue;
        }
        cnt = 2;
      }
    }
    if (cnt == 1) {
      printf("1\n");
      for (int i = 1; i <= n; i++) printf("1 ");
      printf("\n");
      continue;
    } else {
      if (mark == 0) {
        if (a[1] != a[n] && n % 2 == 1) {
          printf("3\n");
          for (int i = 1; i <= n - 1; i++) {
            if (i % 2 == 1)
              printf("1 ");
            else
              printf("2 ");
          }
          printf("3");
          printf("\n");
          continue;
        } else {
          printf("2\n");
          for (int i = 1; i <= n; i++)
            if (i % 2 == 0)
              printf("1 ");
            else
              printf("2 ");
          printf("\n");
          ;
          continue;
        }
      } else {
        if (n % 2 == 1 && a[1] != a[n]) {
          printf("2\n");
          int loc = 1;
          for (int i = 1; i <= n; i++) {
            if (i == 1) {
              printf("%d ", loc);
              loc = 2;
            } else if (mark == 1) {
              if (a[i] == a[i - 1]) {
                mark = 0;
                if (loc == 1)
                  printf("2 ");
                else
                  printf("1 ");
              } else {
                printf("%d ", loc);
                if (loc == 2)
                  loc = 1;
                else
                  loc = 2;
              }
            } else {
              printf("%d ", loc);
              if (loc == 2)
                loc = 1;
              else
                loc = 2;
            }
          }
          printf("\n");
          ;
        } else {
          printf("2\n");
          for (int i = 1; i <= n; i++)
            if (i % 2 == 0)
              printf("1 ");
            else
              printf("2 ");
          printf("\n");
          ;
          continue;
        }
      }
    }
  }
}
