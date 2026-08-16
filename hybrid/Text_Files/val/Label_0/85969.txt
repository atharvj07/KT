#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <utility>
#include <queue>
using namespace std;
using int64 = long long int;
const int64 INF = 1LL << 60;

int N, M, C;
vector< pair<int64, int64> > G[100010];
int64 dist[100010];

struct Elem {
  int64 cur, cost;
  Elem() {}
  Elem(int64 a, int64 b) : cur(a), cost(b) {}
  bool operator<(const Elem &e) const {
    return cost > e.cost;
  }
};

int main() {
  cin >> N >> M >> C;
  int64 cost_sum = 0;
  for(int i=0; i<M; i++) {
    int64 a, b, d; cin >> a >> b >> d;
    a--; b--;
    G[a].emplace_back(b, d);
    G[b].emplace_back(a, d);
    cost_sum += d;
  }

  
  priority_queue<Elem> que;
  fill(dist, dist + N, INF);
  dist[0] = 0;
  que.emplace(0, 0);
  while(que.size()) {
    auto e = que.top(); que.pop();
    if(dist[e.cur] < e.cost) continue;
    for(auto edge : G[e.cur]) {
      int64 to, mon; tie(to, mon) = edge;
      if(dist[to] > e.cost + mon) {
        dist[to] = e.cost + mon;
        que.emplace(to, dist[to]);
      }
    }
  }

  vector< pair<int64, int64> > info;
  for(int i=0; i<N; i++) {
    for(auto edge : G[i]) {
      int to, cost; tie(to, cost) = edge;
      int u = i, v = to;
      if(u > v) continue;

      int64 max_dist = max(dist[u], dist[v]);
      info.emplace_back(max_dist, cost);
    }
  }
  sort(info.begin(), info.end());

  int64 ans = cost_sum;
  for(size_t i=0; i<info.size(); i++) {
    int64 a, b; tie(a, b) = info[i];
    cost_sum -= b;
    int64 sum = a * C + cost_sum;
    // fprintf(stderr, "sum: %lld\n", sum);
    ans = min(ans, sum);
  }
  cout << ans << endl;

  /*  
  vector<int64> cand;
  for(int i=0; i<N; i++) {
    // fprintf(stderr, "dist[%d] = %lld\n", i, dist[i]);
    cand.push_back(dist[i]);
  }
  sort(cand.begin(), cand.end());
  cand.erase(unique(cand.begin(), cand.end()), cand.end());
  int L = cand.size();

  auto calc = [&](int idx) {
                int64 X = cand[idx];
                int64 sum = C * X;

                for(int i=0; i<N; i++) {
                  for(auto edge : G[i]) {
                    int64 to, cost; tie(to, cost) = edge;
                    int64 u = i, v = to;
                    if(u > v) continue;
                    if(!(dist[u] <= X and dist[v] <= X)) {
                      sum += cost;
                    }
                  }
                }

                return sum;
              };

  int ub = L-1, lb = -1;
  while(ub - lb > 1) {
    int mid = (ub + lb) / 2;
    int64 vl = calc(mid), vr = calc(mid + 1);
    if(vl < vr) ub = mid;
    else lb = mid;
  }
  cout << calc(ub) << endl;
  */
  return 0;
}

