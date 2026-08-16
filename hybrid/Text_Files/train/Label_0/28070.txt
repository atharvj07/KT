/*
 * g.cc: 
 */

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<queue>
#include<deque>
#include<algorithm>
#include<numeric>
#include<utility>
#include<complex>
#include<functional>

using namespace std;

/* constant */

const int MAX_N = 100000;
const int MAX_D = 20;

typedef long long ll;

const int INF = 1 << 30;
const ll LINF = 1LL << 60;

/* typedef */

typedef pair<int,int> pii;
typedef vector<pii> vpii;

struct Stat {
  ll c;
  int d, i;
  Stat() {}
  Stat(ll _c, int _d, int _i): c(_c), d(_d), i(_i) {}
  bool operator<(const Stat &s) const {
    return c > s.c || (c == s.c && d > s.d);
  }
};

/* global variables */

int ts[MAX_N];
vpii nbrs[MAX_N];
ll costs[MAX_N];
int dists[MAX_N], prts[MAX_N][MAX_D];

/* subroutines */

/* main */

int main() {
  int n, m;
  int tmp = scanf("%d%d", &n, &m);

  for (int i = 0; i < n; i++) tmp = scanf("%d", &ts[i]);

  for (int i = 0; i < m; i++) {
    int ai, bi, ci;
    tmp = scanf("%d%d%d", &ai, &bi, &ci);
    ai--, bi--;
    nbrs[ai].push_back(pii(bi, ci));
    nbrs[bi].push_back(pii(ai, ci));
  }

  for (int i = 0; i < n; i++) costs[i] = LINF;
  costs[0] = 0;
  dists[0] = 0;
  prts[0][0] = -1;

  priority_queue<Stat> q;
  q.push(Stat(0, 0, 0));

  while (! q.empty()) {
    Stat u = q.top(); q.pop();
    if (costs[u.i] != u.c || dists[u.i] != u.d) continue;

    int vd = u.d + 1;
    vpii &nbru = nbrs[u.i];

    for (vpii::iterator vit = nbru.begin(); vit != nbru.end(); vit++) {
      int &vi = vit->first;
      ll vc = u.c + vit->second;

      if (costs[vi] > vc) {
	costs[vi] = vc;
	dists[vi] = vd;
	prts[vi][0] = u.i;
	q.push(Stat(vc, vd, vi));
      }
      else if (costs[vi] == vc) {
	if (dists[vi] > vd) {
	  dists[vi] = vd;
	  prts[vi][0] = u.i;
	  q.push(Stat(vc, vd, vi));
	}
	else if (dists[vi] == vd && ts[prts[vi][0]] > ts[u.i]) {
	  prts[vi][0] = u.i;
	}
      }
    }
  }

  for (int d = 1; d < MAX_D; d++)
    for (int i = 0; i < n; i++) {
      int j = prts[i][d - 1];
      prts[i][d] = (j < 0) ? -1 : prts[j][d - 1];
    }

  int k;
  tmp = scanf("%d", &k);

  while (k--) {
    int xi, di, pi;
    tmp = scanf("%d%d%d", &xi, &di, &pi);
    xi--;

    int r = dists[xi] - di;
    int yi = xi;
    //printf("xi=%d,di=%d,pi=%d: costs=%lld,dists=%d,r=%d\n",
    //xi, di, pi, costs[xi], dists[xi], r);

    if (r > 0)
      for (int d = MAX_D - 1; d >= 0; d--)
	if (r & (1 << d)) yi = prts[yi][d];
    //printf("  yi=%d\n", yi);
    
    ll cost = costs[xi] - costs[yi];
    if (cost < costs[xi] - pi) cost = costs[xi] - pi;

    printf("%lld\n", cost);
  }
}
