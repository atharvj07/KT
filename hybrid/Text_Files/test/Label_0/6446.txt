#include <bits/stdc++.h>
using namespace std;
long long int b, q, l;
int m;
long long int a[100001];
int p, n;
int c;
long long int abso(long long int x) {
  if (x >= 0) return x;
  return -x;
}
int main() {
  c = 0;
  scanf("%lld %lld %lld %d", &b, &q, &l, &m);
  for (int i = 0; i < m; i++) scanf("%lld", &a[i]);
  n = m;
  if (b == 0) {
    for (int i = 0; i < m; i++)
      if (a[i] == 0) {
        printf("0\n");
        return 0;
      }
    printf("inf\n");
    return 0;
  }
  if (q == 0) {
    if (abso(b) > l) {
      printf("0\n");
      return 0;
    }
    bool zf = false;
    bool bf = false;
    for (int i = 0; i < m; i++)
      if (a[i] == 0)
        zf = true;
      else if (a[i] == b)
        bf = true;
    if (!zf)
      printf("inf\n");
    else if (!bf)
      printf("1\n");
    else
      printf("0\n");
    return 0;
  }
  if (q == 1) {
    if (abso(b) > l) {
      printf("0\n");
      return 0;
    }
    for (int i = 0; i < m; i++)
      if (a[i] == b) {
        printf("0\n");
        return 0;
      }
    printf("inf\n");
    return 0;
  }
  if (q == -1) {
    if (abso(b) > l) {
      printf("0\n");
      return 0;
    }
    bool pf = false;
    bool nf = false;
    for (int i = 0; i < m; i++)
      if (a[i] == b)
        pf = true;
      else if (a[i] == -b)
        nf = true;
    if (!pf || !nf)
      printf("inf\n");
    else
      printf("0\n");
    return 0;
  }
  p = m;
  n = -1;
  sort(a, a + m);
  for (int i = 0; i < m; i++)
    if (a[i] >= 0) {
      p = i;
      n = i - 1;
      break;
    }
  if (n == -1 && a[0] < 0) n = m - 1;
  while (abs(b) <= l) {
    if (b > 0) {
      while (p < m && a[p] < b) p++;
      if (p < m && a[p] != b) c++;
      if (p >= m) c++;
    } else {
      while (n >= 0 && a[n] > b) n--;
      if (n >= 0 && a[n] != b) c++;
      if (n < 0) c++;
    }
    b *= q;
  }
  printf("%d\n", c);
  return 0;
}
