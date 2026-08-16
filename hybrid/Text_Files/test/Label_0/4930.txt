#include <bits/stdc++.h>
constexpr int MAX_M = 1e5 + 5;
using i64 = std::int64_t;
using state = std::pair<i64, int>;
struct Point {
  Point() {}
  Point(int _x, int _y, int _id) : x(_x), y(_y), id(_id) {}
  int x, y, id;
};
struct Edge {
  Edge(int _from, int _to, int _w) : from(_from), to(_to), w(_w) {}
  int from, to, w;
};
int n, m;
std::vector<Edge> g[MAX_M];
Point pts[MAX_M];
int manhattan(int i, int j) {
  return std::abs(pts[i].x - pts[j].x) + std::abs(pts[i].y - pts[j].y);
}
int cost(int i, int j) {
  return std::min(std::abs(pts[i].x - pts[j].x), std::abs(pts[i].y - pts[j].y));
}
std::vector<i64> dijkstra(int s, int t) {
  std::vector<i64> dist(m + 2, -1);
  std::priority_queue<state, std::vector<state>, std::greater<state>> pq;
  dist[s] = 0;
  pq.emplace(0, s);
  while (!pq.empty()) {
    i64 d;
    int cur;
    std::tie(d, cur) = pq.top();
    pq.pop();
    for (const auto &ed : g[cur]) {
      if (dist[ed.to] == -1 || d + ed.w < dist[ed.to]) {
        dist[ed.to] = d + ed.w;
        pq.emplace(dist[ed.to], ed.to);
      }
    }
  }
  return dist;
}
int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cin >> n >> m;
  std::cin >> pts[0].x >> pts[0].y;
  pts[0].id = 0;
  std::cin >> pts[1].x >> pts[1].y;
  pts[1].id = 1;
  for (int i = 0; i < m; i++) {
    std::cin >> pts[2 + i].x >> pts[2 + i].y;
    pts[2 + i].id = 2 + i;
  }
  g[0].emplace_back(0, 1, manhattan(0, 1));
  for (int i = 2; i < 2 + m; i++) {
    g[0].emplace_back(0, i, cost(0, i));
    g[i].emplace_back(i, 1, manhattan(i, 1));
  }
  std::sort(pts + 2, pts + 2 + m,
            [&](const Point &a, const Point &b) { return a.x < b.x; });
  for (int i = 2; i < m + 2; i++) {
    if (i > 2) {
      g[pts[i].id].emplace_back(pts[i].id, pts[i - 1].id, cost(i, i - 1));
    }
    if (i + 1 < m + 2) {
      g[pts[i].id].emplace_back(pts[i].id, pts[i + 1].id, cost(i, i + 1));
    }
  }
  std::sort(pts + 2, pts + 2 + m,
            [&](const Point &a, const Point &b) { return a.y < b.y; });
  for (int i = 2; i < m + 2; i++) {
    if (i > 2) {
      g[pts[i].id].emplace_back(pts[i].id, pts[i - 1].id, cost(i, i - 1));
    }
    if (i + 1 < m + 2) {
      g[pts[i].id].emplace_back(pts[i].id, pts[i + 1].id, cost(i, i + 1));
    }
  }
  std::sort(pts + 2, pts + 2 + m,
            [&](const Point &a, const Point &b) { return a.id < b.id; });
  std::cout << dijkstra(0, 1)[1] << "\n";
  return 0;
}
