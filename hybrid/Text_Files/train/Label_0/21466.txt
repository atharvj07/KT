#include <bits/stdc++.h>
using namespace std;
int ns[305];
int flag[305];
char sign[305][305];
int n;
int coun;
vector<int> tmpsort;
vector<int> az[305];
queue<int> Q;
void justdoit() {
  int i, tmp, j;
  for (i = 0; i < n; ++i) {
    if (flag[i]) continue;
    Q.push(i);
    coun++;
    flag[i] = 1;
    while (!Q.empty()) {
      tmp = Q.front();
      Q.pop();
      az[coun - 1].push_back(tmp);
      for (j = 0; j < n; j++) {
        if (sign[tmp][j] == '1') {
          if (flag[j]) continue;
          Q.push(j);
          flag[j] = 1;
        }
      }
    }
  }
}
int main() {
  scanf("%d", &n);
  int i, j, k;
  for (i = 0; i < n; ++i) {
    scanf("%d", &ns[i]);
  }
  getchar();
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      scanf("%c", &sign[i][j]);
    }
    getchar();
  }
  justdoit();
  for (i = 0; i < coun; i++) {
    tmpsort.clear();
    for (j = 0; j < az[i].size(); j++) {
      tmpsort.push_back(ns[az[i][j]]);
    }
    sort(tmpsort.begin(), tmpsort.end());
    for (j = 0; j < az[i].size(); j++) {
      sort(az[i].begin(), az[i].end());
      ns[az[i][j]] = tmpsort[j];
    }
  }
  for (i = 0; i < n; i++) {
    printf("%d ", ns[i]);
  }
  return 0;
}
