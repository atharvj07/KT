#include <bits/stdc++.h>
using namespace std;
map<int, vector<int> > mp;
map<int, int> visited;
int single_count = -1;
void dfs(int n) {
  if (visited[n]) return;
  cout << n << " ";
  visited[n] = 1;
  for (int i = 0; i < mp[n].size(); i++) {
    dfs(mp[n][i]);
  }
}
int main() {
  int total;
  cin >> total;
  for (int i = 0; i < total; i++) {
    int a;
    int b;
    cin >> a >> b;
    mp[a].push_back(b);
    mp[b].push_back(a);
  }
  for (map<int, vector<int> >::iterator it = mp.begin(); it != mp.end(); it++) {
    if ((*it).second.size() == 1) {
      single_count = (*it).first;
      break;
    }
  }
  dfs(single_count);
}
