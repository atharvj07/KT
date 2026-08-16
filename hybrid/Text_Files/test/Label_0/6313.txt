#include <bits/stdc++.h>
using namespace std;
long long unsigned int countDivisors(long long unsigned int n) {
  long long unsigned int cnt = 0;
  for (long long unsigned int i = 1; i <= sqrt(n); i++) {
    if (n % i == 0) {
      if (n / i == i)
        ++cnt;
      else
        cnt += 2;
    }
  }
  return cnt;
}
int findFirst(const std::vector<long long int> &array, int key, int low,
              int high) {
  int ans = -1;
  while (low <= high) {
    int mid = low + (high - low) / 2;
    if (key == array[mid]) {
      ans = mid;
      high = mid - 1;
    } else if (key > array[mid])
      low = mid + 1;
    else
      high = mid - 1;
  }
  return ans;
}
int findLast(const std::vector<long long int> &array, int key, int low,
             int high) {
  int ans = -1;
  while (low <= high) {
    int mid = low + (high - low) / 2;
    if (key == array[mid]) {
      ans = mid;
      low = mid + 1;
    } else if (key > array[mid])
      low = mid + 1;
    else
      high = mid - 1;
  }
  return ans;
}
int d, x, y;
void extendedEuclid(int a, int b) {
  if (b == 0) {
    d = 1;
    x = 1;
    y = 0;
  } else {
    extendedEuclid(b, a % b);
    int temp = x;
    x = y;
    y = temp - (a / b) * y;
  }
}
const int N = 2 * (2e5 + 5);
vector<int> adj[N];
vector<int> level(N, 0);
vector<bool> vis(N, 0);
void BFS(int s) {
  queue<int> q;
  q.push(s);
  vis[s] = 1;
  level[s] = 0;
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int j = 0; j < adj[v].size(); j++) {
      int w = adj[v][j];
      if (!vis[w]) {
        q.push(w);
        vis[w] = 1;
        level[w] = 1 + level[v];
      }
    }
  }
}
void dfs(int s) {
  vis[s] = 1;
  for (int j = 0; j < adj[s].size(); j++) {
    int w = adj[s][j];
    if (!vis[w]) {
      dfs(w);
    }
  }
}
bool cmp(const pair<int, long long int> &a, const pair<int, long long int> &b) {
  return a.second < b.second;
}
int main() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  ;
  int n, m, x, y, c;
  cin >> n >> m;
  vector<pair<int, long long int> > arr(n + 1);
  for (int i1 = 1; i1 <= n; i1++) {
    cin >> c;
    arr[i1].first = i1;
    arr[i1].second = c;
  }
  sort(arr.begin(), arr.end(), cmp);
  for (int i = 0; i < m; i++) {
    cin >> x >> y;
    adj[x].push_back(y);
    adj[y].push_back(x);
  }
  long long unsigned int ans = 0;
  for (int i = 1; i <= n; i++) {
    int v = arr[i].first;
    long long int cost = arr[i].second;
    if (!vis[v]) {
      dfs(v);
      ans += cost;
    }
  }
  cout << ans << endl;
  return 0;
}
