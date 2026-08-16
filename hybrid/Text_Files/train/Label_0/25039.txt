#include <bits/stdc++.h>
using namespace std;
double max(double a, double b) {
  if (a > b) return a;
  return b;
}
double min(double a, double b) {
  if (a > b) return b;
  return a;
}
bool comp(string a, string b) { return a.size() < b.size(); }
using namespace std;
const int N = 200005;
int a[N];
int main() {
  int n, k;
  cin >> n >> k;
  for (int i = 1; i <= n; i++) cin >> a[i];
  sort(a + 1, a + n + 1);
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    int pos = upper_bound(a + 1, a + n + 1, a[i]) - a;
    if (pos > n || a[pos] > a[i] + k) ans++;
  }
  printf("%d\n", ans);
}
