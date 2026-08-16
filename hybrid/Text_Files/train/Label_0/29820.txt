#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <map>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

int n;
ll encode(int box[2][8]) {
  ll ret = 0;
  REP(lr, 2) {
    REP(index, n) {
      ret |= (ll)box[lr][index] << (3 * (lr * 8 + index));
    }
  }
  return ret;
}
void decode(int box[2][8], ll value) {
  REP(lr, 2) {
    REP(index, n) {
      box[lr][index] = (value >> (3 * (lr * 8 + index))) & 7;
    }
  }
}
int huristic1(int box[2][8]) {
  int ret = 0;
  REP(lr, 2) {
    REP(index, n) {
      ret += abs(box[lr][index] - index);
    }
  }
  return ret;
}
inline int h2check(int l, int r) {
  if (l > r) { return 2; }
  else if (l == r) { return 1; }
  return 0;
}
int huristic2(int box[2][8]) {
  int ret = 5;
  REP(to, n) {
    if (box[0][to] != box[1][to]) { ret++; }
    REP(from, to) {
      REP(fromlr, 2) {
        REP(tolr, 2) {
          ret += h2check(box[fromlr][from], box[tolr][to]);
        }
      }
    }
  }
  return ret;
}
int huristic2part(int box[2][8], int ph2, int f, int t, int flr, int tlr) {
  int ret = ph2;
  if (box[0][f] != box[1][f]) { ret--; }
  if (box[0][t] != box[1][t]) { ret--; }
  ret -= h2check(box[flr][f], box[tlr][t]);
  ret -= h2check(box[flr][f], box[1 ^ tlr][t]);
  ret -= h2check(box[1 ^ flr][f], box[tlr][t]);

  swap(box[flr][f], box[tlr][t]);
  if (box[0][f] != box[1][f]) { ret++; }
  if (box[0][t] != box[1][t]) { ret++; }
  ret += h2check(box[flr][f], box[tlr][t]);
  ret += h2check(box[flr][f], box[1 ^ tlr][t]);
  ret += h2check(box[1 ^ flr][f], box[tlr][t]);
  swap(box[flr][f], box[tlr][t]);
  assert(abs(ret - ph2) <= 6);
  return ret;
}

struct State {
  ll state;
  int cost;
  int hcost;
  int ph2cost;
  State() {;}
  State(ll s, int c, int hc, int ph2) : state(s), cost(c), hcost(hc), ph2cost(ph2) {;}
  bool operator<(const State &rhs) const {
    return cost + hcost > rhs.cost + rhs.hcost;
  }
};
void printBox(int box[2][8]) {
  REP(lr, 2) {
    REP(index, n) {
      printf("%d ", box[lr][index]);
    }
    puts("");
  }
}

const int dy[2] = { 1, -1 };
int box[2][8];

int main() {
  while (scanf("%d", &n) > 0 && n) {
    MEMSET(box, 0);
    REP(i, n) {
      box[0][i] = box[1][i] = i;
    }
    ll endState = encode(box);
    REP(index, n) {
      REP(lr,2) {
        int x;
        scanf("%d", &x);
        x--;
        box[lr][index] = x;
      }
    }
    REP(i, n) {
      if (box[0][i] > box[1][i]) { swap(box[0][i], box[1][i]); }
    }
    set<ll> visit;
    priority_queue<State> que;
    que.push(State(encode(box), 0, 0, huristic2(box)));
    while (!que.empty()) {
      State s = que.top();
      que.pop();
      if (visit.count(s.state)) { continue; }
      visit.insert(s.state);
      if (s.state == endState) {
        printf("%d\n", s.cost);
        break;
      }
      decode(box, s.state);
      REP(from, n - 1) {
        if (box[0][0] == 0 && box[1][0] == 0 && from == 0) { continue; }
        if (box[0][0] == 0 && box[1][0] == 0 && box[0][1] == 1 && box[1][1] == 1 && from == 1) { continue; }
        if (box[0][n - 1] == n - 1 && box[1][n - 1] == n - 1 && from == n - 2) { continue; }
        if (n >= 3 && box[0][n - 1] == n - 1 && box[1][n - 1] == n - 1 && box[0][n - 2] == n - 2 && box[1][n - 2] == n - 2 && from == n - 3) { continue; }
        int to = from + 1;
        REP(fromlr, 2) {
          if (box[0][from] == box[1][from] && fromlr == 1) { continue; }
          REP(tolr, 2) {
            if (box[0][to] == box[1][to] && tolr == 1) { continue; }
            if (box[fromlr][from] == box[tolr][to]) { continue; }
            int h2 = huristic2part(box, s.ph2cost, from, to, fromlr, tolr);
            bool upswap = false;
            bool lowerswap = false;
            swap(box[fromlr][from], box[tolr][to]);
            if (box[0][from] > box[1][from]) {
              swap(box[0][from], box[1][from]);
              upswap = true;
            }
            if (box[0][to] > box[1][to]) {
              swap(box[0][to], box[1][to]);
              lowerswap = true;
            }
            ll enc = encode(box);
            int h1 = huristic1(box);
            //int h2 = huristic2(box);
            que.push(State(enc, s.cost + 1, max(h1 / 2, h2 / 6), h2));
            if (upswap) { swap(box[0][from], box[1][from]); }
            if (lowerswap) { swap(box[0][to], box[1][to]); }
            swap(box[fromlr][from], box[tolr][to]);
          }
        }
      }
    }
   //cout << visit.size() << endl;
  }
}