#include <bits/stdc++.h>
using namespace std;
long long int curr[200005], mx[200005], arr[200005], n, inf = -9999999999,
                                                        m = -9999999999;
vector<long long int> v[200005];
long long int dfs(long long int a, long long int p) {
  curr[a] = arr[a];
  for (auto it : v[a]) {
    if (it != p) {
      curr[a] += dfs(it, a);
      mx[a] = max(mx[a], mx[it]);
    }
  }
  mx[a] = max(mx[a], curr[a]);
  return curr[a];
}
void ds(long long int a, long long int p) {
  vector<long long int> vec;
  for (auto it : v[a]) {
    if (it != p) {
      ds(it, a);
    }
  }
  if (v[a].size() > 2) {
    for (auto it : v[a]) {
      if (it != p) {
        vec.push_back(mx[it]);
      }
    }
    sort(vec.begin(), vec.end(), greater<long long int>());
    m = max(m, vec[0] + vec[1]);
  }
}
int main() {
  long long int i, a, b, sum;
  cin >> n;
  for (i = 1; i <= n; i++) {
    cin >> arr[i];
    mx[i] = inf;
  }
  for (i = 1; i < n; i++) {
    cin >> a >> b;
    v[a].push_back(b);
    v[b].push_back(a);
  }
  v[1].push_back(0);
  dfs(1, 0);
  ds(1, 0);
  if (m == inf)
    cout << "Impossible";
  else
    cout << m;
  return 0;
}
