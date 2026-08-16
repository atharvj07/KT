#include <bits/stdc++.h>
using namespace std;
bool vis[1000008];
int link[1000008];
void solve() {
  int a, k, i, j, n, sum = 0, mx = 0, ind, ct = 1, curr = 0, remain = -1;
  cin >> n;
  int D[n + 5];
  for (i = 0; i < n; i++) {
    cin >> D[i];
    vis[D[i]] = 1;
  }
  link[D[n - 1]] = D[n - 1];
  for (i = 0; i < n - 1; i++) {
    link[D[i]] = D[i + 1];
  }
  if (D[0] == 0) {
    while (vis[++curr])
      ;
    cout << curr << " ";
    while (vis[++curr])
      ;
    remain = 0;
  } else {
    cout << 0 << " ";
    while (vis[++curr])
      ;
  }
  for (i = 1; i < n; i++) {
    if (D[i] != D[i - 1]) {
      cout << D[i - 1] << " ";
      if (remain == D[i - 1]) remain = -1;
      continue;
    }
    if (remain != D[i] && remain > -1) {
      cout << remain << " ";
      remain = -1;
    } else {
      cout << curr << " ";
      while (vis[++curr])
        ;
    }
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  solve();
  return 0;
}
