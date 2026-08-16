#include <bits/stdc++.h>
using namespace std;
inline long long read() {
  long long sum = 0, ff = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') ff = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') sum = sum * 10 + ch - '0', ch = getchar();
  return sum * ff;
}
const long long N = 2e5 + 7;
long long n, a[28][N], b[N], cnt[27], tr[N], ans;
char s[N], t[N];
inline long long lowbit(long long x) { return x & (-x); }
void modify(long long x) {
  for (; x <= n; x += lowbit(x)) tr[x]++;
}
long long ask(long long x) {
  long long sum = 0;
  for (; x; x -= lowbit(x)) sum += tr[x];
  return sum;
}
signed main() {
  n = read();
  for (long long i = 1; i <= n; i++) cin >> s[i], t[n - i + 1] = s[i];
  for (long long i = 1; i <= n; i++)
    a[t[i] - 'a' + 1][++cnt[t[i] - 'a' + 1]] = i;
  memset(cnt, 0, sizeof(cnt));
  for (long long i = 1; i <= n; i++)
    b[i] = a[s[i] - 'a' + 1][++cnt[s[i] - 'a' + 1]];
  for (long long i = n; i >= 1; i--) modify(b[i]), ans += ask(b[i] - 1);
  cout << ans;
  return 0;
}
