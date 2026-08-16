#include <bits/stdc++.h>
int n, m, cnt;
long long tr[400010], tags[400010], tage[400010];
void addtag(long long s, long long e, int x, int l, int r) {
  tr[x] += s * (r - l + 1) + 1ll * (r - l) * (r - l + 1) / 2 * e;
  tags[x] += s, tage[x] += e;
}
void pushdown(int x, int ls, int rs, int l, int mid, int r) {
  if (tage[x] || tags[x]) {
    addtag(tags[x], tage[x], ls, l, mid);
    addtag(tags[x] + tage[x] * (mid - l + 1), tage[x], rs, mid + 1, r);
    tags[x] = tage[x] = 0;
  }
}
void update(int pl, int pr, long long ps, long long pe, int x = 1, int l = 1,
            int r = n) {
  if (l == pl && r == pr) return addtag(ps, pe, x, l, r);
  int mid = (l + r) >> 1, ls = x << 1, rs = x << 1 | 1;
  pushdown(x, ls, rs, l, mid, r);
  if (pr <= mid)
    update(pl, pr, ps, pe, ls, l, mid);
  else if (pl > mid)
    update(pl, pr, ps, pe, rs, mid + 1, r);
  else
    update(pl, mid, ps, pe, ls, l, mid),
        update(mid + 1, pr, ps + (mid - pl + 1) * pe, pe, rs, mid + 1, r);
  tr[x] = tr[ls] + tr[rs];
}
void dfs(int x = 1, int l = 1, int r = n) {
  printf("%d %d %lld %lld %lld\n", l, r, tr[x], tags[x], tage[x]);
  if (l == r) return;
  int mid = (l + r) >> 1, ls = x << 1, rs = x << 1 | 1;
  pushdown(x, ls, rs, l, mid, r);
  dfs(ls, l, mid), dfs(rs, mid + 1, r);
}
long long query(int p, int x = 1, int l = 1, int r = n) {
  if (l == r) return tr[x];
  int mid = (l + r) >> 1, ls = x << 1, rs = x << 1 | 1;
  pushdown(x, ls, rs, l, mid, r);
  if (p <= mid)
    return query(p, ls, l, mid);
  else
    return query(p, rs, mid + 1, r);
}
std::set<std::pair<int, int>> st[200010];
struct node {
  int l, r, x;
  node() : l(), r(), x() {}
  node(int _l, int _r, int _c) : l(_l), r(_r), x(_c) {}
  bool operator<(node const &x) const { return l < x.l; }
};
std::set<node> s;
std::map<int, int> mp;
void insert(int l, int r, int x) {
  s.emplace(l, r, x);
  std::set<std::pair<int, int>>::iterator it = st[x].emplace(l, r).first;
  int pre = (--it)->second;
  ++it;
  int nxt = (++it)->first;
  int k = std::min(l - pre, nxt - r), f = std::max(l - pre, nxt - r);
  update(1, k, r - l + 1, 1);
  if (k != f) {
    update(k + 1, f, k + r - l, 0);
  }
  if (f + 1 <= nxt - pre - 1) update(f + 1, nxt - pre - 1, k + r - l - 1, -1);
}
std::set<node>::iterator split(int pos) {
  std::set<node>::iterator it = s.lower_bound(node(pos, 0, 0));
  if (it->l == pos) return it;
  --it;
  int l = it->l, r = it->r, x = it->x;
  s.erase(it);
  st[x].erase(std::make_pair(l, r));
  st[x].emplace(l, pos - 1), st[x].emplace(pos, r);
  s.emplace(l, pos - 1, x);
  return s.emplace(pos, r, x).first;
}
void erase(int l, int r) {
  std::set<node>::iterator itr = split(r + 1), itl = split(l);
  for (std::set<node>::iterator it = itl; it != itr; ++it) {
    int l = it->l, r = it->r, x = it->x;
    std::set<std::pair<int, int>>::iterator i =
        st[x].find(std::make_pair(l, r));
    int pre = (--i)->second;
    ++i;
    int nxt = (++i)->first;
    st[x].erase(--i);
    int k = std::min(l - pre, nxt - r), f = std::max(l - pre, nxt - r);
    update(1, k, -(r - l + 1), -1);
    if (k != f) {
      update(k + 1, f, -(k + r - l), 0);
    }
    if (f + 1 <= nxt - pre - 1)
      update(f + 1, nxt - pre - 1, -(k + r - l - 1), 1);
  }
  s.erase(itl, itr);
}
int main() {
  scanf("%d%d", &n, &m);
  s.emplace(0, 0, 0), s.emplace(n + 1, n + 1, 0);
  for (int i = 1; i <= n + m; i++)
    st[i].emplace(0, 0), st[i].emplace(n + 1, n + 1);
  for (int i = 1, x; i <= n; i++) {
    scanf("%d", &x);
    if (!mp[x]) mp[x] = ++cnt;
    x = mp[x];
    insert(i, i, x);
  }
  for (int i = 1; i <= m; i++) {
    int op, l, r, x;
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d%d%d", &l, &r, &x);
      erase(l, r);
      if (!mp[x]) mp[x] = ++cnt;
      x = mp[x];
      insert(l, r, x);
    } else {
      scanf("%d", &x);
      printf("%lld\n", query(x));
    }
  }
  return 0;
}
