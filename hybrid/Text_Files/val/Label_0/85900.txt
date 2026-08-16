#include <bits/stdc++.h>
using namespace std;
int vals[200005];
int par[200005];
int len[200005];
int li[200005];
int FIND(int x) {
  if (x == par[x]) return x;
  return par[x] = FIND(par[x]);
}
bool isUNION(int a, int b) { return FIND(a) == FIND(b); }
void UNION(int a, int b) {
  int pa = FIND(a);
  int push_back = FIND(b);
  par[pa] = push_back;
  len[push_back] += len[pa];
  li[push_back] = min(li[pa], li[push_back]);
}
map<pair<int, int>, int> chunks;
map<int, int> mleft;
int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &vals[i]);
    par[i] = i;
    len[i] = 1;
    li[i] = i;
  }
  for (int i = 0; i < n - 1; i++) {
    if (vals[i] == vals[i + 1]) {
      UNION(i, i + 1);
    }
  }
  for (int i = 0; i < n; i++) {
    int ind = FIND(i);
    int lenv = len[ind];
    int liv = li[ind];
    chunks[make_pair(-lenv, liv)] = ind;
    mleft[liv] = ind;
  }
  int ans = 0;
  while (!chunks.empty()) {
    int ind = chunks.begin()->second;
    int lenv = len[ind];
    int liv = li[ind];
    map<int, int>::iterator it = mleft.find(liv);
    int leftind = -1;
    if (it != mleft.begin()) {
      --it;
      leftind = it->second;
      ++it;
    }
    int rightind = -1;
    ++it;
    if (it != mleft.end()) {
      rightind = it->second;
    }
    --it;
    chunks.erase(chunks.begin());
    mleft.erase(it);
    if (rightind != -1 && leftind != -1 && vals[rightind] == vals[leftind]) {
      lenv = len[rightind];
      liv = li[rightind];
      chunks.erase(chunks.find(make_pair(-lenv, liv)));
      mleft.erase(mleft.find(liv));
      lenv = len[leftind];
      liv = li[leftind];
      chunks.erase(chunks.find(make_pair(-lenv, liv)));
      mleft.erase(mleft.find(liv));
      UNION(leftind, rightind);
      ind = FIND(leftind);
      lenv = len[ind];
      liv = li[ind];
      chunks[make_pair(-lenv, liv)] = ind;
      mleft[liv] = ind;
    }
    ans++;
  }
  cout << ans << "\n";
}
