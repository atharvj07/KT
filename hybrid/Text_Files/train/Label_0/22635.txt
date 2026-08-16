#include <bits/stdc++.h>
struct M {
  int p, b;
};
struct F {
  const int p, i;
  int r, c;
  F(int p, int t, int i) : p(p), i(i), r(p + t), c(0) {}
  int t() { return r - p; }
};
void solve(std::vector<F> &fs, std::vector<M> &ms) {
  std::multimap<int, int> ms_landed;
  std::map<int, F *> fs_active;
  {
    std::vector<F *> fs_sort;
    fs_sort.reserve(fs.size());
    for (int i = 0; i < fs.size(); i++) fs_sort.push_back(&fs[i]);
    std::sort(fs_sort.begin(), fs_sort.end(),
              [](const F *lhs, const F *rhs) { return lhs->p < rhs->p; });
    fs_active.insert({fs_sort[0]->p, fs_sort[0]});
    int curr = fs_sort[0]->r;
    for (int i = 1; i < fs_sort.size(); i++) {
      F &f = *fs_sort[i];
      if (f.r > curr) {
        int l = std::max(curr + 1, f.p);
        curr = f.r;
        fs_active.insert({l, &f});
      }
    }
  }
  auto update = [&](F &f, std::map<int, F *>::iterator &f_succ, const int &b) {
    f.c++;
    f.r += b;
    while (f_succ != fs_active.end()) {
      int l_succ = f_succ->first;
      int r_succ = f_succ->second->r;
      if (f.r < r_succ) {
        if (f.r >= l_succ) {
          fs_active.erase(f_succ);
          f_succ = fs_active.insert({f.r + 1, f_succ->second}).first;
        }
        break;
      }
      f_succ = fs_active.erase(f_succ);
    }
  };
  for (const M &m : ms) {
    auto f_it = --fs_active.upper_bound(m.p);
    const int l = f_it->first;
    F &f = *f_it->second;
    if (l <= m.p && m.p <= f.r) {
      update(f, ++f_it, m.b);
      auto m_it = ms_landed.lower_bound(l);
      while (m_it != ms_landed.end()) {
        M m{m_it->first, m_it->second};
        if (l <= m.p && m.p <= f.r) {
          update(f, f_it, m.b);
          m_it = ms_landed.erase(m_it);
        } else {
          break;
        }
      }
    } else {
      ms_landed.insert({m.p, m.b});
    }
  }
  for (F &f : fs) {
    printf("%d %d\n", f.c, f.t());
  }
}
int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  std::vector<F> fs;
  fs.reserve(n);
  std::vector<M> ms;
  ms.reserve(m);
  for (int i = 0; i < n; i++) {
    int p, t;
    scanf("%d%d", &p, &t);
    fs.push_back({p, t, i});
  }
  for (int i = 0; i < m; i++) {
    int p, b;
    scanf("%d%d", &p, &b);
    ms.push_back({p, b});
  }
  solve(fs, ms);
  return 0;
}
