#include <bits/stdc++.h>
using namespace std;
const int Mod = 1e9 + 7;
const int digits = 1e5 + 20, Nmax = 1e5 + 5;
int x, y, c, n, m, pos0, pw[Nmax], i, start, finish, come[Nmax], answer = 0;
vector<pair<int, int> > v[Nmax];
bool expanded[Nmax];
class Node {
 public:
  Node *left, *right;
  int hash_val, sum;
  Node(Node *_left, Node *_right, int sz) {
    left = _left;
    right = _right;
    if (!sz) {
      sum = hash_val = 1;
      return;
    } else if (sz == -1) {
      sum = hash_val = 0;
      return;
    }
    sum = left->sum + right->sum;
    hash_val =
        ((long long)left->hash_val * pw[(sz + 1) / 2] + right->hash_val) % Mod;
  }
  bool compar(Node *w, int st, int dr) {
    if (st == dr) return hash_val > w->hash_val;
    if (left->hash_val == w->left->hash_val)
      return right->compar(w->right, ((st + dr) >> 1) + 1, dr);
    return left->compar(w->left, st, ((st + dr) >> 1));
  }
  Node *update_range(int st, int dr, int Left, int Right, Node *zero) {
    if (Left <= st && dr <= Right) return zero;
    Node *a, *b;
    if (Left <= ((st + dr) >> 1))
      a = left->update_range(st, ((st + dr) >> 1), Left, Right, zero->left);
    else
      a = left;
    if (((st + dr) >> 1) < Right)
      b = right->update_range(((st + dr) >> 1) + 1, dr, Left, Right,
                              zero->right);
    else
      b = right;
    return new Node(a, b, dr - st);
  }
  Node *update_position(int st, int dr, int pos) {
    if (st == dr) return new Node(NULL, NULL, -1);
    if (pos <= ((st + dr) >> 1))
      return new Node(left->update_position(st, ((st + dr) >> 1), pos), right,
                      dr - st);
    else
      return new Node(
          left, right->update_position(((st + dr) >> 1) + 1, dr, pos), dr - st);
  }
  void find0(int st, int dr, int pos) {
    if (sum == 0) return;
    if (dr <= pos) {
      if (st == dr) {
        pos0 = st;
        return;
      }
      if (right->sum)
        return right->find0(((st + dr) >> 1) + 1, dr, pos);
      else
        return left->find0(st, ((st + dr) >> 1), pos);
    }
    if (((st + dr) >> 1) < pos) {
      right->find0(((st + dr) >> 1) + 1, dr, pos);
      if (pos0) return;
    }
    left->find0(st, ((st + dr) >> 1), pos);
  }
  Node() { left = right = NULL; }
  bool smaller(Node *t);
  void build(int st, int dr, int v) {
    if (st == dr) {
      sum = hash_val = v;
      return;
    }
    left = new Node();
    right = new Node();
    left->build(st, ((st + dr) >> 1), v);
    right->build(((st + dr) >> 1) + 1, dr, v);
    sum = left->sum + right->sum;
    hash_val =
        ((long long)left->hash_val * pw[(dr - st + 1) / 2] + right->hash_val) %
        Mod;
  }
  void find_number() {
    if (!left)
      answer = (answer * 2 + 1 - sum) % Mod;
    else
      left->find_number(), right->find_number();
  }
} * dist[Nmax], *full0, *full1;
Node *add(Node *t, int w) {
  pos0 = 0;
  w = digits - w;
  t->find0(1, digits, w);
  Node *res;
  res = t->update_position(1, digits, pos0);
  if (pos0 < w) res = res->update_range(1, digits, pos0 + 1, w, full0);
  return res;
}
bool Node ::smaller(Node *t) {
  if (!left) return hash_val > t->hash_val;
  if (left->hash_val == t->left->hash_val) return right->smaller(t->right);
  return left->smaller(t->left);
}
class MyCmp {
 public:
  bool operator()(pair<Node *, int> A, pair<Node *, int> B) {
    if (A.first->hash_val == B.first->hash_val) return A.second < B.second;
    return !A.first->compar(B.first, 1, digits);
  }
};
void run_dijkstra() {
  cin >> n >> m;
  while (m--) {
    cin >> x >> y >> c;
    v[x].push_back({y, c});
    v[y].push_back({x, c});
  }
  cin >> start >> finish;
  for (i = 1; i <= n; ++i) dist[i] = full1;
  priority_queue<pair<Node *, int>, vector<pair<Node *, int> >, MyCmp> q;
  dist[finish] = full0;
  int node = finish;
  q.push({dist[finish], finish});
  while (q.size()) {
    node = q.top().second;
    if (node == start) break;
    q.pop();
    if (expanded[node]) continue;
    expanded[node] = 1;
    for (auto it : v[node])
      if (!expanded[it.first]) {
        Node *s = add(dist[node], it.second);
        if (s->smaller(dist[it.first])) {
          q.push({s, it.first});
          dist[it.first] = s;
          come[it.first] = node;
        }
      }
  }
}
void print_path() {
  if (start == finish) {
    cout << 0 << '\n' << 1 << '\n' << start << '\n';
    return;
  }
  if (!come[start]) {
    cout << -1 << '\n';
    return;
  }
  answer = 0;
  dist[start]->find_number();
  cout << answer << '\n';
  vector<int> ans;
  while (start != finish) {
    ans.push_back(start);
    start = come[start];
  }
  ans.push_back(finish);
  cout << ans.size() << '\n';
  for (auto it : ans) cout << it << ' ';
}
int main() {
  cin.sync_with_stdio(false);
  pw[0] = 1;
  for (i = 1; i <= digits / 2 + 5; ++i) pw[i] = pw[i - 1] * 2 % Mod;
  full0 = new Node();
  full1 = new Node();
  full0->build(1, digits, 1);
  full1->build(1, digits, 0);
  run_dijkstra();
  print_path();
  return 0;
}
