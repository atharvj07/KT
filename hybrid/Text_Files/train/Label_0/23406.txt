#include <bits/stdc++.h>
using namespace std;
int main() {
  long long p;
  int k, a[111], cnt = 0;
  cin >> p >> k;
  while (p) {
    if (cnt & 1) {
      long long pp;
      if (p % k == 0)
        pp = p;
      else
        pp = (p / k + 1) * k;
      a[cnt++] = (pp - p) % k;
      p = pp / k;
    } else {
      a[cnt++] = p % k;
      p /= k;
    }
  }
  while (cnt > 0 && a[cnt - 1] == 0) cnt--;
  printf("%d\n", cnt);
  for (int i = 0; i < cnt; i++) {
    printf("%d ", a[i]);
  }
  return 0;
}
