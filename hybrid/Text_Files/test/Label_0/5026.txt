#include <bits/stdc++.h>
using namespace std;
template <class T, class S>
ostream& operator<<(ostream& os, const pair<T, S>& v) {
  return os << "(" << v.first << ", " << v.second << ")";
}
template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
  os << "[";
  for (int i = int(0); i <= int((static_cast<int>((v).size())) - 1); ++i) {
    if (i) os << ", ";
    os << v[i];
  }
  return os << "]";
}
template <class T>
bool setmax(T& _a, T _b) {
  if (_a < _b) {
    _a = _b;
    return true;
  }
  return false;
}
template <class T>
bool setmin(T& _a, T _b) {
  if (_b < _a) {
    _a = _b;
    return true;
  }
  return false;
}
template <class T>
T gcd(T _a, T _b) {
  return _b == 0 ? _a : gcd(_b, _a % _b);
}
vector<int> read_vi(int n = -1) {
  if (n < 0) scanf("%d", &n);
  vector<int> a(n);
  for (int i = int(0); i <= int((n)-1); ++i) scanf("%d", &a[i]);
  return a;
}
vector<long long> read_vl(int n = -1) {
  if (n < 0) scanf("%d", &n);
  vector<long long> a(n);
  for (int i = int(0); i <= int((n)-1); ++i) scanf("%lld", &a[i]);
  return a;
}
vector<double> read_vd(int n = -1) {
  if (n < 0) scanf("%d", &n);
  vector<double> a(n);
  for (int i = int(0); i <= int((n)-1); ++i) scanf("%lf", &a[i]);
  return a;
}
vector<pair<int, int>> read_vpi(int n = -1) {
  if (n < 0) scanf("%d", &n);
  vector<pair<int, int>> a(n);
  for (int i = int(0); i <= int((n)-1); ++i)
    scanf("%d%d", &a[i].first, &a[i].second);
  return a;
}
vector<pair<long long, long long>> read_vpl(int n = -1) {
  if (n < 0) scanf("%d", &n);
  vector<pair<long long, long long>> a(n);
  for (int i = int(0); i <= int((n)-1); ++i)
    scanf("%lld%lld", &a[i].first, &a[i].second);
  return a;
}
vector<pair<double, double>> read_vpd(int n = -1) {
  if (n < 0) scanf("%d", &n);
  vector<pair<double, double>> a(n);
  for (int i = int(0); i <= int((n)-1); ++i)
    scanf("%lf%lf", &a[i].first, &a[i].second);
  return a;
}
inline long long powmod(long long a, long long b, long long m) {
  long long r = 1;
  for (; b > 0; b >>= 1, a = a * a % m) {
    if (b & 1) r = r * a % m;
  }
  return r;
}
template <class T>
class Net {
 public:
  explicit Net(int n0)
      : n(n0 + 4),
        original_s(n0),
        original_t(n0 + 1),
        super_s(n0 + 2),
        super_t(n0 + 3),
        es(n),
        dis(n) {}
  int s() const { return original_s; }
  int t() const { return original_t; }
  void* add(int x, int y, T w) {
    assert(x >= 0 && x < n && y >= 0 && y < n);
    Edge *e1, *e2;
    es[x].emplace_back(e1 = new Edge{y, w, nullptr});
    es[y].emplace_back(e2 = new Edge{x, 0, nullptr});
    e1->oppo = e2, e2->oppo = e1;
    return e1;
  }
  void* add(int x, int y, pair<T, T> w) {
    assert(w.first <= w.second);
    if (w.first > 0) {
      add(super_s, y, w.first);
      add(x, super_t, w.first);
      super_total += w.first;
    }
    return add(x, y, w.second - w.first);
  }
  T compute() {
    if (super_total > 0) {
      add(original_t, original_s, numeric_limits<T>::max());
      long long r = 0, tmp;
      while ((tmp = augment(super_s, super_t)) > 0) {
        r += tmp;
      }
      if (r != super_total) return -1;
    }
    T ans = 0, tmp;
    while ((tmp = augment(original_s, original_t)) > 0) {
      ans += tmp;
    }
    return ans;
  }
  T flow(void* e) const { return static_cast<Edge*>(e)->oppo->w; }
  bool on_cut(void* e) const {
    return dis[static_cast<Edge*>(e)->oppo->y] > 0 &&
           dis[static_cast<Edge*>(e)->y] == 0;
  }
  vector<int> left() const {
    vector<int> r;
    for (int i = int(0); i <= int((n - 4) - 1); ++i)
      if (dis[i] > 0) r.push_back(i);
    return r;
  }

 private:
  struct Edge {
    int y;
    T w;
    Edge* oppo;
  };
  T augment(int s, int t) {
    dis.resize(n);
    fill((dis).begin(), (dis).end(), 0);
    dis[s] = 1;
    queue<int> que;
    que.push(s);
    while (!que.empty()) {
      int x = que.front();
      que.pop();
      for (const auto& e : es[x]) {
        if (e->w > 0 && dis[e->y] == 0) {
          dis[e->y] = dis[x] + 1;
          que.push(e->y);
        }
      }
    }
    if (dis[t] == 0) return 0;
    vector<size_t> ce(n);
    const function<T(int, T)> dfs = [&](int x, T rest) {
      if (x == t) return rest;
      T r = 0;
      for (size_t& i = ce[x]; i < es[x].size(); ++i) {
        const auto& e = es[x][i];
        if (e->w > 0 && dis[e->y] > dis[x]) {
          T cur = dfs(e->y, min(e->w, rest));
          e->w -= cur, e->oppo->w += cur;
          r += cur, rest -= cur;
          if (rest == 0) break;
        }
      }
      return r;
    };
    return dfs(s, numeric_limits<T>::max());
  }
  const int n, original_s, original_t, super_s, super_t;
  T super_total = 0;
  vector<vector<unique_ptr<Edge>>> es;
  vector<int> dis;
};
class IntervalTree {
 public:
  IntervalTree(int n) : n(n), tr(n * 4) {}
  void add(int l, int r, int val) { add(0, 0, n, l, r, val); }
  vector<pair<int, pair<int, int>>> intervals() const {
    vector<pair<int, pair<int, int>>> ans;
    const function<void(int, int, int)> dfs = [&](int x, int l, int r) {
      if (l + 1 == r) {
        ans.push_back({x, {l, -1}});
        return;
      } else {
        ans.push_back({x, {x * 2 + 1, x * 2 + 2}});
      }
      const int m = (l + r) / 2;
      dfs(x * 2 + 1, l, m);
      dfs(x * 2 + 2, m, r);
    };
    dfs(0, 0, n);
    return ans;
  }
  vector<int> extract_gt0() {
    vector<int> ans;
    extract(0, 0, n, &ans);
    return ans;
  }

 private:
  struct Node {
    int minv = 0, maxv = 0, buf = 0;
  };
  void push(int x, int val) {
    tr[x].minv += val;
    tr[x].maxv += val;
    tr[x].buf += val;
  }
  void update(int x) {
    tr[x].minv = min(tr[x * 2 + 1].minv, tr[x * 2 + 2].minv);
    tr[x].maxv = max(tr[x * 2 + 1].maxv, tr[x * 2 + 2].maxv);
  }
  void release(int x) {
    if (tr[x].buf) {
      push(x * 2 + 1, tr[x].buf);
      push(x * 2 + 2, tr[x].buf);
      tr[x].buf = 0;
    }
  }
  void add(int x, int l, int r, int st, int en, int val) {
    if (st <= l && r <= en) {
      push(x, val);
      return;
    }
    release(x);
    const int m = (l + r) / 2;
    if (st < m) add(x * 2 + 1, l, m, st, en, val);
    if (m < en) add(x * 2 + 2, m, r, st, en, val);
    update(x);
  }
  void extract(int x, int l, int r, vector<int>* ans) {
    if (tr[x].minv > 0) {
      return;
    }
    if (tr[x].maxv == 0) {
      ans->push_back(x);
      return;
    }
    release(x);
    const int m = (l + r) / 2;
    extract(x * 2 + 1, l, m, ans);
    extract(x * 2 + 2, m, r, ans);
  }
  const int n;
  vector<Node> tr;
};
int main() {
  int n, q;
  scanf("%d%d", &n, &q);
  vector<vector<pair<int, pair<int, int>>>> events(n + 1);
  for (int i = int(0); i <= int((q)-1); ++i) {
    int x1, y1, x2, y2;
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    --x1, --y1;
    events[x1].push_back({+1, {y1, y2}});
    events[x2].push_back({-1, {y1, y2}});
  }
  const int kInf = 1 << 30;
  IntervalTree tr(n);
  Net<int> net(7 * n);
  for (int x = int(0); x <= int((n)-1); ++x) net.add(net.s(), x, 1);
  for (int y = int(0); y <= int((n)-1); ++y) net.add(n + y, net.t(), 1);
  for (const auto& p : tr.intervals()) {
    int t = p.first, u = p.second.first, v = p.second.second;
    if (v < 0) {
      net.add(2 * n + t, n + u, kInf);
    } else {
      net.add(2 * n + t, 2 * n + u, kInf);
      net.add(2 * n + t, 2 * n + v, kInf);
    }
  }
  int cur = n * 6, last = 0;
  const auto add = [&](int x1, int x2, const vector<int>& ids) {
    int p = cur++;
    for (int x = int(x1); x <= int((x2)-1); ++x) net.add(x, p, kInf);
    for (int i : ids) net.add(p, 2 * n + i, kInf);
  };
  for (int x = int(0); x <= int(n); ++x) {
    if (x > 0 && (x == n || !events[x].empty())) {
      add(last, x, tr.extract_gt0());
      last = x;
    }
    for (const auto& e : events[x]) {
      tr.add(e.second.first, e.second.second, e.first);
    }
  }
  int ans = net.compute();
  printf("%d\n", ans);
  return 0;
}
