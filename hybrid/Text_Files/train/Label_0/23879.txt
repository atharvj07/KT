#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <complex>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <queue>
#include <set>
#include <map>
#include <valarray>
#include <bitset>
#include <stack>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef long long ll;
typedef pair<int,int> pii;
const int INF = 1<<29;
const double PI = acos(-1);
const double EPS = 1e-8;

struct Cat {
  int s;
  int w, c;
  Cat() {}
  Cat(int s, int w, int c) : s(s),w(w),c(c) {}
  bool operator<(const Cat &rhs) const {
    return c < rhs.c;
  }
};

Cat cats[1000];
int dp[2][10001];
int Na, Nb, W;
bool exist[2];

bool add(int &x) {
  if (x == Na+Nb) return 0;
  int s = cats[x].s;
  exist[s] = 1;
  for (int i=W-cats[x].w; i>=0; --i) {
    int w = i+cats[x].w;
    if (i == 0 || dp[s][i] != -1) {
      if (i == 0) dp[s][w] = x;
      else dp[s][w] = max(dp[s][w], dp[s][i]);
    }
  }
  x++;
  return 1;
}

bool erase(int &x) {
  if (x == Na+Nb) return 0;
  bool f = 0;
  int s = cats[x].s;
  REP(i,W+1) {
    if (dp[s][i] == x) dp[s][i] = -1;
    if (dp[s][i] != -1) f = 1;
  }
  exist[s] = f;
  x++;
  return 1;
}

int main() {
  cin >> Na >> Nb >> W;
  REP(i,Na) {
    int m, c;
    cin >> m >> c;
    cats[i] = Cat(0,m,c);
  }
  REP(i,Nb) {
    int m, c;
    cin >> m >> c;
    cats[i+Na] = Cat(1,m,c);
  }
  sort(cats,cats+Na+Nb);
  memset(dp,-1,sizeof(dp));
  // REP(i,Na+Nb) {
  //   cout << cats[i].s << " " << cats[i].c << " " << cats[i].w << endl;
  // }

  // dp[0][0] = 100000;
  // dp[0][0] = 100000;
  int head=0, tail=0;
  int ans = INT_MAX;
  while(1) {
    while(!exist[0]||!exist[1]) {
      if (!add(head)) break;
    }
    if (!exist[0]||!exist[1]) break;
    int w = INT_MAX;
    int p[2] = {-2000000000,-2000000000};
    REP(i,W+1) {
      REP(j,2) {
        if (dp[j][i] >= 0) {
          w = min(w, abs(i-p[j^1]));
          p[j] = i;
        }
      }
    }
    int c = cats[head-1].c-cats[tail].c;
    // cout << w << " " << c << endl;
    // cout << head << ", " << tail << endl;
    
    ans = min(ans, max(w, c));
    if (w > c) {
      if (!add(head)) break;
    } else {
      if (!erase(tail)) break;
    }
  }
  cout << ans << endl;
}