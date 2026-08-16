#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>

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


inline unsigned int next_subset(unsigned int S, unsigned int U) {
  return (S - U) & U;
}
int n, m, w;
int pos[16];
int weight[16];
int memo[1 << 16];

int sum[1 << 16];
int upper[1 << 16];
int lower[1 << 16];

int calc(int s, int f, int t, int rest) {
  if (rest == 0) { return 0; }
  if (memo[rest] != -1) { return memo[rest]; }
  int ret = 1 << 30;
  for (int use = rest & -rest; use; use = next_subset(use, rest)) {
    if (sum[use] > w) { continue; }
    int nrest = rest ^ use;
    int cost = abs(s - f) + abs(f - t);
    ret = min(ret, calc(t, f, t, nrest) + cost);
  }
  return memo[rest] = ret;
}

int main() {
  while (scanf("%d %d %d", &n, &m, &w) > 0) {
    m--;
    int cnt = 0;
    vector<int> fs;
    fs.push_back(0);
    REP(i, n) {
      int k;
      scanf("%d", &k);
      if (i != 0 && k > 0) {
        fs.push_back(i);
      }
      REP(j, k) {
        if (i == 0) { scanf("%*d"); continue; }
        pos[cnt] = i;
        scanf("%d", &weight[cnt++]);
      }
    }
    reverse(fs.begin(), fs.end());
    MEMSET(sum, 0);
    MEMSET(upper, 0);
    MEMSET(lower, 0x0f);
    n = cnt;
    REP(i, 1 << n) {
      REP(j, n) {
        if (i & (1 << j)) {
          sum[i] += weight[j];
          upper[i] = max(upper[i], pos[j]);
          lower[i] = min(lower[i], pos[j]);
        }
      }
    }
    int ans = 0;
    int prev = m;
    REP(i, fs.size() - 1) {
      MEMSET(memo, -1);
      int target = 0;
      REP(j, n) {
        if (pos[j] >= fs[i]) { target |= 1 << j; }
      }
      ans += calc(prev, fs[i], fs[i + 1], target);
      prev = fs[i + 1];
    }
    cout << ans << endl;
  }
}