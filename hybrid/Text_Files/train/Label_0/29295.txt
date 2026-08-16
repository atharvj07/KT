#include <bits/stdc++.h>
using namespace std;
const int MAX = 800000 + 10;
const double INF = 1e30;
const double EPS = 0.02;
struct point {
  double x, y;
  point(double a, double b) {
    x = a;
    y = b;
  }
  point() {}
  void print() { printf("%lf %lf\n", x, y); }
};
double sqr(double x) { return x * x; }
double dist(const point& a, const point& b) {
  return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
}
double chaji(const point& s, const point& a, const point& b) {
  return (a.x - s.x) * (b.y - s.y) - (a.y - s.y) * (b.x - s.x);
}
int n, S, T;
point d[MAX], TOP(0, INF);
int head[MAX * 4], t[MAX * 4], tot, nxt[MAX * 4];
double c[MAX * 4];
void addedge(int x, int y, double v) {
  t[++tot] = y;
  nxt[tot] = head[x];
  head[x] = tot;
  c[tot] = v;
}
struct line {
  int s, t, type, number;
  line() {}
  line(int a, int b) {
    s = a;
    t = b;
    type = 0;
  }
  void print() const {
    d[s].print();
    d[t].print();
    printf("\n");
  }
} l[MAX];
point get(point b, point c, double x) {
  double k = (x - b.x) / (c.x - b.x);
  return point(b.x + (c.x - b.x) * k, b.y + (c.y - b.y) * k);
}
int operator<(const line& a, const line& b) {
  double l = max(d[a.s].x, d[b.s].x), r = min(d[a.t].x, d[b.t].x);
  double x = (l + r) * 0.5;
  point s1 = get(d[a.s], d[a.t], x), s2 = get(d[b.s], d[b.t], x);
  if (s1.y != s2.y)
    return s1.y < s2.y;
  else
    return a.number < b.number;
}
set<line> st;
struct accident {
  int x, num, flag;
  accident(double c, int a, int b) {
    x = c;
    num = a;
    flag = b;
  }
  accident() {}
} p[MAX];
int operator<(const accident& a, const accident& b) { return a.x < b.x; }
int num;
void add(double x, line A, line B) {
  point a = d[A.s], h = d[A.t], b = d[B.s], c = d[B.t];
  point e = get(b, c, x), f = get(a, h, x);
  addedge(A.s, B.s, dist(a, f) + dist(f, e) + dist(e, b));
  addedge(A.s, B.t, dist(a, f) + dist(f, e) + dist(e, c));
  addedge(A.t, B.s, dist(h, f) + dist(f, e) + dist(e, b));
  addedge(A.t, B.t, dist(h, f) + dist(f, e) + dist(e, c));
}
int same(double x, line A, line B) {
  point a = d[A.s], h = d[A.t], b = d[B.s], c = d[B.t];
  point e = get(b, c, x), f = get(a, h, x);
  return fabs(e.y - f.y) < 0.0000000001;
}
queue<int> q;
int hh[MAX];
double dis[MAX];
double SPFA() {
  int i, u, v;
  for (i = 1; i <= n; ++i) dis[i] = INF;
  q.push(S);
  dis[S] = 0;
  hh[S] = 1;
  while (!q.empty()) {
    u = q.front();
    q.pop();
    hh[u] = 0;
    for (i = head[u]; i; i = nxt[i]) {
      v = t[i];
      if (dis[v] > dis[u] + c[i]) {
        dis[v] = dis[u] + c[i];
        if (!hh[v]) {
          hh[v] = 1;
          q.push(v);
        }
      }
    }
  }
  return dis[T];
}
void update(int now) {
  set<line>::iterator ii, it = st.find(l[p[now].num]);
  if (it == st.end()) return;
  if (it->type == -1) {
    ii = it;
    ++ii;
    while (same(p[now].x, *ii, *it) && ii->type == it->type) {
      ++ii;
      if (ii == st.end()) return;
    }
    if (ii == st.end()) return;
  }
  if (it->type == 1) {
    if (it == st.begin()) return;
    ii = it;
    --ii;
    while (same(p[now].x, *ii, *it) && ii->type == it->type) {
      if (ii == st.begin()) return;
      --ii;
    }
    swap(ii, it);
  }
  if (it->type == ii->type) return;
  add(p[now].x, *ii, *it);
}
int main() {
  int i, j, now;
  scanf("%d", &n);
  for (i = 1; i <= n; ++i) scanf("%lf%lf", &d[i].x, &d[i].y);
  scanf("%d%d", &S, &T);
  for (i = 1; i <= n; ++i) {
    j = (i == n ? 1 : i + 1);
    addedge(i, j, dist(d[i], d[j]));
    addedge(j, i, dist(d[j], d[i]));
    l[i] = line(i, j);
    l[i].number = i;
    if (d[i].x != d[j].x) {
      if (chaji(d[i], d[j], TOP) >= 0)
        l[i].type = -1;
      else
        l[i].type = 1;
      if (d[l[i].s].x > d[l[i].t].x) swap(l[i].s, l[i].t);
      p[++num] = accident((int)d[l[i].s].x, i, 1);
      p[++num] = accident((int)d[l[i].t].x, i, -1);
    }
  }
  set<line>::iterator it;
  sort(p + 1, p + num + 1);
  for (now = 1; now <= num;) {
    j = now;
    while (j <= num && p[j].x == p[now].x) {
      if (p[j].flag == 1) {
        st.insert(l[p[j].num]);
      }
      ++j;
    }
    j = now;
    while (j <= num && p[j].x == p[now].x) update(j), ++j;
    j = now;
    while (j <= num && p[j].x == p[now].x) {
      if (p[j].flag == -1) {
        st.erase(l[p[j].num]);
      }
      ++j;
    }
    now = j;
  }
  double ans = SPFA();
  printf("%lf\n", ans);
  return 0;
}
