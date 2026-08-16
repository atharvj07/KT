#include <bits/stdc++.h>
using namespace std;
struct rect {
  long long x1, y1, x2, y2;
  long long area() { return (x2 - x1) * (y2 - y1); };
};
rect c, a, b, d;
void enter() {
  cin >> a.x1 >> a.y1 >> a.x2 >> a.y2;
  cin >> b.x1 >> b.y1 >> b.x2 >> b.y2;
  cin >> c.x1 >> c.y1 >> c.x2 >> c.y2;
}
void createD() {
  d.x1 = max(b.x1, c.x1);
  d.y1 = max(b.y1, c.y1);
  d.x2 = min(b.x2, c.x2);
  d.y2 = min(b.y2, c.y2);
}
long long overlap(rect ra, rect rb) {
  long long x = max((long long)0, min(ra.x2, rb.x2) - max(ra.x1, rb.x1));
  long long y = max((long long)0, min(ra.y2, rb.y2) - max(ra.y1, rb.y1));
  return x * y;
}
void solve() {
  long long res = a.area() - overlap(a, b) - overlap(a, c);
  createD();
  if (d.area() > 0) res += overlap(d, a);
  if (res > 0)
    cout << "YES";
  else
    cout << "NO";
}
int main() {
  ios ::sync_with_stdio(0);
  cin.tie(0);
  cout << (fixed) << setprecision(9);
  enter();
  solve();
}
