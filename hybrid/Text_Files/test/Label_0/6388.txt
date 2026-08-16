#include <bits/stdc++.h>
using namespace std;
int a[100005], b[100005], ansx, ansy, n, qst, qed, now, ansk, x, y, l;
bool find(int nx, int t) {
  qst = 1;
  qed = 1;
  now = b[1];
  while (qst <= n) {
    if (now == nx) {
      if (t == 0)
        return 1;
      else {
        if (a[qed] - x >= 0 || a[qed] + y <= l) return 1;
      }
    }
    if (qed < qst && now > nx) {
      now -= b[qed];
      qed++;
    } else {
      qst++;
      now += b[qst];
    }
  }
  return 0;
}
int main() {
  int i, j, m;
  scanf("%d%d%d%d", &n, &l, &x, &y);
  for (i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
    b[i - 1] = a[i] - a[i - 1];
  }
  n--;
  if (!find(x, 0)) ansx++;
  if (!find(y, 0)) ansy++;
  if (x == y && ansx) {
    printf("%d\n%d\n", 1, x);
  } else if (x != y && ansx && ansy) {
    if (find(x + y, 0)) ansk++;
    if (ansk) {
      printf("1\n%d\n", x + a[qed]);
    } else {
      if (find(y - x, 1)) ansk++;
      if (ansk) {
        printf("1\n");
        if (a[qed] - x >= 0)
          printf("%d\n", a[qed] - x);
        else
          printf("%d\n", a[qed] + y);
      } else
        printf("2\n%d %d\n", x, y);
    }
  } else {
    if (ansx + ansy == 2) {
      printf("2\n%d %d\n", x, y);
    } else {
      printf("%d\n", ansx + ansy);
      if (ansx) printf("%d\n", x);
      if (ansy) printf("%d\n", y);
    }
  }
  return 0;
}
