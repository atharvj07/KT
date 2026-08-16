#include <bits/stdc++.h>
using namespace std;
int k, n;
pair<long long, long long> s[7];
pair<long long, long long> m[1000];
vector<int> hits[7][1000];
vector<int> edges[7];
int vis[10];
int w;
void dfs(vector<int> done, vector<int> need, vector<int> rem) {
  if (w) return;
  if (need.size() > rem.size()) return;
  if (need.size() == 0) {
    w = 1;
    return;
  }
  for (int i = 0; i < rem.size(); i++) {
    vector<int> done1;
    vector<int> need1;
    vector<int> rem1;
    for (int c = 1; c < need.size(); c++) need1.push_back(need[c]);
    for (int c = 0; c < done.size(); c++) done1.push_back(done[c]);
    for (int d = 0; d < rem.size(); d++)
      if (d != i) rem1.push_back(rem[d]);
    for (int f = 0; f < hits[rem[i]][need[0]].size(); f++) {
      int a = hits[rem[i]][need[0]][f];
      int no = 0;
      for (int g = 0; g < done1.size(); g++) {
        if (done1[g] == a) {
          no = 1;
        }
      }
      for (int g = 0; g < need1.size(); g++) {
        if (need1[g] == a) {
          no = 1;
        }
      }
      if (!no) need1.push_back(a);
      if (need1.size() > rem1.size()) continue;
    }
    done1.push_back(need[0]);
    dfs(done1, need1, rem1);
  }
}
int main() {
  cin >> k >> n;
  for (int i = 0; i < k; i++) {
    cin >> s[i].first >> s[i].second;
  }
  for (int i = 0; i < n; i++) {
    cin >> m[i].first >> m[i].second;
  }
  for (int i = 0; i < k; i++) {
    for (int j = 0; j < n; j++) {
      for (int c = 0; c < n; c++) {
        if (c == j) continue;
        long long a = (s[i].first - m[j].first) * (s[i].second - m[c].second);
        long long b = (s[i].first - m[c].first) * (s[i].second - m[j].second);
        if (a != b) continue;
        if ((s[i].first - m[c].first) * (m[j].first - m[c].first) > 0) continue;
        if ((s[i].second - m[c].second) * (m[j].second - m[c].second) > 0)
          continue;
        hits[i][j].push_back(c);
      }
    }
  }
  int ans = 0;
  for (int i = 0; i < n; i++) {
    w = 0;
    vector<int> used;
    vector<int> need;
    vector<int> rem;
    need.push_back(i);
    for (int j = 0; j < k; j++) rem.push_back(j);
    dfs(used, need, rem);
    ans += w;
  }
  cout << ans;
  cout << endl;
}
