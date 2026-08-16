#include <bits/stdc++.h>
using namespace std;
map<int, pair<int, int> > a;
int p[100010], n, k;
void solve() {
  scanf("%d%d", &n, &k);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &p[i]);
    pair<int, int> t = a[p[i]];
    int an = t.first, rr = t.second;
    int l = max(max(1, i - k), rr + 1), r = min(n, i + k);
    an += r - l + 1;
    rr = r;
    a[i] = make_pair(an, rr);
    cout << an << " ";
  }
}
int main() { solve(); }
