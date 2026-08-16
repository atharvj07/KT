#include <bits/stdc++.h>
using namespace std;
const double Pi = acos(-1.0);
const int maxn = 1e7 + 100;
inline int read() {
  char c = getchar();
  int x = 0, f = 1;
  while (c < '0' || c > '9') {
    if (c == '-') f = -1;
    c = getchar();
  }
  while (c >= '0' && c <= '9') {
    x = x * 10 + c - '0';
    c = getchar();
  }
  return x * f;
}
char a[100010], b[100010];
int ans[200010];
int main() {
  int t;
  scanf("%d", &t);
  while (t--) {
    int n;
    int cnt = 0;
    scanf("%d", &n);
    scanf("%s%s", a, b);
    int rtag = 0, ftag = 0, just1 = 0, just2 = n - 1;
    for (int i = n - 1; i >= 0; i--) {
      if (rtag == 0) {
        if (((int)a[just1] - '0') ^ ftag != (b[i] - '0')) {
          just1++;
          ftag ^= 1;
          rtag ^= 1;
          ans[++cnt] = i + 1;
        } else {
          a[just1] ^= 1;
          just1++;
          ftag ^= 1;
          rtag ^= 1;
          ans[++cnt] = 1;
          ans[++cnt] = i + 1;
        }
      } else {
        if (((int)a[just2] - '0') ^ ftag != (b[i] - '0')) {
          just2--;
          ftag ^= 1;
          rtag ^= 1;
          ans[++cnt] = i + 1;
        } else {
          a[just2] ^= 1;
          just2--;
          ftag ^= 1;
          rtag ^= 1;
          ans[++cnt] = 1;
          ans[++cnt] = i + 1;
        }
      }
    }
    printf("%d ", cnt);
    for (int i = 1; i <= cnt; i++) printf("%d ", ans[i]);
    printf("\n");
  }
  return 0;
}
