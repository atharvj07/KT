#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T gcd(T a, T b) {
  while (b) {
    a %= b;
    swap(a, b);
  }
  return a;
}
inline int nxt() {
  int wow;
  scanf("%d", &wow);
  return wow;
}
inline long long int lxt() {
  long long int wow;
  scanf("%lld", &wow);
  return wow;
}
vector<int> v[1000002], temp;
int a[1000002], visited[1000002], ans[1000002];
bool comp(int x, int y) { return x > y; }
void dfs(int s) {
  visited[s] = 1;
  temp.push_back(s);
  for (int i = 0; i < v[s].size(); i++) {
    int t = v[s][i];
    if (visited[t] == 0) dfs(t);
  }
}
int main() {
  int n = nxt(), m = nxt();
  for (int i = 1; i <= n; i++) a[i] = nxt();
  for (int i = 0; i < m; i++) {
    int x = nxt(), y = nxt();
    v[x].push_back(y);
    v[y].push_back(x);
  }
  for (int i = 1; i <= n; i++) {
    if (visited[i] == 0) dfs(i);
    sort(temp.begin(), temp.end(), comp);
    vector<int> vara;
    for (int i = 0; i < temp.size(); i++) {
      vara.push_back(a[temp[i]]);
    }
    sort(vara.begin(), vara.end());
    for (int i = 0; i < temp.size(); i++) {
      ans[temp[i]] = vara[i];
    }
    temp.clear();
  }
  for (int i = 1; i <= n; i++) cout << ans[i] << ' ';
  cout << endl;
  return 0;
}
