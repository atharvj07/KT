#include <bits/stdc++.h>
using namespace std;
vector<int> g[500];
vector<int> rg[500];
int n, m;
string s[500];
int curc = 0;
int color[500];
int color2[500];
set<int> c1[500];
set<int> c2[500];
void no() {
  cout << "No\n";
  exit(0);
}
void yes() {
  cout << "Yes\n";
  exit(0);
}
void dfs2(int j);
void dfs(int i) {
  c1[curc].insert(i);
  color[i] = curc;
  for (int j : g[i]) {
    if (color2[j] && color2[j] != curc) no();
    if (color2[j] == 0) {
      color2[j] = curc;
      dfs2(j);
    }
  }
}
void dfs2(int j) {
  c2[curc].insert(j);
  color2[j] = curc;
  for (int i : rg[j]) {
    if (color[i] && color[i] != curc) no();
    if (color[i] == 0) {
      color[i] = curc;
      dfs(i);
    }
  }
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    cin >> s[i];
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (s[i][j] == '#') {
        g[i].push_back(j);
        rg[j].push_back(i);
      }
    }
  }
  for (int i = 0; i < n; i++) {
    curc++;
    if (!color[i]) dfs(i);
  }
  for (int j = 0; j < m; j++) {
    curc++;
    if (!color2[j]) dfs2(j);
  }
  for (int c = 1; c <= curc; c++) {
    auto ii = c1[c];
    auto jj = c2[c];
    for (int i : ii) {
      for (int j : jj) {
        if (s[i][j] != '#') no();
      }
    }
  }
  cout << "Yes\n";
  return 0;
}
