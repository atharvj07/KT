#include <bits/stdc++.h>
constexpr int inf = 1e9;
struct SegmentTree {
  int n;
  std::vector<int> t;
  SegmentTree(int n) : n(n), t(2 * n) {}
  void modify(int p, int val) {
    for (t[p += n] = val; p > 1; p >>= 1) {
      t[p >> 1] = std::min(t[p], t[p ^ 1]);
    }
  }
  int rangeMin(int l, int r) {
    int res = inf;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
      if (l % 2 == 1) {
        res = std::min(res, t[l++]);
      }
      if (r % 2 == 1) {
        res = std::min(res, t[--r]);
      }
    }
    return res;
  }
};
struct LazySegmentTree {
  int n;
  std::vector<int> info, tag;
  LazySegmentTree(int n) : n(n), info(4 * n), tag(4 * n) {}
  void push(int len, int p) {
    if (tag[p] == 0) {
      return;
    }
    if (len > 1) {
      tag[2 * p] = tag[2 * p + 1] = tag[p];
    }
    info[p] = tag[p];
    tag[p] = 0;
  }
  void modify(int p, int l, int r, int pos, int v) {
    if (l == r - 1) {
      info[p] = v;
      return;
    }
    int m = (l + r) / 2;
    if (pos < m) {
      modify(2 * p, l, m, pos, v);
    } else {
      modify(2 * p + 1, m, r, pos, v);
    }
    info[p] = std::min(info[2 * p], info[2 * p + 1]);
  }
  void modify(int p, int val) { modify(1, 0, n, p, val); }
  void rangeApply(int p, int l, int r, int x, int y, int v) {
    push(r - l, p);
    if (l >= y || r <= x) {
      return;
    }
    if (l >= x && r <= y) {
      tag[p] = v;
      push(r - l, p);
      return;
    }
    int m = (l + r) / 2;
    rangeApply(2 * p, l, m, x, y, v);
    rangeApply(2 * p + 1, m, r, x, y, v);
    info[p] = std::min(info[2 * p], info[2 * p + 1]);
  }
  void rangeApply(int x, int y, int v) { rangeApply(1, 0, n, x, y, v); }
  int rangeQuery(int p, int l, int r, int x, int y) {
    push(r - l, p);
    if (l >= y || r <= x) {
      return inf;
    }
    if (l >= x && r <= y) {
      return info[p];
    }
    int m = (l + r) / 2;
    return std::min(rangeQuery(2 * p, l, m, x, y),
                    rangeQuery(2 * p + 1, m, r, x, y));
  }
  int rangeQuery(int x, int y) { return rangeQuery(1, 0, n, x, y); }
};
int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int n, k;
  std::cin >> n >> k;
  std::vector<int> b(n);
  SegmentTree mn(n);
  for (int i = 0; i < n; i++) {
    std::cin >> b[i];
    mn.modify(i, b[i]);
  }
  auto get = [&](int l, int r) {
    int tl = l / n + (l % n > 0);
    int tr = r / n - (r % n > 0);
    if (tl < tr) {
      return mn.rangeMin(0, n);
    }
    l %= n;
    r %= n;
    if (l < r) {
      return mn.rangeMin(l, r);
    } else {
      return std::min(mn.rangeMin(0, r), mn.rangeMin(l, n));
    }
  };
  int q;
  std::cin >> q;
  std::vector<std::tuple<int, int, int, int>> queries(q);
  std::vector<int> f;
  for (auto &[typ, l, r, x] : queries) {
    std::cin >> typ >> l >> r;
    if (typ == 1) {
      std::cin >> x;
    }
    l--;
    f.push_back(l);
    f.push_back(r);
  }
  std::sort(f.begin(), f.end());
  f.erase(std::unique(f.begin(), f.end()), f.end());
  int m = f.size();
  f.push_back(n * k);
  LazySegmentTree s(m);
  for (int i = 0; i < m; i++) {
    s.modify(i, get(f[i], f[i + 1]));
  }
  for (auto [typ, l, r, x] : queries) {
    l = std::lower_bound(f.begin(), f.end(), l) - f.begin();
    r = std::lower_bound(f.begin(), f.end(), r) - f.begin();
    if (typ == 1) {
      s.rangeApply(l, r, x);
    } else {
      std::cout << s.rangeQuery(l, r) << "\n";
    }
  }
  return 0;
}
