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
ll memo[1001];
int calc(int idx, vector<string>& v){
  int N = v.size();
  if(idx == N) return 1;
  if(memo[idx] != -1) return memo[idx];
  ll &res = memo[idx];
  res = 0;
  string s;
  string mask[4] = {
    "0xxxxxxx",
    "110yyyyx10xxxxxx",
    "1110yyyy10yxxxxx10xxxxxx",
    "11110yyy10yyxxxx10xxxxxx10xxxxxx"
  };
  for(int l = 0; l < 4; l++){
    if(idx + l == N) return res;
    s += v[idx + l];
    bool y_judge[256] = {};
    bool ok = true;
    REP(i, mask[l].size()) {
      if(mask[l][i] == 'y'){
        y_judge[s[i]] = true;
      }
      if(mask[l][i] == '0' && s[i] == '1') ok = false;
      if(mask[l][i] == '1' && s[i] == '0') ok = false;
    }
    if(l >= 1 && !y_judge['x'] && !y_judge['1']) ok = false;
    if(!ok) continue;
    ll cnt1 = 1, cnt2 = 1;
    REP(i, mask[l].size()){
      if(mask[l][i] == 'y' && s[i] == 'x') cnt1 <<= 1;
      if(mask[l][i] == 'x' && s[i] == 'x') cnt2 <<= 1;
    }
    if(l >= 1 && !y_judge['1']) cnt1--;
    cnt1 %= 1000000;
    cnt2 %= 1000000;
    ll add = cnt1 * cnt2 * calc(idx + 1 + l, v);
    res += add % 1000000;
    res %= 1000000;
  }
  return res;
}
int main(){
  int N;
  while(cin>>N && N){
    vector<string> v(N);
    REP(i, N) cin>>v[i];
    memset(memo, -1, sizeof(memo));
    cout<<calc(0, v)<<endl;
  }
  return 0;
}