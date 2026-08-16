#include <bits/stdc++.h>
int read() {
  int ans = 0, c, f = 1;
  while (!isdigit(c = getchar()))
    if (c == '-') f *= -1;
  do ans = ans * 10 + c - '0';
  while (isdigit(c = getchar()));
  return ans * f;
}
const int N = 10050;
const int K = 5;
inline int query(int l, int r, int t) {
  return (r + K - t) / K - (l - 1 + K - t) / K;
}
std::pair<int, int> Q[N];
int main() {
  int n = read(), b = read(), q = read();
  for (int i = 0; i < q; ++i) {
    Q[i].first = read();
    Q[i].second = read();
  }
  Q[q++] = std::make_pair(0, 0);
  Q[q++] = std::make_pair(b, n);
  std::sort(Q, Q + q);
  for (int i = 1; i < q; ++i)
    if (Q[i].second < Q[i - 1].second ||
        Q[i].second - Q[i - 1].second > Q[i].first - Q[i - 1].first) {
      puts("unfair");
      return 0;
    }
  for (int S = 1; S < (1 << K); ++S) {
    int t = n;
    for (int i = 1; i < q; ++i) {
      int l = Q[i - 1].first + 1, r = Q[i].first,
          s = Q[i].second - Q[i - 1].second;
      int b = 0;
      for (int j = 0; j < K; ++j)
        if ((S >> j) & 1) b += query(l, r, j);
      if (b - s < 0) t += b - s;
    }
    int sx = 0;
    for (int j = 0; j < K; ++j)
      if ((S >> j) & 1) ++sx;
    sx *= n / 5;
    if (sx > t) {
      puts("unfair");
      return 0;
    }
  }
  puts("fair");
  return 0;
}
