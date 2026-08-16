#include <bits/stdc++.h>
const int MAX_N = 2e5 + 10, SIGMA = 26;
int N, ans;
char S[MAX_N];
struct SegTree {
  int l, r, m;
  SegTree *cl, *cr;
  SegTree(int l, int r)
      : l(l), r(r), m((l + r) / 2), cl(nullptr), cr(nullptr) {}
};
SegTree *touch(int l, int r, int x) {
  SegTree *res = new SegTree(l, r);
  if (l != r) {
    if (x <= res->m)
      res->cl = touch(l, res->m, x);
    else
      res->cr = touch(res->m + 1, r, x);
  }
  return res;
}
SegTree *merge(SegTree *a, SegTree *b) {
  if (!a) return b;
  if (!b) return a;
  SegTree *res = new SegTree(a->l, a->r);
  res->cl = merge(a->cl, b->cl);
  res->cr = merge(a->cr, b->cr);
  return res;
}
int last_before(SegTree *t, int x) {
  if (!t || t->l > x) return -1;
  if (t->l == t->r) return t->l;
  int res = last_before(t->cr, x);
  return res == -1 ? last_before(t->cl, x) : res;
}
int first_after(SegTree *t, int x) {
  if (!t || t->r < x) return -1;
  if (t->l == t->r) return t->l;
  int res = first_after(t->cl, x);
  return res == -1 ? first_after(t->cr, x) : res;
}
struct SAM {
  struct Node {
    int len, right, f, flen;
    Node *trans[SIGMA], *fail;
    SegTree *seg, *fseg;
    Node(SAM *sam, int len, int right)
        : len(len),
          right(right),
          f(0),
          flen(0),
          fail(nullptr),
          seg(nullptr),
          fseg(nullptr) {
      sam->nodes.push_back(this);
      std::fill_n(trans, SIGMA, nullptr);
    }
  } * empty, *last;
  std::vector<Node *> nodes;
  SAM() { last = empty = new Node(this, 0, 0); }
  void extend(int ch) {
    Node *u = new Node(this, last->len + 1, last->len + 1), *v = last;
    for (; v && !v->trans[ch]; v = v->fail) v->trans[ch] = u;
    if (!v)
      u->fail = empty;
    else {
      Node *q = v->trans[ch];
      if (q->len == v->len + 1)
        u->fail = q;
      else {
        Node *p = new Node(this, v->len + 1, 0);
        p->fail = q->fail;
        q->fail = u->fail = p;
        std::copy_n(q->trans, SIGMA, p->trans);
        for (; v && v->trans[ch] == q; v = v->fail) v->trans[ch] = p;
      }
    }
    last = u;
  }
  void solve() {
    sort(nodes.begin(), nodes.end(),
         [](Node *a, Node *b) { return a->len < b->len; });
    for (auto i = nodes.rbegin(); i != nodes.rend(); i++) {
      Node *node = *i;
      if (node->right) node->seg = merge(node->seg, touch(1, N, node->right));
      if (node->fail) node->fail->seg = merge(node->seg, node->fail->seg);
    }
    for (Node *node : nodes) {
      if (node == empty) continue;
      if (node->fail == empty) {
        node->f = 1;
        node->fseg = node->seg;
        node->flen = node->len;
      } else {
        int p = first_after(node->seg, 1);
        int pf = last_before(node->fail->fseg, p - 1);
        if (pf - node->fail->flen + 1 >= p - node->len + 1) {
          node->f = node->fail->f + 1;
          node->fseg = node->seg;
          node->flen = node->len;
        } else {
          node->f = node->fail->f;
          node->fseg = node->fail->fseg;
          node->flen = node->fail->flen;
        }
      }
      ans = std::max(ans, node->f);
    }
  }
} sam;
int main() {
  std::scanf("%d", &N);
  std::scanf("%s", S + 1);
  for (int i = 1; i <= N; i++) sam.extend(S[i] - 'a');
  sam.solve();
  std::printf("%d\n", ans);
}
