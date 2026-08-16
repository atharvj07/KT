#include <bits/stdc++.h>
using namespace std;
set<int> vis;
vector<int> ans;
map<int, int> d;
int main() {
  int n, m;
  cin >> n >> m;
  queue<int> q;
  int count = 0;
  for (int i = 0; i < n; i++) {
    int x;
    scanf("%d", &x);
    q.push(x);
    vis.insert(x);
    d[x] = 0;
  }
  long long int res = 0;
  while (!q.empty()) {
    int now = q.front();
    q.pop();
    if (int(ans.size()) == m) break;
    if (d[now] != 0) {
      res += d[now];
      ans.push_back(now);
    }
    if (vis.find(now - 1) != vis.end())
      res += 0;
    else {
      q.push(now - 1);
      vis.insert(now - 1);
      d[now - 1] = d[now] + 1;
    }
    if (vis.find(now + 1) != vis.end())
      continue;
    else {
      q.push(now + 1);
      vis.insert(now + 1);
      d[now + 1] = d[now] + 1;
    }
  }
  printf("%lld\n", res);
  for (int i = 0; i < ans.size(); i++) {
    printf("%d ", ans[i]);
  }
  cout << endl;
}
