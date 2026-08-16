#include <bits/stdc++.h>
using namespace std;
int n, m;
struct Pair {
  int id, v;
  Pair() { id = v = 0; }
  Pair(int a, int b) {
    id = a;
    v = b;
  }
  friend bool operator<(const Pair &a, const Pair &b) { return a.v < b.v; }
  friend bool operator>(const Pair &a, const Pair &b) { return a.v > b.v; }
  friend Pair max(const Pair &a, const Pair &b) { return a < b ? b : a; }
  friend Pair min(const Pair &a, const Pair &b) { return a < b ? a : b; }
};
priority_queue<Pair> q;
priority_queue<Pair, vector<Pair>, greater<Pair> > p;
struct node {
  int x, y, v, id;
} a[200010], b[200010];
bool cmp1(const node &a, const node &b) {
  return a.x == b.x ? a.y < b.y : a.x < b.x;
}
bool cmp2(const node &a, const node &b) {
  return a.y == b.y ? a.x > b.x : a.y > b.y;
}
struct Splay {
  struct node {
    int key, size;
    Pair v, mx;
    int ch[2], pnt;
    node() {
      ch[0] = ch[1] = pnt = 0;
      key = 0;
      size = 0;
      v = mx = Pair(0, 0);
    }
  } tr[200010];
  int tot, root;
  Splay() {
    tot = 0;
    root = 0;
    tr[0].v.v = tr[0].mx.v = 0;
  }
  void update(int x) {
    tr[x].mx = tr[x].v;
    if (tr[x].ch[0] && tr[x].mx < tr[tr[x].ch[0]].mx)
      tr[x].mx = tr[tr[x].ch[0]].mx;
    if (tr[x].ch[1] && tr[x].mx < tr[tr[x].ch[1]].mx)
      tr[x].mx = tr[tr[x].ch[0]].mx;
    tr[x].size = 1;
    if (tr[x].ch[0]) tr[x].size += tr[tr[x].ch[0]].size;
    if (tr[x].ch[1]) tr[x].size += tr[tr[x].ch[1]].size;
  }
  void rotate(int x, bool b) {
    int y = tr[x].pnt;
    int z = tr[y].pnt;
    int son = tr[x].ch[b];
    if (son) tr[son].pnt = y;
    tr[y].pnt = x;
    tr[x].pnt = z;
    if (z) tr[z].ch[tr[z].ch[1] == y] = x;
    tr[x].ch[b] = y;
    tr[y].ch[!b] = son;
    update(y);
  }
  void splay(int x, int target) {
    while (tr[x].pnt != target) {
      int y = tr[x].pnt;
      if (tr[y].pnt == target)
        rotate(x, tr[y].ch[0] == x);
      else {
        int z = tr[y].pnt;
        bool c = tr[y].ch[0] == x, d = tr[z].ch[0] == y;
        if (c == d)
          rotate(y, c), rotate(x, c);
        else
          rotate(x, c), rotate(x, d);
      }
    }
    update(x);
    if (target == 0) root = x;
  }
  void insert(int id, int key, int val) {
    int x = root;
    if (!root) {
      root = ++tot;
      tr[tot].pnt = 0;
      tr[tot].key = key;
      tr[tot].v = Pair(id, val);
      update(tot);
      return;
    }
    while (1) {
      if (tr[x].key == key) {
        tr[x].v = max(tr[x].v, Pair(id, val));
        update(x);
        return;
      }
      if (tr[x].key < key) {
        if (!tr[x].ch[1]) {
          ++tot;
          tr[x].ch[1] = tot;
          tr[tot].pnt = x;
          tr[tot].key = key;
          tr[tot].v = Pair(id, val);
          update(tot);
          splay(tot, 0);
          return;
        } else
          x = tr[x].ch[1];
      }
      if (tr[x].key > key) {
        if (!tr[x].ch[0]) {
          ++tot;
          tr[x].ch[0] = tot;
          tr[tot].key = key;
          tr[tot].pnt = x;
          tr[tot].v = Pair(id, val);
          update(tot);
          splay(tot, 0);
          return;
        } else
          x = tr[x].ch[0];
      }
    }
  }
  Pair query(int x, int key) {
    if (!x) return Pair(0, 0);
    int l = tr[x].ch[0], r = tr[x].ch[1];
    Pair res;
    if (tr[x].key < key) {
      if (r)
        return query(r, key);
      else
        return Pair(0, 0);
    } else if (tr[x].key > key) {
      if (l)
        return max(query(l, key), max(tr[r].mx, tr[x].v));
      else
        return max(tr[r].mx, tr[x].v);
    } else if (tr[x].key == key) {
      return max(tr[r].mx, tr[x].v);
    }
  }
} sp;
int main() {
  int ansx, ansy;
  long long ans = 0;
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) {
    scanf("%d%d", &a[i].x, &a[i].y);
    a[i].id = i;
  }
  for (int i = 1; i <= m; i++) {
    scanf("%d%d%d", &b[i].x, &b[i].y, &b[i].v);
    b[i].id = i;
  }
  sort(a + 1, a + 1 + n, cmp1);
  sort(b + 1, b + 1 + m, cmp1);
  for (int i = 1, j = 1; i <= m; i++) {
    for (; j <= n && a[j].x <= b[i].x; j++) q.push(Pair(a[j].id, a[j].y));
    if (!q.size()) continue;
    long long tmp = 1ll * (min(q.top().v, b[i].y) - b[i].x) * b[i].v;
    if (tmp > ans) {
      ans = tmp;
      ansx = q.top().id;
      ansy = b[i].id;
    }
  }
  for (int i = 1, j = 1; i <= n; i++) {
    for (; j <= m && b[j].x <= a[i].x; j++) sp.insert(b[j].id, b[j].y, b[j].v);
    Pair re = sp.query(sp.root, a[i].y);
    long long tmp = 1ll * (a[i].y - a[i].x) * re.v;
    if (tmp > ans) {
      ans = tmp;
      ansx = a[i].id;
      ansy = re.id;
    }
  }
  sort(a + 1, a + 1 + n, cmp2);
  sort(b + 1, b + 1 + m, cmp2);
  for (int i = 1, j = 1; i <= m; i++) {
    for (; j <= n && a[j].y >= b[i].y; j++) p.push(Pair(a[j].id, a[j].x));
    if (!p.size()) continue;
    long long tmp = 1ll * (b[i].y - max(p.top().v, b[i].x)) * b[i].v;
    if (tmp > ans) {
      ans = tmp;
      ansx = p.top().id;
      ansy = b[i].id;
    }
  }
  printf("%I64d\n", ans);
  if (ans > 0) {
    printf("%d %d", ansx, ansy);
  }
  return 0;
}
