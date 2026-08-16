#include <bits/stdc++.h>
using namespace std;
struct kxj {
  int a, b;
} q[205];
int l[205], r[205];
int main() {
  int n;
  scanf("%d", &n);
  for (int a, b, i = 1; i <= n; i++) {
    scanf("%d %d", &a, &b);
    q[i] = (kxj){a, b};
  }
  int t = 0;
  l[t] = 1;
  r[t++] = 2000000007;
  for (int i = 1; i <= n; i++) {
    int s = 2000000007, id = -1;
    bool flag = 0;
    for (int j = 0; j < t; j++) {
      if (!flag && r[j] >= l[j] + q[i].b - 1 && s > l[j]) s = l[j], id = j;
      if (l[j] <= q[i].a && r[j] >= q[i].a && r[j] >= q[i].a + q[i].b - 1)
        s = q[i].a, id = j, flag = 1;
    }
    printf("%d %d\n", s, s + q[i].b - 1);
    if (s == l[id])
      l[id] = s + q[i].b;
    else {
      l[t] = s + q[i].b;
      r[t++] = r[id];
      r[id] = s - 1;
    }
  }
  return 0;
}
