#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
const int mod = 1e9 + 7;
const int P = 1e9 + 7;
const int N = 2e7;
const int maxn = 1e6 + 5;
long long n, m;
long long xx, yy;
struct node {
  long long x;
  long long r;
  long long pos;
  long long ans;
} s[10005];
bool judge(int x, int y, int p) {
  if (p < 0 || p >= n) return false;
  if (s[p].ans != -1) return false;
  if ((s[p].x - x) * (s[p].x - x) + y * y <= s[p].r * s[p].r) return true;
  return false;
}
bool cmp1(node a, node b) { return a.x < b.x; }
bool cmp2(node a, node b) { return a.pos < b.pos; }
int main() {
  ios::sync_with_stdio(false);
  cin >> n;
  for (long long i = 0; i < n; ++i)
    cin >> s[i].x >> s[i].r, s[i].pos = i + 1, s[i].ans = -1;
  sort(s, s + n, cmp1);
  cin >> m;
  long long temp = 0;
  for (long long i = 0; i < m; ++i) {
    cin >> xx >> yy;
    long long l = 0, r = n - 1;
    while (l <= r) {
      long long mid = (l + r) / 2;
      if (s[mid].x > xx)
        r = mid - 1;
      else
        l = mid + 1;
    }
    if (judge(xx, yy, l - 1)) s[l - 1].ans = i + 1, temp++;
    if (judge(xx, yy, l)) s[l].ans = i + 1, temp++;
    if (judge(xx, yy, l + 1)) s[l + 1].ans = i + 1, temp++;
  }
  sort(s, s + n, cmp2);
  cout << temp << endl;
  for (long long i = 0; i < n; ++i) cout << s[i].ans << " ";
  cout << endl;
}
