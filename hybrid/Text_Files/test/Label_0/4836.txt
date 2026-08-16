#include <bits/stdc++.h>
using namespace std;
int n, k;
priority_queue<double> q;
struct Node {
  int x, y;
  double z;
  bool operator<(const Node &rhs) const {
    if (x != rhs.x) return x < rhs.x;
    if (y != rhs.y) return y < rhs.y;
    return z < rhs.z;
  }
} a[1000010];
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
int main() {
  scanf("%d%d", &n, &k);
  for (register int i = 1; i <= n; i++) {
    scanf("%d%d", &a[i].x, &a[i].y);
    a[i].z = gcd(abs(a[i].x), abs(a[i].y));
    if (a[i].z) {
      a[i].x /= a[i].z;
      a[i].y /= a[i].z;
    }
    a[i].z *= sqrt(1ll * a[i].x * a[i].x + 1ll * a[i].y * a[i].y);
  }
  sort(a + 1, a + n + 1);
  for (register int l = 1, r = 0; l <= n && r <= n; l = r + 1) {
    while (r + 1 <= n && a[r + 1].x == a[l].x && a[r + 1].y == a[l].y) r++;
    double sum = 0;
    for (register int i = l; i <= r; i++) {
      if (k - 2 * (r - i) - 1 <= 0) {
        if (k & 1) {
          q.push(sum);
        } else {
          q.push(sum - a[i].z);
        }
        sum -= 2 * a[i].z;
      } else {
        q.push(a[i].z * (k - 2 * (r - i) - 1));
      }
    }
  }
  double ans = 0;
  while (k) {
    ans += q.top();
    q.pop();
    k--;
  }
  printf("%.8lf", ans);
  return 0;
}
