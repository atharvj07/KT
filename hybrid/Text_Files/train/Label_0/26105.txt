#include <bits/stdc++.h>
using namespace std;
template <typename T, typename F>
struct SEGMENT_TREE {
  long long Li, Ri;
  long long pt = 0;
  vector<T> ST;
  vector<long long> L;
  vector<long long> R;
  vector<bool> lazy;
  SEGMENT_TREE(long long a, long long b) {
    assert(a <= b);
    Li = a, Ri = b;
    ST.push_back(T{});
    L.push_back(0);
    R.push_back(0);
    lazy.push_back(false);
  }
  void build(vector<T> &vect) {
    assert(Li == 0ll && Ri == (long long)vect.size() - 1ll);
    ST_build(0, Li, Ri, vect);
  }
  void update(long long a, long long b, F &up) {
    ST_update(0, Li, Ri, a, b, up);
  }
  T query(long long a, long long b) { return ST_query(0, Li, Ri, a, b); }
  void ST_build(long long node, long long l, long long r, vector<T> &vect) {
    if (l == r) {
      ST[node] = vect[l];
      return;
    } else {
      L[node] = ++pt;
      ST.push_back(T{});
      L.push_back(0);
      R.push_back(0);
      lazy.push_back(false);
      R[node] = ++pt;
      ST.push_back(T{});
      L.push_back(0);
      R.push_back(0);
      lazy.push_back(false);
    }
    long long mid = (l + r) / 2;
    ST_build(L[node], l, mid, vect);
    ST_build(R[node], mid + 1, r, vect);
    ST[node].merge(ST[L[node]], ST[R[node]]);
  }
  void ST_update(long long node, long long l, long long r, long long a,
                 long long b, F &up) {
    if (l != r) {
      if (L[node] == 0) {
        L[node] = ++pt;
        ST.push_back(T{});
        L.push_back(0);
        R.push_back(0);
        lazy.push_back(false);
      }
      if (R[node] == 0) {
        R[node] = ++pt;
        ST.push_back(T{});
        L.push_back(0);
        R.push_back(0);
        lazy.push_back(false);
      }
    }
    if (lazy[node]) {
      if (l != r) {
        ST[node].propagation(ST[L[node]], ST[R[node]]);
        lazy[L[node]] = true;
        lazy[R[node]] = true;
      }
      ST[node].update(l, r);
      lazy[node] = false;
    }
    if (r < a || l > b) return;
    if (a <= l && r <= b) {
      ST[node].push(up);
      if (l != r) {
        ST[node].propagation(ST[L[node]], ST[R[node]]);
        lazy[L[node]] = true;
        lazy[R[node]] = true;
      }
      ST[node].update(l, r);
      return;
    }
    long long mid = (l + r) / 2;
    ST_update(L[node], l, mid, a, b, up);
    ST_update(R[node], mid + 1, r, a, b, up);
    ST[node].merge(ST[L[node]], ST[R[node]]);
  }
  T ST_query(long long node, long long l, long long r, long long a,
             long long b) {
    if (l != r) {
      if (L[node] == 0) {
        L[node] = ++pt;
        ST.push_back(T{});
        L.push_back(0);
        R.push_back(0);
        lazy.push_back(false);
      }
      if (R[node] == 0) {
        R[node] = ++pt;
        ST.push_back(T{});
        L.push_back(0);
        R.push_back(0);
        lazy.push_back(false);
      }
    }
    if (lazy[node]) {
      if (l != r) {
        ST[node].propagation(ST[L[node]], ST[R[node]]);
        lazy[L[node]] = true;
        lazy[R[node]] = true;
      }
      ST[node].update(l, r);
      lazy[node] = false;
    }
    if (a <= l && r <= b) {
      return ST[node];
    }
    long long mid = (l + r) / 2;
    T qu;
    bool flag = false;
    if (a <= mid) {
      qu = ST_query(L[node], l, mid, a, b);
      flag = true;
    }
    if (b > mid) {
      T temp = ST_query(R[node], mid + 1, r, a, b);
      if (flag)
        qu.merge(qu, temp);
      else
        swap(qu, temp);
    }
    return qu;
  }
};
struct QUERY {
  long long L, R;
};
struct NODE {
  long long init, last;
  long long L, R;
  void merge(NODE &H1, NODE &H2) {
    if (H1.L == -1 || H2.L == -1) {
      L = -1, R = -1;
      return;
    }
    R = H1.R;
    L = max(H1.L, H2.L);
    if (L > R) {
      L = -1;
      R = -1;
      return;
    }
    long long me = min(H1.last, H2.init);
    if (me < H2.L) {
      L = -1, R = -1;
      return;
    }
    init = H1.init;
    last = min(H1.last, H2.last);
  }
  void push(QUERY &Q) {
    init = Q.R;
    last = Q.R;
    L = Q.L;
    R = Q.R;
  }
  void update(long long l, long long r) {}
  void propagation(NODE &H1, NODE &H2) {}
};
const long long MAXN = 4e5 + 100;
set<long long> st[MAXN];
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  long long N, M, Q;
  cin >> N >> M >> Q;
  SEGMENT_TREE<NODE, QUERY> ST(0, N - 1);
  vector<NODE> vect;
  for (long long i = 0; i < N; i++) {
    NODE tp;
    tp.init = M;
    tp.last = M;
    tp.L = 0;
    tp.R = M;
    vect.push_back(tp);
  }
  ST.build(vect);
  for (long long i = 0; i < Q; i++) {
    long long x, y;
    cin >> x >> y;
    if (st[x].find(y) != st[x].end()) {
      st[x].erase(y);
    } else {
      st[x].insert(y);
    }
    long long pos = (x - 1) / 2;
    long long me, ma;
    if (st[pos * 2 + 1].size()) {
      me = (*st[pos * 2 + 1].begin()) / 2 + 1 - 1;
    } else {
      me = M;
    }
    if (st[pos * 2 + 2].size()) {
      ma = (*(--st[pos * 2 + 2].end())) / 2;
    } else {
      ma = 0;
    }
    QUERY tp;
    if (ma <= me) {
      tp.L = ma, tp.R = me;
    } else {
      tp.L = -1, tp.R = -1;
    }
    ST.update(pos, pos, tp);
    if (ST.query(0, N - 1).L != -1) {
      cout << "YES" << '\n';
    } else {
      cout << "NO" << '\n';
    }
  }
  return 0;
}
