#include <bits/stdc++.h>
using namespace std;
const int maxn = 3e5 + 2;
struct ques {
  int id, l, r, d, u;
} Q[maxn];
long long ans[maxn];
int p[maxn], last;
bool cmp1(ques A, ques B) { return A.d < B.d; }
bool cmp2(ques A, ques B) { return A.u < B.u; }
int n, m;
int tr[maxn];
int lowbit(int x) { return (x & (-x)); }
void add(int x) {
  if (x == 0) return;
  for (int i = x; i <= n; i += lowbit(i)) {
    tr[i]++;
  }
}
long long query(int x) {
  long long ans = 0;
  for (int i = x; i >= 1; i -= lowbit(i)) {
    ans += tr[i];
  }
  return ans;
}
long long calc(int x) {
  return max(0LL, ((long long)x * ((long long)x - 1) / 2));
}
int main() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%d", &x);
    p[x] = i;
  }
  for (int i = 1; i <= m; i++) {
    scanf("%d%d%d%d", &Q[i].l, &Q[i].d, &Q[i].r, &Q[i].u);
    if (Q[i].l > Q[i].r) swap(Q[i].l, Q[i].r);
    if (Q[i].d > Q[i].u) swap(Q[i].d, Q[i].u);
    Q[i].id = i;
    ans[Q[i].id] = (long long)n * ((long long)n - 1) / 2 - calc(Q[i].d - 1) -
                   calc(n - Q[i].r) - calc(Q[i].l - 1) - calc(n - Q[i].u);
  }
  sort(Q + 1, Q + 1 + m, cmp1);
  last = 1;
  for (int i = 1; i <= m; i++) {
    for (int j = last; j < Q[i].d; j++) {
      add(p[j]);
    }
    long long num1 = query(Q[i].l - 1), num2 = query(n) - query(Q[i].r);
    ans[Q[i].id] += (num1 * (num1 - 1) / 2) + (num2 * (num2 - 1) / 2);
    last = Q[i].d;
  }
  memset(tr, 0, sizeof(tr));
  sort(Q + 1, Q + 1 + m, cmp2);
  last = n;
  for (int i = m; i >= 1; i--) {
    for (int j = last; j > Q[i].u; j--) {
      add(p[j]);
    }
    long long num1 = query(Q[i].l - 1), num2 = query(n) - query(Q[i].r);
    ans[Q[i].id] += (num1 * (num1 - 1) / 2) + (num2 * (num2 - 1) / 2);
    last = Q[i].u;
  }
  for (int i = 1; i <= m; i++) {
    printf("%lld\n", ans[i]);
  }
  return 0;
}
