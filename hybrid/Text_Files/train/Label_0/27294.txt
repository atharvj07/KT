#include <bits/stdc++.h>
using namespace std;
int n, ans, last;
int f1[200000 + 10], f2[200000 + 10], t1[200000 + 10], t2[200000 + 10];
struct NODE {
  int s, t;
  NODE(){};
  NODE(int _s, int _t) : s(_s), t(_t) {}
} node[200000 + 10];
void scan() {
  f1[0] = f2[0] = ans = 0;
  for (int i = 0; i < 200000 + 10; i++) t1[i] = t2[i] = 0x3f3f3f3f;
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    f1[i] = f1[i - 1];
    f2[i] = f2[i - 1];
    if (x == 1)
      f1[i]++;
    else
      f2[i]++;
    if (i == n) last = x;
  }
  for (int i = 1; i <= n; i++) {
    t1[f1[i]] = min(t1[f1[i]], i);
    t2[f2[i]] = min(t2[f2[i]], i);
  }
  return;
}
void solve() {
  for (int i = 1; i <= n; i++) {
    int win1, win2, now;
    win1 = win2 = now = 0;
    while (1) {
      int n1, n2;
      n1 = f1[now] + i;
      n2 = f2[now] + i;
      n1 = t1[n1];
      n2 = t2[n2];
      if (n1 < n2)
        win1++;
      else if (n1 > n2)
        win2++;
      int temp = min(n1, n2);
      if (temp == n) {
        if (last == 1 && n1 == n && win1 > win2) node[ans++] = NODE(win1, i);
        if (last == 2 && n2 == n && win2 > win1) node[ans++] = NODE(win2, i);
        break;
      }
      if (temp > n) break;
      if (n1 < n2)
        now = n1;
      else
        now = n2;
    }
  }
  return;
}
bool cmp(NODE a, NODE b) {
  if (a.s == b.s) return a.t < b.t;
  return a.s < b.s;
}
void print() {
  printf("%d\n", ans);
  sort(node, node + ans, cmp);
  for (int i = 0; i < ans; i++) printf("%d %d\n", node[i].s, node[i].t);
  return;
}
int main() {
  while (scanf("%d", &n) != EOF) {
    scan();
    solve();
    print();
  }
  return 0;
}
