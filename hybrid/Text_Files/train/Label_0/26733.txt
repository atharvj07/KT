#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define FOR(i,k,n) for(int i=(k); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

template<class T> void debug(T begin, T end){ for(T i = begin; i != end; ++i) cerr<<*i<<" "; cerr<<endl; }
inline bool valid(int x, int y, int W, int H){ return (x >= 0 && y >= 0 && x < W && y < H); }

typedef long long ll;
const int INF = 100000000;
const double EPS = 1e-8;
const int MOD = 1000000007;
int dx[8] = {1, 0, -1, 0, 1, -1, -1, 1};
int dy[8] = {0, 1, 0, -1, 1, 1, -1, -1};
vector<int> v;
vector<int> cnt;
int N, M, G;
double p[8][8] = {};
double memo[390626];
int pow5[8];
double dfs(const int S){
  if(memo[S] >= 0) return memo[S];
  if(S == G) return memo[S] = 1.0;
  vector<int> cur(N);
  int idx = 0;
  int TMPS = S;
  REP(i, N){
    cur[i] = TMPS % 5;
    idx += cur[i];
    TMPS /= 5;
  }
  if(idx == v.size()) return memo[S] = 0.0;
  int u = v[idx];
  memo[S] = 0;
  REP(v, N){
    if(cur[v] + 1 > cnt[v]) continue;
    int NS = S + pow5[v];
    memo[S] += p[u][v] * dfs(NS);
  }
  return memo[S];
}

int main(){
  pow5[0] = 1;
  for(int i = 1; i < 8; i++) pow5[i] = 5 * pow5[i - 1];
  int CASENUM = 1;
  while(cin >> N && N){
    printf("Case %d: ", CASENUM++);
    v.clear();
    cnt = vector<int>(N);
    G = 0;
    REP(i, 390626) memo[i] = -1.0;

    REP(i, N) REP(j, N) cin >> p[i][j];

    REP(i, N){
      int t; cin >> t;
      cnt[i] = t;
      REP(j, t) v.push_back(i);
      G += t * pow5[i];
    }

    M = v.size();

    double ans = dfs(0);
    if(ans == 0.0) cout << "-INFINITY" << endl;
    else printf("%.8lf\n", log(ans));
  }
  return 0;
}