//
// Created by maze on 2019/11/03.
//

#include <bits/stdc++.h>
using namespace std;

#define INF_LL (int64)le18
#define INF (int32)le9
#define REP(i, n) for(int64 i = 0; i < (n); i++)
#define FOR(i, a, b) for(int64 i = (a); i < (b); i++)
#define all(x) x.begin(), x.end()
#define fs first
#define sc second

using int32 = int_fast32_t;
using int64 = int_fast64_t;
using uint32 = uint_fast32_t;
using uint64 = uint_fast64_t;
using PII = pair<int32, int32>;
using PLL = pair<int64, int64>;

const double eps = 1e-10;

class UnionFind{
private:
  size_t n;
public:
  vector<int32> par;
  UnionFind(size_t n):n(n){
    par.resize(n, -1);
  }

  int32 root(int32 x){
    if(par[x] < 0)return x;
    return par[x] = root(par[x]);
  }

  int32 size(int32 x){
    return -par[root(x)];
  }

  bool unite(int32 x, int32 y){
    x = root(x);
    y = root(y);
    if(x == y)return false;
    if(size(x) < size(y))swap(x, y);
    par[x] += par[y];
    par[y] = x;
    return true;
  }

  bool same(int32 x, int32 y){
    return root(x) == root(y);
  }

};
//
//int main() {
//  int64 n;
//  cin >> n;
//  map<int64, vector<PII>> mp;
//  vector<int64> a(n);
//  REP(i, n) cin >> a[i];
//  sort(all(a));
//  REP(i, n) {
//    FOR(j, i+1, n) {
//      if (abs(a[i]-a[j]) * 2 >= abs(a[0]-a.back())) continue;
////      cout << i << " " << j << endl;
//      mp[abs(a[i]-a[j])].emplace_back(i, j);
//    }
//  }
//
//  int64 res = 2;
//  UnionFind uf(n);
//  for (auto &v : mp) {
//    for (auto &p : v.sc) {
//      uf.unite(p.fs, p.sc);
//      res = max(res, (int64)max(uf.size(p.fs), uf.size(p.sc)));
//    }
//
//    for (auto &p : v.sc) {
//      uf.par[p.fs] = -1;
//      uf.par[p.sc] = -1;
//    }
//  }
//  cout << res << endl;
//}

int main(void) {
  int64 n;
  cin >> n;
  vector<int64> a(n);
  REP(i, n) cin >> a[i];

  sort(all(a));
  int64 res = 0;
  REP(i, n) {
    FOR(j, i+1, n) {
      int64 d =a[j] - a[i];
      int64 cnt = 2;
      if (*lower_bound(all(a), a[i]-d) == a[i]-d) continue;
      int64 v = a[j];
      while (*lower_bound(all(a), v+d) == v+d) {
        v += d;
        cnt++;
      }
      res = max(res, cnt);
    }
  }
  cout << res << endl;
}
