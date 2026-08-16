#include <bits/stdc++.h>
using namespace std;
const int seed = 999983;
inline int read() {
  int n = 0, f = 1;
  char c;
  for (c = getchar(); c < '0' || c > '9'; c = getchar())
    if (c == '-') f = -1;
  for (; c >= '0' && c <= '9'; c = getchar()) n = n * 10 + c - '0';
  return n * f;
}
int sz[105], bj[105], n;
unsigned long long val[105];
vector<unsigned long long> tmp[105], Tmp;
bool vis[105];
multiset<unsigned long long> MP;
struct Tree {
  vector<int> to[105];
  int r1, r2, num;
  unsigned long long vl;
  void predfs(int x, int fa) {
    sz[x] = 1;
    for (int i = 0; i <= (int)to[x].size() - 1; i++)
      if (to[x][i] != fa && !vis[to[x][i]])
        predfs(to[x][i], x), sz[x] += sz[to[x][i]];
  }
  void findrt(int x, int fa, int size) {
    bj[x] = 0;
    for (int i = 0; i <= (int)to[x].size() - 1; i++)
      if (to[x][i] != fa && !vis[to[x][i]])
        findrt(to[x][i], x, size), bj[x] = max(bj[x], sz[to[x][i]]);
    bj[x] = max(bj[x], size - sz[x]);
    if (!r1 || bj[x] < bj[r1])
      r1 = x, r2 = 0;
    else if (r1 && bj[x] == bj[r1])
      r2 = x;
  }
  unsigned long long dfs(int x, int fa) {
    vector<unsigned long long>().swap(tmp[x]);
    vis[x] = 1;
    for (int i = 0; i <= (int)to[x].size() - 1; i++) {
      int t = to[x][i];
      if (t == fa || vis[t]) continue;
      tmp[x].push_back(dfs(t, x));
    }
    sort(tmp[x].begin(), tmp[x].end());
    unsigned long long ans = 1;
    for (int i = 0; i <= (int)tmp[x].size() - 1; i++)
      ans = ans * seed + tmp[x][i];
    return ans;
  }
  unsigned long long cal_hash(int x) {
    predfs(x, 0);
    r1 = r2 = 0;
    findrt(x, 0, sz[x]);
    if (!r2) return dfs(r1, 0);
    unsigned long long a1 = dfs(r1, r2), a2 = dfs(r2, r1);
    if (a1 > a2) swap(a1, a2);
    return a1 * seed + a2;
  }
  void init() {
    for (int i = 1; i <= n; i++) vector<int>().swap(to[i]);
    for (int m = read(); m--;) {
      int x = read(), y = read();
      to[x].push_back(y);
      to[y].push_back(x);
    }
    for (int i = 1; i <= n; i++) vis[i] = 0;
    num = 0;
    vector<unsigned long long>().swap(Tmp);
    for (int i = 1; i <= n; i++)
      if (!vis[i]) {
        ++num;
        Tmp.push_back(cal_hash(i));
      }
    sort(Tmp.begin(), Tmp.end());
    vl = 0;
    for (int i = 0; i <= (int)Tmp.size() - 1; i++) vl = vl * seed + Tmp[i];
  }
  bool check(int fo) {
    MP.clear();
    for (int i = 1; i <= n; i++) MP.insert(val[i]);
    for (int i = 1; i <= n; i++) {
      vector<unsigned long long>().swap(Tmp);
      Tmp.push_back(1);
      for (int j = 1; j <= n; j++) vis[j] = 0;
      vis[i] = 1;
      for (int j = 0; j <= (int)to[i].size() - 1; j++) {
        Tmp.push_back(cal_hash(to[i][j]));
      }
      sort(Tmp.begin(), Tmp.end());
      unsigned long long _vl = 0;
      for (int j = 0; j <= (int)Tmp.size() - 1; j++) _vl = _vl * seed + Tmp[j];
      if (MP.find(_vl) == MP.end())
        return 0;
      else
        MP.erase(MP.find(_vl));
    }
    return 1;
  }
  void print() {
    for (int i = 1; i <= n; i++)
      for (int j = 0; j <= (int)to[i].size() - 1; j++) {
        int t = to[i][j];
        if (t < i) printf("%d %d\n", t, i);
      }
  }
} T[105];
void solve() {
  n = read(), n = read();
  for (int i = 1; i <= n; i++) T[i].init(), val[i] = T[i].vl;
  for (int i = 1; i <= n; i++)
    if (T[i].num == 2) {
      for (int j = 1; j <= n; j++)
        if (T[i].to[j].empty()) {
          for (int k = 1; k <= n; k++)
            if (k ^ j) {
              T[i].to[j].push_back(k);
              T[i].to[k].push_back(j);
              if (T[i].check(j)) {
                puts("YES");
                T[i].print();
                return;
              }
              T[i].to[j].pop_back();
              T[i].to[k].pop_back();
            }
        }
      break;
    }
  puts("NO");
}
int main() {
  for (int cas = read(); cas--;) solve();
  return 0;
}
