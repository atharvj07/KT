#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5 + 5;
int v[maxn], color[maxn], used[maxn], cnt[maxn];
int main() {
  int n, m;
  cin >> n >> m;
  for (int i = 1; i <= n; i++) cin >> v[i];
  for (int i = 1; i <= m; i++) cin >> color[i];
  int sat = 0, sum = 0;
  for (int i = 1; i <= m; i++) {
    sum += color[i];
    if (color[i] == 0) {
      sat++;
      used[i] = 1;
    }
  }
  deque<int> dq;
  int res = 1e9;
  for (int x : v) {
    dq.push_back(x);
    cnt[x]++;
    if (cnt[x] == color[x]) sat++;
    while (!dq.empty() && cnt[dq.front()] > color[dq.front()]) {
      cnt[dq.front()]--;
      dq.pop_front();
    }
    if (sat == m) res = min(res, (int)dq.size() - sum);
  }
  if (res == 1e9)
    cout << -1 << endl;
  else
    cout << res << endl;
  return 0;
}
