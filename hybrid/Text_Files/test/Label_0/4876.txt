#include <bits/stdc++.h>
using namespace std;
struct Node {
  bool fr;
  int lb, rb;
  Node *lc, *rc;
};
void buildSeg(Node *&p, int l, int r) {
  p = new Node;
  p->fr = true;
  p->lb = l;
  p->rb = r;
  if (p->lb < p->rb) {
    int mid = (p->lb + p->rb) / 2;
    buildSeg(p->lc, p->lb, mid);
    buildSeg(p->rc, mid + 1, p->rb);
  }
}
void setVal(Node *p, int x, bool val) {
  if (p->lb == p->rb)
    p->fr = val;
  else {
    int mid = (p->lb + p->rb) / 2;
    if (x <= mid)
      setVal(p->lc, x, val);
    else
      setVal(p->rc, x, val);
    p->fr = p->lc->fr | p->rc->fr;
  }
}
int findFr(Node *p, int l, int r) {
  if (p->fr) {
    if (p->lb == p->rb)
      return p->lb;
    else {
      int mid = (p->lb + p->rb) / 2, ret = -1;
      if (l <= mid) ret = findFr(p->lc, l, r);
      if ((mid + 1 <= r) && (ret == -1)) ret = findFr(p->rc, l, r);
      return ret;
    }
  }
  return -1;
}
const int _N = 200010;
int h, m, n, ptN, pt[_N];
long long cost;
pair<int, int> inP[_N];
Node *rt;
map<int, int> ps;
void initSeg() {
  ptN = 0;
  int cnt = 0;
  for (int i = 0; i < h; i++) inP[i].first = -1;
  for (int i = 0; i < h; i++)
    if (inP[i].first == -1) {
      pt[ptN] = cnt;
      for (int j = i; inP[j].first == -1; j = (j + m) % h)
        inP[j] = pair<int, int>(ptN, cnt++);
      ptN++;
    }
  pt[ptN] = cnt;
  buildSeg(rt, 0, cnt - 1);
}
void pushHash(int i, int v) {
  int p = findFr(rt, inP[v].second, pt[inP[v].first + 1] - 1);
  if (p == -1) p = findFr(rt, pt[inP[v].first], inP[v].second - 1);
  setVal(rt, p, false);
  ps.insert(pair<int, int>(i, p));
  cost += (p >= inP[v].second)
              ? (p - inP[v].second)
              : (pt[inP[v].first + 1] - inP[v].second + p - pt[inP[v].first]);
}
void popHash(int i) {
  map<int, int>::iterator x = ps.find(i);
  setVal(rt, x->second, true);
  ps.erase(x);
}
int main() {
  ios::sync_with_stdio(false);
  cin >> h >> m >> n;
  initSeg();
  cost = 0;
  for (int k = 0; k < n; k++) {
    char c;
    int i;
    cin >> c >> i;
    if (c == '+') {
      int v;
      cin >> v;
      pushHash(i, v);
    } else
      popHash(i);
  }
  cout << cost << endl;
  return 0;
}
