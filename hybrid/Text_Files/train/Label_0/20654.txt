#include <bits/stdc++.h>
using namespace std;
const int N = 3e5 + 35;
struct Interval {
  int l, r, c, i;
};
struct Event {
  int l, t, i;
  Event() {}
  Event(int il, int it, int ii) {
    l = il;
    t = it;
    i = ii;
  }
};
bool operator<(Interval a, Interval b) {
  if (a.c != b.c) return a.c < b.c;
  return a.i < b.i;
}
bool operator<(Event a, Event b) {
  if (a.l != b.l) return a.l < b.l;
  if (a.t != b.t) return a.t < b.t;
  return a.i < b.i;
}
int n, C;
Interval clouds[N];
Event eventslist[N << 1];
pair<int, int> tr[N << 2];
int maxone[N], maxcombwith[N], ans[N];
map<int, int> maxcomb[N];
void build(int v, int l, int r) {
  tr[v] = {-1e9, l};
  if (l == r) return;
  int m = (l + r) / 2;
  build(v + v, l, m);
  build(v + v + 1, m + 1, r);
}
void update(int v, int l, int r, int ind) {
  if (l == r) {
    tr[v].first = maxone[l];
    return;
  }
  int m = (l + r) / 2;
  if (ind <= m)
    update(v + v, l, m, ind);
  else
    update(v + v + 1, m + 1, r, ind);
  tr[v] = max(tr[v + v], tr[v + v + 1]);
}
pair<int, int> query(int v, int s, int e, int l, int r) {
  if (l <= s && e <= r) return tr[v];
  int m = (s + e) / 2;
  if (r <= m) return query(v + v, s, m, l, r);
  if (m + 1 <= l) return query(v + v + 1, m + 1, e, l, r);
  return max(query(v + v, s, m, l, r), query(v + v + 1, m + 1, e, l, r));
}
int query(int ind) {
  int cc = C - clouds[ind].c;
  if (clouds[1].c > cc) return -1;
  int lo = 1, hi = n;
  while (lo < hi) {
    int mi = lo + (hi - lo + 1) / 2;
    if (clouds[mi].c <= cc)
      lo = mi;
    else
      hi = mi - 1;
  }
  if (lo < ind) return query(1, 1, n, 1, lo).second;
  if (lo == ind && lo == 1) return -1;
  if (lo == ind) return query(1, 1, n, 1, lo - 1).second;
  if (ind == 1) return query(1, 1, n, 2, lo).second;
  return max(query(1, 1, n, 1, ind - 1), query(1, 1, n, ind + 1, lo)).second;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout << setprecision(32);
  cin >> n >> C;
  for (int i = 1; i <= n; i++) {
    cin >> clouds[i].l >> clouds[i].r >> clouds[i].c;
    clouds[i].i = i;
  }
  sort(clouds + 1, clouds + n + 1);
  for (int i = 1; i <= n; i++) {
    clouds[i].i = i;
    eventslist[2 * i - 1] = Event(clouds[i].l, 0, i);
    eventslist[2 * i] = Event(clouds[i].r, 1, i);
  }
  sort(eventslist + 1, eventslist + (n << 1) + 1);
  int m;
  cin >> m;
  vector<pair<int, int> > queries;
  for (int i = 0; i < m; i++) {
    int x;
    cin >> x;
    queries.push_back({x, i});
    if (n == 0) {
      cout << x << '\n';
    }
  }
  if (n == 0) exit(0);
  sort(queries.rbegin(), queries.rend());
  memset(maxcombwith, 0, sizeof(maxcombwith));
  memset(maxone, 0, sizeof(maxone));
  int last = 0, curmax = 0, empty = 0;
  set<int> open;
  build(1, 1, n);
  for (int i = 1; i <= (n << 1); i++) {
    Event e = eventslist[i];
    if (open.empty()) {
      empty += e.l - last;
    } else if (open.size() == 1) {
      int ind1 = *open.begin();
      if (clouds[ind1].c <= C) {
        maxone[ind1] += e.l - last;
        maxcombwith[ind1] += e.l - last;
        int ind2 = query(ind1);
        if (ind2 != -1) {
          int tmp = maxone[ind1] + maxone[ind2];
          if (maxcomb[ind1].find(ind2) != maxcomb[ind1].end()) {
            tmp += maxcomb[ind1][ind2];
          }
          maxcombwith[ind1] = max(maxcombwith[ind1], tmp);
        }
        curmax = max(curmax, maxcombwith[ind1]);
        update(1, 1, n, ind1);
      }
    } else if (open.size() == 2) {
      int ind1 = *open.begin();
      int ind2 = *open.rbegin();
      if (clouds[ind1].c + clouds[ind2].c <= C) {
        maxcomb[ind1][ind2] += e.l - last;
        maxcomb[ind2][ind1] += e.l - last;
        maxcombwith[ind1] = max(maxcombwith[ind1], maxone[ind1] + maxone[ind2] +
                                                       maxcomb[ind1][ind2]);
        maxcombwith[ind2] = max(maxcombwith[ind2], maxone[ind1] + maxone[ind2] +
                                                       maxcomb[ind2][ind1]);
        curmax = max(curmax, maxcombwith[ind1]);
        curmax = max(curmax, maxcombwith[ind2]);
      }
    }
    while (!queries.empty()) {
      int x = queries.back().first;
      int k = queries.back().second;
      if (x <= curmax + empty) {
        queries.pop_back();
        ans[k] = e.l - (curmax + empty - x);
      } else {
        break;
      }
    }
    if (!e.t) {
      open.insert(e.i);
    } else {
      open.erase(e.i);
    }
    last = e.l;
  }
  while (!queries.empty()) {
    int x = queries.back().first;
    int k = queries.back().second;
    ans[k] = eventslist[n << 1].l - (curmax + empty - x);
    queries.pop_back();
  }
  for (int i = 0; i < m; i++) {
    cout << ans[i] << '\n';
  }
  return 0;
}
