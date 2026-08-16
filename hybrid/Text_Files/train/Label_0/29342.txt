#include <bits/stdc++.h>
using namespace std;
long long int X[100010], L[100010], T[100010], n, total, sol[100010],
    dp[100010];
vector<long long int> adj[100010], sv[100010];
struct KEY {
  long long int key, vt;
  KEY() {}
  KEY(long long int _key, long long int _vt) {
    key = _key;
    vt = _vt;
  }
  bool operator<(const KEY &o) const {
    if (key == o.key) {
      return vt < o.vt;
    }
    return key < o.key;
  }
  bool operator>(const KEY &o) const {
    if (key == o.key) {
      return vt > o.vt;
    }
    return key > o.key;
  }
  bool operator==(const KEY &o) const { return key == o.key && vt == o.vt; }
};
struct node {
  long long int prior, sz, bis, tim;
  KEY key;
  node *l, *r, *p;
};
node *Treap;
long long int getSize(node *cur) { return cur ? cur->sz : 0; }
long long int getBis(node *cur) { return cur ? cur->bis : 0; }
long long int getTim(node *cur) { return cur ? cur->tim : 0; }
inline void update(node *cur) {
  if (!cur) {
    return;
  }
  if (cur->l) {
    cur->l->p = cur;
  }
  if (cur->r) {
    cur->r->p = cur;
  }
  cur->sz = getSize(cur->l) + 1 + getSize(cur->r);
  cur->bis = getBis(cur->l) + X[cur->key.vt] + getBis(cur->r);
  cur->tim = getTim(cur->l) + T[cur->key.vt] * X[cur->key.vt] + getTim(cur->r);
}
inline node *newNode(KEY key) {
  node *ret = (node *)malloc(sizeof(node));
  ret->key = key;
  ret->sz = 1;
  ret->bis = X[key.vt];
  ret->tim = X[key.vt] * T[key.vt];
  ret->p = ret->l = ret->r = NULL;
  ret->prior = rand();
  return ret;
}
void split(node *cur, node *&l, node *&r, KEY key) {
  if (!cur) {
    l = r = NULL;
  } else if (cur->key < key) {
    split(cur->r, cur->r, r, key), l = cur;
  } else {
    split(cur->l, l, cur->l, key), r = cur;
  }
  update(cur);
}
void merge(node *&cur, node *l, node *r) {
  if (!l || !r) {
    cur = l ? l : r;
  } else if (l->prior > r->prior) {
    merge(l->r, l->r, r), cur = l;
  } else {
    merge(r->l, l, r->l), cur = r;
  }
  update(cur);
}
void insert(node *&cur, node *it) {
  if (!cur) {
    cur = it;
  } else if (it->prior > cur->prior) {
    split(cur, it->l, it->r, it->key), cur = it;
  } else if (cur->key < it->key) {
    insert(cur->r, it);
  } else {
    insert(cur->l, it);
  }
  update(cur);
}
void remove(node *&cur, KEY key) {
  if (!cur) {
    return;
  } else if (cur->key == key) {
    node *temp = cur;
    merge(cur, cur->l, cur->r);
    free(temp);
  } else if (cur->key < key) {
    remove(cur->r, key);
  } else {
    remove(cur->l, key);
  }
  update(cur);
}
void printTreap(node *cur) {
  if (!cur) {
    return;
  }
  if (cur->l) {
    printTreap(cur->l);
  }
  printf("%lld %lld %lld %lld\n", cur->key.key, cur->key.vt,
         T[cur->key.vt] * X[cur->key.vt], X[cur->key.vt]);
  if (cur->r) {
    printTreap(cur->r);
  }
}
long long int query(node *cur, long long int tim, long long int bis) {
  long long int ret;
  if (tim < getTim(cur->l)) {
    ret = query(cur->l, tim, bis);
  } else if (tim <= getTim(cur->l) + T[cur->key.vt] * X[cur->key.vt]) {
    ret = bis + getBis(cur->l) + (tim - getTim(cur->l)) / T[cur->key.vt];
  } else if (tim <= getTim(cur)) {
    ret =
        query(cur->r, tim - (getTim(cur->l) + T[cur->key.vt] * X[cur->key.vt]),
              bis + getBis(cur->l) + X[cur->key.vt]);
  } else {
    ret = bis + cur->bis;
  }
  return ret;
}
void input() {
  long long int i, j, x;
  scanf("%lld %lld", &n, &total);
  for (i = 1; i <= n; i++) {
    scanf("%lld", &X[i]);
  }
  for (i = 1; i <= n; i++) {
    scanf("%lld", &T[i]);
  }
  for (i = 2; i <= n; i++) {
    scanf("%lld %lld", &x, &L[i]);
    adj[i].push_back(x);
    adj[x].push_back(i);
  }
}
void dfs(long long int src, long long int par, long long int d) {
  long long int i, j, u, p;
  insert(Treap, newNode(KEY(T[src], src)));
  p = total - 2 * d;
  if (p >= 0) {
    sol[src] = query(Treap, p, 0);
  }
  for (i = 0; i < adj[src].size(); i++) {
    u = adj[src][i];
    if (u != par) {
      dfs(u, src, d + L[u]);
    }
  }
  remove(Treap, KEY(T[src], src));
}
void dfs1(long long int src, long long int par, long long int d) {
  long long int i, j, u, sz;
  for (i = 0; i < adj[src].size(); i++) {
    u = adj[src][i];
    if (u != par) {
      dfs1(u, src, d + 1);
      sv[src].push_back(dp[u]);
    }
  }
  if (d == 0) {
    sort(sv[src].begin(), sv[src].end());
    sz = sv[src].size();
    dp[src] = max(sol[src], sv[src][sz - 1]);
  } else {
    dp[src] = sol[src];
    sort(sv[src].begin(), sv[src].end());
    sz = sv[src].size();
    if (sz >= 2) {
      dp[src] = max(dp[src], sv[src][sz - 2]);
    }
  }
}
void solve() {
  long long int i, j;
  dfs(1, 0, 0);
  dfs1(1, 0, 0);
  printf("%lld", dp[1]);
  puts("");
}
int main() {
  input();
  solve();
}
