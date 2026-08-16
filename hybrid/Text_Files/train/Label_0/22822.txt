#include <bits/stdc++.h>
using namespace std;
inline void read(int &x) {
  int flg = 1;
  char ch;
  while (!isdigit(ch = getchar()))
    if (ch == '-') flg = -flg;
  for (x = ch - '0'; isdigit(ch = getchar()); x = x * 10 + ch - '0')
    ;
  x *= flg;
}
const int MAXN = 100005;
const int MAXM = MAXN * 30;
const int inf = 2000000000;
int n, Q, mx, s[MAXN], m[MAXN], r[MAXN], t[MAXN];
int tot, lc[MAXM], rc[MAXM], rt[MAXN];
long long sr[MAXM], sm[MAXM];
void ins(int &i, int L, int R, int x, int vr, int vm) {
  ++tot;
  lc[tot] = lc[i], rc[tot] = rc[i];
  sr[tot] = sr[i] + vr;
  sm[tot] = sm[i] + vm;
  i = tot;
  if (L == R) return;
  int mid = (L + R) >> 1;
  x <= mid ? ins(lc[i], L, mid, x, vr, vm) : ins(rc[i], mid + 1, R, x, vr, vm);
}
long long qry(int i, int L, int R, int x, int y, int v) {
  if (!i) return 0;
  if (x <= L && R <= y) return v ? sm[i] : sr[i];
  int mid = (L + R) >> 1;
  long long re = 0;
  if (x <= mid) re += qry(lc[i], L, mid, x, y, v);
  if (y > mid) re += qry(rc[i], mid + 1, R, x, y, v);
  return re;
}
struct node {
  pair<int, int> x;
  int y;
  node(int a = 0, int b = 0, int c = 0) {
    x = pair<int, int>(a, b);
    y = c;
  }
  inline bool operator<(const node &o) const {
    return x == o.x ? y < o.y : x < o.x;
  }
};
set<node> st;
set<node>::iterator split_l(int x) {
  set<node>::iterator it = st.upper_bound(node(x, n + 1, 0));
  --it;
  if (it->x.first < x) {
    int L = it->x.first, R = it->x.second, t = it->y;
    st.erase(it);
    st.insert(node(L, x - 1, t));
    return st.insert(node(x, R, t)).first;
  } else
    return it;
}
set<node>::iterator split_r(int x) {
  set<node>::iterator it = st.upper_bound(node(x, n + 1, 0));
  --it;
  if (it->x.second > x) {
    int L = it->x.first, R = it->x.second, t = it->y;
    st.erase(it);
    st.insert(node(x + 1, R, t));
    return st.insert(node(L, x, t)).first;
  } else
    return it;
}
long long cal(int L, int R, int t) {
  long long re = 0;
  if (L == R) {
    int tmp = r[L] ? (m[L] - s[L] + r[L] - 1) / r[L] : inf;
    if (t >= tmp)
      re = m[L];
    else
      re = s[L] + r[L] * t;
    s[L] = 0;
    return re;
  }
  t = min(t, mx - 1);
  re += t *
        (qry(rt[R], 1, mx, t + 1, mx, 0) - qry(rt[L - 1], 1, mx, t + 1, mx, 0));
  if (t >= 1) re += qry(rt[R], 1, mx, 1, t, 1) - qry(rt[L - 1], 1, mx, 1, t, 1);
  return re;
}
int main() {
  read(n);
  mx = 1;
  for (int i = 1; i <= n; ++i) {
    read(s[i]), read(m[i]), read(r[i]);
    if (r[i])
      mx = max(mx, t[i] = (m[i] + r[i] - 1) / r[i]);
    else
      t[i] = -1;
    st.insert(node(i, i, 0));
  }
  ++mx;
  for (int i = 1; i <= n; ++i)
    ins(rt[i] = rt[i - 1], 1, mx, (~t[i]) ? t[i] : mx, r[i], m[i]);
  read(Q);
  int t, L, R;
  while (Q--) {
    read(t), read(L), read(R);
    set<node>::iterator itL = split_l(L), itR = split_r(R);
    long long ans = 0;
    if (itR->x.first == L && itR->x.second == R)
      ans += cal(L, R, t - itR->y), st.erase(itR);
    else {
      for (set<node>::iterator i = itL; i != itR;)
        ans += cal(i->x.first, i->x.second, t - i->y), st.erase(i++);
      ans += cal(itR->x.first, itR->x.second, t - itR->y), st.erase(itR);
    }
    st.insert(node(L, R, t));
    printf("%lld\n", ans);
  }
}
