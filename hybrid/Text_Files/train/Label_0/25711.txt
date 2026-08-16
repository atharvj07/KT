#include <bits/stdc++.h>
using namespace std;
static const int INF = 0x3f3f3f3f;
static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
template <typename T, typename U>
static void amin(T &x, U y) {
  if (y < x) x = y;
}
template <typename T, typename U>
static void amax(T &x, U y) {
  if (x < y) x = y;
}
int main() {
  int minl = -1e9;
  int maxr = 1e9;
  int n;
  cin >> n;
  vector<int> a(n), ba(n);
  for (int(i) = 0; (i) < (int)(n); ++(i)) cin >> (a[i]);
  ;
  for (int i = 0; i < n; i++) {
    char c;
    cin >> c;
    ba[i] = c - '0';
  }
  int i = 4;
  int sost = 0;
  while (i < n) {
    if (ba[i] == 1) {
      if (!sost) {
        int cur = -INF;
        for (int j = i - 4; j <= i; j++) cur = max(cur, a[j] + 1);
        minl = max(minl, cur);
        sost = 1;
        i += 4;
        continue;
      } else {
        i++;
      }
    } else {
      if (sost) {
        int cur = INF;
        for (int j = i - 4; j <= i; j++) cur = min(cur, a[j] - 1);
        maxr = min(maxr, cur);
        sost = 0;
        i += 4;
        continue;
      } else {
        i++;
      }
    }
  }
  cout << minl << ' ' << maxr << endl;
  return 0;
}
