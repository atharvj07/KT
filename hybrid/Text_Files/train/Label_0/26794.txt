#include <bits/stdc++.h>
using namespace std;
template <class C>
void mini(C &a4, C b4) {
  a4 = min(a4, b4);
}
template <class C>
void maxi(C &a4, C b4) {
  a4 = max(a4, b4);
}
template <class T1, class T2>
ostream &operator<<(ostream &out, pair<T1, T2> pair) {
  return out << "(" << pair.first << ", " << pair.second << ")";
}
struct SegmentTree {
  int n;
  struct pr {
    int x, y;
    pr() {}
    pr(int _x, int _y) : x(_x), y(_y) {}
    bool operator<(pr const &p) const { return x < p.x; }
  };
  struct node {
    int b, e;
    vector<pr> v;
    void single(int y1, int y2, vector<int> &res) {
      while (b <= e && v[e].x > y2) {
        res.push_back(v[e].y);
        --e;
      }
      while (b <= e && v[b].x < y1) {
        res.push_back(v[b].y);
        ++b;
      }
    }
  };
  vector<pair<int, pr> > to_add;
  vector<node> T;
  SegmentTree(int _n) {
    n = 1;
    while (n < _n) n *= 2;
    T = vector<node>(2 * n);
  };
  void add(int x, int y, int id) { to_add.push_back(make_pair(x, pr(y, id))); }
  void _query(int i, int bb, int ee, int b, int e, int y1, int y2,
              vector<int> &res) {
    if (ee <= b || e <= bb) return;
    if (b <= bb && ee <= e) {
      T[i].single(y1, y2, res);
      return;
    }
    _query(2 * i, bb, (bb + ee) / 2, b, e, y1, y2, res);
    _query(2 * i + 1, (bb + ee) / 2, ee, b, e, y1, y2, res);
  }
  void query(int b, int e, int y1, int y2, vector<int> &res) {
    _query(1, 0, n, b, e, y1, y2, res);
  }
  void init() {
    sort((to_add).begin(), (to_add).end());
    for (auto tr : to_add) {
      T[n + tr.first].v.push_back(tr.second);
    }
    for (int i = (n - 1); i >= (1); --i) {
      T[i].v.resize(T[2 * i].v.size() + T[2 * i + 1].v.size());
      merge((T[2 * i].v).begin(), (T[2 * i].v).end(), (T[2 * i + 1].v).begin(),
            (T[2 * i + 1].v).end(), T[i].v.begin());
    }
    for (int i = 0; i < (2 * n); ++i) {
      T[i].b = 0;
      T[i].e = ((int)(T[i].v).size()) - 1;
    }
  }
};
struct Tree {
  int n;
  struct node {
    int par;
    int in, out;
    vector<int> ngb;
  };
  vector<node> T;
  SegmentTree S;
  vector<pair<int, int> > edg;
  Tree(int _n) : n(_n), T(_n), S(2 * _n) {}
  void add_edge(int a, int b) {
    edg.push_back(make_pair(b, a));
    T[b].ngb.push_back(a);
    T[a].ngb.push_back(b);
  }
  void dfs(int &t, int i = 0, int par = -1) {
    node &v = T[i];
    v.par = par;
    v.in = t;
    ++t;
    for (auto j : v.ngb) {
      if (j != par) dfs(t, j, i);
    }
    v.out = t;
    ++t;
    return;
  }
  void insert(int i, int j, int v) {
    if (T[i].out > T[j].out) swap(i, j);
    S.add(T[i].out, T[j].out, v);
    S.add(T[j].out, T[i].out, v);
  }
  vector<int> get(int id) {
    vector<int> res;
    pair<int, int> p = edg[id];
    int i = p.first;
    if (T[p.first].par != p.second) i = p.second;
    S.query(T[i].in, T[i].out + 1, T[i].in, T[i].out, res);
    return res;
  }
};
int main() {
  int n;
  scanf("%d", &n);
  vector<Tree> T(2, Tree(n));
  vector<vector<bool> > del(2, vector<bool>(n - 1, false));
  for (int t = 0; t < (2); ++t) {
    for (int i = 0; i < (n - 1); ++i) {
      int a;
      scanf("%d", &a);
      --a;
      T[t].add_edge(i + 1, a);
    }
    int time = 0;
    T[t].dfs(time);
  }
  for (int t = 0; t < (2); ++t) {
    for (int i = 0; i < (n - 1); ++i) {
      pair<int, int> p = T[1 - t].edg[i];
      T[t].insert(p.first, p.second, i);
    }
    T[t].S.init();
  }
  int t = 0;
  int id;
  vector<int> cur;
  scanf("%d", &id);
  --id;
  cur.push_back(id);
  del[1][id] = true;
  while (!cur.empty()) {
    vector<int> prv = cur;
    cur.clear();
    if (t % 2 == 0)
      printf("Blue\n");
    else
      printf("Red\n");
    for (int j : prv) {
      printf("%d ", j + 1);
    }
    printf("\n");
    cur.clear();
    for (int j : prv) {
      vector<int> me = (T[t].get(j));
      for (int k : me) {
        if (!del[t][k]) {
          del[t][k] = true;
          cur.push_back(k);
        }
      }
    }
    sort((cur).begin(), (cur).end());
    t = 1 - t;
  }
  return 0;
}
