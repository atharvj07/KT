#include <bits/stdc++.h>
using namespace std;
int n;
int a[1000008], f1[1000008], f2[1000008];
int x[1000008];
void init() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", a + i);
  }
  map<int, int> cnt;
  cnt.clear();
  for (int i = 0; i < n; i++) {
    cnt[a[i]]++;
    f1[i] = cnt[a[i]];
  }
  cnt.clear();
  for (int i = n - 1; i >= 0; i--) {
    cnt[a[i]]++;
    f2[i] = cnt[a[i]];
  }
}
inline int lowbit(int v) { return v & (-v); }
inline void update(int size, int pos, int delta) {
  while (pos <= size) {
    x[pos] += delta;
    pos += lowbit(pos);
  }
}
inline int get_sum(int pos) {
  int ret = 0;
  while (pos > 0) {
    ret += x[pos];
    pos -= lowbit(pos);
  }
  return ret;
}
void solve() {
  long long ans = 0;
  memset(x, 0, sizeof(x));
  for (int i = n - 1; i >= 0; i--) {
    ans += get_sum(f1[i] - 1);
    update(n, f2[i], 1);
  }
  cout << ans << endl;
}
int main() {
  init();
  solve();
}
