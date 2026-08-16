#include <bits/stdc++.h>
using namespace std;
vector<long long int> gp[100005];
bool visited[100005] = {false};
long long int arr[100005];
long long int n, k;
long long int ct = 0;
double depth[100005] = {-1};
bool flag = false;
void bfs(long long int root) {
  queue<long long int> q;
  q.push(root);
  visited[root] = true;
  ct++;
  while (!q.empty()) {
    long long int curr = q.front();
    q.pop();
    for (long long int x : gp[curr]) {
      if (!visited[x]) {
        q.push(x);
        visited[x] = true;
        ct++;
        depth[x] = 1 - depth[curr];
      } else {
        if (depth[x] == depth[curr]) {
          flag = true;
          break;
        }
      }
    }
  }
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> n >> k;
  for (long long i = 0, u, v; i < k; ++i) {
    cin >> u >> v;
    gp[u].push_back(v);
    gp[v].push_back(u);
  }
  for (long long int i = 1; i < n + 1; i++) {
    if ((!visited[i]) && (gp[i].size() != 0)) {
      bfs(i);
    }
  }
  if (flag == true) {
    cout << -1 << "\n";
    return 0;
  }
  vector<long long> one, zero;
  for (long long i = 1; i < n + 1; ++i) {
    if (visited[i]) {
      (depth[i] == 1) ? one.push_back(i) : zero.push_back(i);
    }
  }
  cout << zero.size() << "\n";
  for (long long int x : zero) {
    cout << x << " ";
  }
  cout << "\n";
  cout << one.size() << "\n";
  for (long long int x : one) {
    cout << x << " ";
  }
  cout << "\n";
}
