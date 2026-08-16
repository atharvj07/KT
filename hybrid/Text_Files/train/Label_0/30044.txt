#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 10;
struct Node {
  long long num, t;
  bool operator<(const Node &b) const {
    if (t == b.t) return num < b.num;
    return t > b.t;
  }
} a[maxn];
map<int, int> pre;
int findx(int x) { return pre[x] == 0 ? x : pre[x] = findx(pre[x]); }
void merge(int x, int y) {
  int i = findx(x), j = findx(y);
  if (i != j) pre[i] = j;
}
int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> a[i].num;
  for (int i = 1; i <= n; i++) cin >> a[i].t;
  sort(a + 1, a + n + 1);
  long long ans = 0;
  for (int i = 1; i <= n; i++) {
    int res = findx(a[i].num);
    if (res == a[i].num)
      merge(res, res + 1);
    else {
      merge(res, res + 1);
      ans += 1ll * (res - a[i].num) * a[i].t;
    }
  }
  cout << ans << "\n";
  return 0;
}
