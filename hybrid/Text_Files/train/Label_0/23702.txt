#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct query {
  int l, r, block, id;
};
const int N = 200000, Q = 200000;
int n, m, a[N], freq[1000001];
query q[Q];
ll ans[Q];
bool by_block(const query &a, const query &b) {
  if (a.block != b.block) return a.block < b.block;
  return a.r > b.r;
}
int main() {
  scanf("%d %d", &n, &m);
  int bsize = (int)sqrt(n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &q[i].l, &q[i].r);
    q[i].l--;
    q[i].block = q[i].l / bsize;
    q[i].id = i;
  }
  sort(q, q + m, by_block);
  int curr_l = 0, curr_r = 0;
  ll curr_ans = 0;
  for (int i = 0; i < m; i++) {
    int l = q[i].l, r = q[i].r;
    while (curr_l < l) {
      curr_ans += (ll)(1 - 2 * freq[a[curr_l]]) * a[curr_l];
      freq[a[curr_l]]--;
      curr_l++;
    }
    while (curr_l > l) {
      curr_ans += (ll)(1 + 2 * freq[a[curr_l - 1]]) * a[curr_l - 1];
      freq[a[curr_l - 1]]++;
      curr_l--;
    }
    while (curr_r < r) {
      curr_ans += (ll)(1 + 2 * freq[a[curr_r]]) * a[curr_r];
      freq[a[curr_r]]++;
      curr_r++;
    }
    while (curr_r > r) {
      curr_ans += (ll)(1 - 2 * freq[a[curr_r - 1]]) * a[curr_r - 1];
      freq[a[curr_r - 1]]--;
      curr_r--;
    }
    ans[q[i].id] = curr_ans;
  }
  for (int i = 0; i < m; i++) {
    printf("%I64d\n", ans[i]);
  }
  return 0;
}
