#include <bits/stdc++.h>
using namespace std;
const int N = 1000050;
vector<vector<int>> v(N), s(N);
set<int> u;
void dfs(int i, int j) {
  if (i > j) {
    if (u.count(i) && u.count(j) == 1) {
      printf("No\n");
      exit(0);
    }
    u.insert(i);
    for (int k : v[i]) dfs(k, i);
  } else {
    if (u.count(i) == 0 && u.count(j) == 1) {
      u.insert(i);
      for (int k : v[i]) dfs(k, i);
    }
  }
}
int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) {
    int l;
    scanf("%d", &l);
    for (int j = 0; j < l; j++) {
      int in;
      scanf("%d", &in);
      s[i].push_back(in);
    }
  }
  for (int i = 0; i + 1 < n; i++) {
    for (int j = 0; j < s[i].size(); j++) {
      if (j == s[i + 1].size()) {
        printf("No\n");
        return 0;
      }
      if (s[i][j] != s[i + 1][j]) {
        v[s[i + 1][j]].push_back(s[i][j]);
        break;
      }
    }
  }
  for (int i = 1; i <= m; i++) {
    for (int j : v[i]) {
      dfs(j, i);
    }
  }
  for (int i = 0; i + 1 < n; i++) {
    for (int j = 0; j < s[i].size(); j++) {
      if (j == s[i + 1].size()) {
        printf("No\n");
        return 0;
      }
      if (s[i][j] == s[i + 1][j]) {
        continue;
      }
      if (s[i][j] > s[i + 1][j]) {
        if (!(u.count(s[i][j]) == 1 and u.count(s[i + 1][j]) == 0)) {
          printf("No\n");
          return 0;
        }
      } else {
        if (u.count(s[i][j]) == 0 and u.count(s[i + 1][j]) == 1) {
          return printf("No\n"), 0;
        }
      }
      break;
    }
  }
  printf("Yes\n%d\n", u.size());
  for (int next : u) {
    printf("%d ", next);
  }
}
