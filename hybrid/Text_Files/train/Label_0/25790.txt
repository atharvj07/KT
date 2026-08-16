#include <iostream>
#include <complex>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
#include <set>
#include <limits>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define REP(i, j) for(int i = 0; i < (int)(j); ++i)
#define FOR(i, j, k) for(int i = (int)(j); i < (int)(k); ++i)
#define SORT(v) sort((v).begin(), (v).end())
#define REVERSE(v) reverse((v).begin(), (v).end())
typedef pair<char, int> P;

vector<P> sort_v(vector<P> &v, vector<int> &used, int now){
  vector<P> res;
  REP(i, now + 1) REP(j, 9) if(used[j] == i) res.push_back(v[j]);
  return res;
}

bool check(vector<P> &vv, vector<int> &used, int now){
  vector<P> v = sort_v(vv, used, now);
  for(int i = 0; i + 2 < v.size(); i += 3){
    if(!(v[i].first == v[i + 1].first && v[i + 1].first == v[i + 2].first)) return 0;
    if(!(v[i].second == v[i + 1].second && v[i + 1].second == v[i + 2].second) && !(v[i].second == v[i + 1].second - 1 && v[i + 1].second == v[i + 2].second - 1)) return 0;
  }
  return true;
}

bool dfs(vector<P> &v, vector<int> &used, int now){
  if(now >= 9) return 1;
  bool res = 0;
  REP(i, 9){
    if(used[i] != -1) continue;
    used[i] = now;
    if(check(v, used, now)) res = max(res, dfs(v, used, now + 1));
    used[i] = -1;
  }
  return res;
}

int main() {
  int T; cin >>T;
  REP(t, T){
    vector<P> v(9);
    REP(i, 9) cin >>v[i].second;
    REP(i, 9) cin >>v[i].first;
    vector<int> used(9, -1);
    cout <<dfs(v, used, 0) <<endl;
  }
  return 0;
}