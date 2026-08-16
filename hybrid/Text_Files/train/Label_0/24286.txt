#include <bits/stdc++.h>
using namespace std;
struct kxj {
  int l, t;
} bri[200005], res[200005];
int n;
long long r, num;
void MinNum() {
  for (int i = 1; i <= n; i++) {
    int x = bri[i].l - bri[i].t;
    if (x > 0) {
      num += (x - 1) / r + 1;
      long long y = 2 * ((r - x % r) % r);
      while (i < n && bri[i + 1].l <= y) y -= bri[++i].l;
      if (i < n) bri[i + 1].l -= y, bri[i + 1].t -= y / 2;
    }
  }
}
void Plan() {
  long long T = 0;
  for (int i = 1; i <= n; i++) {
    int x = bri[i].l - bri[i].t;
    if (x > 0) {
      long long s = bri[i].t - x + 1;
      T += s - 1;
      while (s <= bri[i].l) {
        cout << T << " ";
        s += r + r;
        T += r;
      }
      s -= bri[i].l + 1;
      while (i < n && bri[i + 1].l <= s) s -= bri[++i].l;
      if (i < n) bri[i + 1].l -= s, bri[i + 1].t -= s / 2;
    } else
      T += bri[i].l;
  }
}
int main() {
  scanf("%d %I64d\n", &n, &r);
  for (int i = 1; i <= n; i++) scanf("%d", &bri[i].l), bri[i].l *= 2;
  for (int i = 1; i <= n; i++) scanf("%d", &bri[i].t);
  for (int i = 1; i <= n; i++)
    if (bri[i].t * 2 < bri[i].l) {
      puts("-1");
      return 0;
    }
  for (int i = 1; i <= n; i++) res[i] = bri[i];
  MinNum();
  cout << num << endl;
  if (num > 100000) return 0;
  for (int i = 1; i <= n; i++) bri[i] = res[i];
  Plan();
  return 0;
}
