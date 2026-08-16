#include <bits/stdc++.h>
int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  size_t n;
  std::cin >> n;
  std::vector<std::vector<std::tuple<size_t, size_t>>> gr(n);
  std::vector<std::tuple<size_t, size_t>> vertices;
  for (size_t i = 1; i < n; ++i) {
    size_t u, v;
    std::cin >> u >> v;
    u -= 1;
    v -= 1;
    gr[u].emplace_back(v, i);
    gr[v].emplace_back(u, i);
    vertices.emplace_back(u, v);
  }
  std::vector<std::tuple<size_t, size_t>> edges;
  for (size_t u = 0; u < n; ++u) {
    for (size_t i = 0; i < gr[u].size(); ++i) {
      if (i > 0) {
        edges.emplace_back(std::get<1>(gr[u][i - 1]), std::get<1>(gr[u][i]));
      }
    }
  }
  std::cout << vertices.size() << '\n';
  for (const auto [a, b] : vertices) {
    std::cout << "2 " << a + 1 << ' ' << b + 1 << '\n';
  }
  for (const auto [a, b] : edges) {
    std::cout << a << ' ' << b << '\n';
  }
}
