#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <complex>
#include <string>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <bitset>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#ifndef LOCAL
#define debug(x) ;
#else
#define debug(x) cerr << __LINE__ << " : " << #x << " = " << (x) << endl;

template <typename T1, typename T2>
ostream &operator<<(ostream &out, const pair<T1, T2> &p) {
  out << "{" << p.first << ", " << p.second << "}";
  return out;
}

template <typename T>
ostream &operator<<(ostream &out, const vector<T> &v) {
  out << '{';
  for (const T &item : v) out << item << ", ";
  out << "\b\b}";
  return out;
}
#endif

#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 3010

char c[SIZE][SIZE];

set<pair<int,int>> ss;

int main(){
  int H, W;

  scanf("%d%d", &H, &W);

  for (int i=0; i<H; i++) {
    scanf("%s", c[i]);

    int l = INF, r = -1;
    for (int j=0; j<W; j++) {
      if (c[i][j] == 'B') {
        l = min(l, j);
        r = max(r, j);
      }
    }

    if (l != INF) {
      ss.insert({i, l});
      ss.insert({i, r});
    }
  }

  for (int j=0; j<W; j++) {
    int u = INF, d = -1;
    for (int i=0; i<H; i++) {
      if (c[i][j] == 'B') {
        u = min(u, i);
        d = max(d, i);
      }
    }
    if (u != INF) {
      ss.insert({u, j});
      ss.insert({u, j});
    }
  }

  int ans = 0;

  for (auto p1 : ss) {
    for (auto p2 : ss) {
      ans = max(ans, abs(p1.first-p2.first) + abs(p1.second-p2.second));
    }
  }

  cout << ans << endl;

  return 0;
}

