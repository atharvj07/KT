#include <bits/stdc++.h>
using namespace std;
const int maxm = 3e5 + 5;
int fa[maxm << 1], cnt[maxm << 1], n, k, state[maxm][2];
int Find(int x) { return fa[x] == x ? x : fa[x] = Find(fa[x]); }
void Union(int x, int y) {
  x = Find(x), y = Find(y);
  if (y == 0) swap(x, y);
  fa[y] = x;
  if (x) cnt[x] += cnt[y];
}
int calc(int x) {
  int y = x <= k ? x + k : x - k;
  x = Find(x), y = Find(y);
  if (x == 0 || y == 0) return cnt[x + y];
  return min(cnt[x], cnt[y]);
}
void run_case() {
  cin >> n >> k;
  string str;
  cin >> str;
  for (int i = 1; i <= k; ++i) {
    int num, lamp;
    cin >> num;
    while (num--) {
      cin >> lamp;
      if (!state[lamp][0])
        state[lamp][0] = i;
      else
        state[lamp][1] = i;
    }
    fa[i] = i, fa[i + k] = i + k, cnt[i + k] = 1;
  }
  int ans = 0;
  for (int i = 1; i <= n; ++i) {
    if (!state[i][1]) {
      int x = state[i][0];
      if (x) {
        ans -= calc(x);
        if (str[i - 1] == '0') {
          fa[Find(x)] = 0;
        } else
          fa[Find(x + k)] = 0;
        ans += calc(x);
      }
    } else {
      int x = state[i][0], y = state[i][1];
      if (str[i - 1] == '0') {
        if (Find(x + k) != Find(y)) {
          ans -= calc(x), ans -= calc(y);
          Union(x, y + k), Union(x + k, y);
          ans += calc(x);
        }
      } else {
        if (Find(x) != Find(y)) {
          ans -= calc(x), ans -= calc(y);
          Union(x, y), Union(x + k, y + k);
          ans += calc(x);
        }
      }
    }
    cout << ans << "\n";
  }
}
int main() {
  ios::sync_with_stdio(false), cin.tie(0);
  run_case();
  return 0;
}
