#include <bits/stdc++.h>
using namespace std;
unordered_map<long long, long long> cost;
void update(long long u, long long v, long long w) {
  if (u > v) {
    cost[u] += w;
    update(u / 2, v, w);
  } else if (v > u) {
    cost[v] += w;
    update(u, v / 2, w);
  } else
    return;
}
long long get(long long u, long long v) {
  if (u == v) return 0;
  if (u > v) {
    if (cost.find(u) != cost.end())
      return cost[u] + get(u / 2, v);
    else
      return get(u / 2, v);
  } else {
    if (cost.find(v) != cost.end())
      return cost[v] + get(u, v / 2);
    else
      return get(u, v / 2);
  }
}
int main() {
  ios::sync_with_stdio(false);
  int q;
  scanf("%d", &q);
  while (q--) {
    int type;
    scanf("%d", &type);
    if (type == 1) {
      long long u, v, w;
      scanf("%lld %lld %lld", &u, &v, &w);
      update(u, v, w);
    } else {
      long long u, v;
      scanf("%lld %lld", &u, &v);
      printf("%lld\n", get(u, v));
    }
  }
  return 0;
}
