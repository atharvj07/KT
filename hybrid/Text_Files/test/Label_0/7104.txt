#include <bits/stdc++.h>
using namespace std;
struct state {
  int t, f;
};
state tree[2 * (1 << 17)];
int s[100010], f[100010], t[100010], l[100010], r[100010], b[100010];
map<int, int> t_id;
vector<pair<int, int> > tf;
map<pair<int, int>, int> tf_pos;
vector<pair<pair<pair<int, int>, pair<int, int> >, int> > query;
int ans[100010];
void update(int f, int t) {
  int id = (1 << 17) + tf_pos[make_pair(t, f)];
  tree[id].t = t;
  tree[id].f = f;
  while (id > 1) {
    id /= 2;
    tree[id].t = max(tree[id * 2].t, tree[id * 2 + 1].t);
    tree[id].f = max(tree[id * 2].f, tree[id * 2 + 1].f);
  }
}
int func(int r, int b, int id = 1, int L = 0, int R = (1 << 17)) {
  if (tree[id].t < b || tree[id].f < r) return -1;
  if (id >= (1 << 17)) return t_id[tree[id].t];
  int tmp = func(r, b, 2 * id, L, (L + R) / 2);
  if (tmp != -1) return tmp;
  return func(r, b, 2 * id + 1, (L + R) / 2, R);
}
int main(void) {
  int N, Q, i;
  scanf("%d%d", &N, &Q);
  for ((i) = 0; (i) < (int)(N); (i)++) scanf("%d%d%d", &s[i], &f[i], &t[i]);
  for ((i) = 0; (i) < (int)(Q); (i)++) scanf("%d%d%d", &l[i], &r[i], &b[i]);
  for ((i) = 0; (i) < (int)(N); (i)++) t_id[t[i]] = i + 1;
  for ((i) = 0; (i) < (int)(N); (i)++) tf.push_back(make_pair(t[i], f[i]));
  sort(tf.begin(), tf.end());
  for ((i) = 0; (i) < (int)(N); (i)++) tf_pos[tf[i]] = i;
  for ((i) = 0; (i) < (int)(N); (i)++)
    query.push_back(
        make_pair(make_pair(make_pair(s[i], 0), make_pair(f[i], t[i])), i));
  for ((i) = 0; (i) < (int)(Q); (i)++)
    query.push_back(
        make_pair(make_pair(make_pair(l[i], 1), make_pair(r[i], b[i])), i));
  sort(query.begin(), query.end());
  for ((i) = 0; (i) < (int)(2 * (1 << 17)); (i)++) tree[i].t = tree[i].f = 0;
  for ((i) = 0; (i) < (int)(N + Q); (i)++) {
    if (query[i].first.first.second == 0) {
      update(query[i].first.second.first, query[i].first.second.second);
    } else {
      ans[query[i].second] =
          func(query[i].first.second.first, query[i].first.second.second);
    }
  }
  for ((i) = 0; (i) < (int)(Q); (i)++) printf("%d\n", ans[i]);
  return 0;
}
