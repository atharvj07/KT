#include <bits/stdc++.h>
using namespace std;
template <typename T>
void gmin(T &a, T b) {
  a = a < b ? a : b;
}
template <typename T>
void gmax(T &a, T b) {
  a = a > b ? a : b;
}
const int MAXN = 100010;
int n, m, ans;
map<int, int> mp[MAXN];
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < m; i++) {
    int x, y, w, v;
    scanf("%d%d%d", &x, &y, &w);
    map<int, int>::iterator itr = mp[x].find(w);
    if (itr != mp[x].end()) {
      v = (itr == mp[x].begin()) ? 1 : (--itr)->second + 1;
    } else {
      mp[x].insert(make_pair(w, 0));
      itr = mp[x].find(w);
      if (itr == mp[x].begin()) v = 1;
      v = (itr == mp[x].begin()) ? 1 : (--itr)->second + 1;
      mp[x].erase(w);
    }
    gmax(ans, v);
    itr = mp[y].find(w);
    if (itr != mp[y].end()) {
      gmax(mp[y][w], v);
    } else {
      mp[y][w] = v;
      itr = mp[y].find(w);
      if (itr != mp[y].begin()) {
        --itr;
        if (itr->second >= v) {
          mp[y].erase(++itr);
          continue;
        }
        ++itr;
      }
    }
    for (map<int, int>::iterator tmp = itr;; tmp = itr) {
      ++tmp;
      if (tmp != mp[y].end() && tmp->second <= v)
        mp[y].erase(tmp);
      else
        break;
    }
  }
  printf("%d\n", ans);
  return 0;
}
