#include <bits/stdc++.h>
using namespace std;

const double pi  = 2 * acos(0.0);
const double eps = 1e-8;

#define REP(i,a,b) for(int i=(a); i<(b);++i)
#define rep(i,n) REP(i,0,n)
#define INF (1<<29)
#define INFLL (1LL<<62)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int dx[8] = {0, 1, 0, -1, 1, -1, 1, -1};
int dy[8] = {1, 0, -1, 0, 1, -1, -1, 1};

int main(void) {
  ios_base::sync_with_stdio(false); cin.tie(0);
  int N; cin >> N;
  string s, S;
  set<string> substrs;

  rep(i, N) {
    cin >> s;
    S += "|" + s;
  }

  REP(i, 1, 5) {
    for (int j = 0; j < S.size(); j++) {
      string s = S.substr(j, i);
      if (s.find("|") != string::npos)
        continue;
      substrs.insert(s);
    }
  }

  string t;
  rep(i, 27) rep(j, 27) rep(k, 27) rep(l, 26) {
    t = "";
    if (i) t += 'a' + i - 1;
    if (j) t += 'a' + j - 1;
    if (k) t += 'a' + k - 1;
    t += 'a' + l;
    if (!substrs.count(t)) {
      cout << t << endl;
      return 0;
    }
  }
  return 0; 
}