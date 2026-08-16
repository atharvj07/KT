#include <bits/stdc++.h>
const int MOD = 1E9 + 7;
const int N = 3000000 + 5;
const int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
const int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
using namespace std;
int tot, f[N], X[N], Y[N], a[N], len, seq[N];
int n, m;
int father[N];
char str[N], c;
int get(int x) {
  int l = 1;
  seq[1] = x;
  for (; f[seq[l]]; l++) seq[l + 1] = f[seq[l]];
  for (int i = 1; i < l; i++) f[seq[i]] = seq[l];
  return seq[l];
}
int getPos(int x) {
  if (!tot) return x;
  int i = 1, last;
  if (x < X[a[i]]) return x;
  x -= X[a[i]] - 1;
  for (last = i++; i <= tot; i++)
    if (X[a[i]] > Y[a[last]]) {
      if (x > X[a[i]] - Y[a[last]] - 1) {
        x -= X[a[i]] - Y[a[last]] - 1;
        last = i;
      } else
        return Y[a[last]] + x;
    }
  return Y[a[last]] + x;
}
struct Query {
  int right;
  int left;
} query[N];
int main() {
  scanf("%s", str + 1);
  scanf("%d%d", &m, &n);
  for (int i = 0; i < n; i++) scanf("%d%d", &query[i].left, &query[i].right);
  memset(f, 0, sizeof(f));
  memset(father, 0, sizeof(father));
  for (int i = n - 1; i >= 0; i--)
    if (query[i].right < m) {
      int pos = getPos(query[i].right + 1);
      if (pos <= m) {
        int k = query[i].left + 1;
        if (k > query[i].right) k = query[i].left;
        int newPos = getPos(k), lim = (query[i].right << 1) - query[i].left + 1,
            j;
        X[i] = pos;
        for (j = query[i].right + 1; j <= lim && pos <= m;
             j++, pos = get(pos)) {
          father[pos] = newPos;
          f[pos] = pos + 1;
          k += 2;
          if (k <= query[i].right)
            newPos = get(get(newPos + 1) + 1);
          else {
            k = query[i].left;
            newPos = getPos(k);
          }
          Y[i] = pos;
        }
        for (j = tot; j && X[a[j]] > X[i]; j--) a[j + 1] = a[j];
        a[j + 1] = i;
        tot++;
      }
    }
  int cnt = 0;
  for (int i = 1; i <= m; i++) {
    father[i] = (!father[i]) ? ++cnt : father[father[i]];
    printf("%c", str[father[i]]);
  }
  printf("\n");
  return 0;
}
