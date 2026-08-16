#include <bits/stdc++.h>
int gcd(int a, int b) {
  if (a < b) std::swap(a, b);
  while (0 < b) {
    a %= b;
    std::swap(a, b);
  }
  return a;
}
int main() {
  int n, k;
  int g[250000];
  std::vector<int> r;
  std::priority_queue<int> q;
  std::scanf("%d", &n);
  for (int i(0); i < n * n; ++i) std::scanf("%d", g + i);
  std::stable_sort(g, g + n * n, std::greater<int>());
  for (int i(0); i < n * n; ++i) {
    if (!q.empty() && g[i] == q.top()) {
      q.pop();
      continue;
    }
    for (int v : r) {
      k = gcd(g[i], v);
      q.push(k);
      q.push(k);
    }
    r.push_back(g[i]);
  }
  for (int i(0); i < r.size(); ++i) {
    if (0 < i) std::printf(" ");
    std::printf("%d", r[i]);
  }
  std::puts("");
  return 0;
}
