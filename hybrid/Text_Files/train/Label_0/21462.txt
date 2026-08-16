#include <bits/stdc++.h>
using namespace std;
int n, d[500005], b[10000005], mn, x, mx, sum;
bool a[10000005];
pair<int, int> p[500005];
int main() {
  cin >> n;
  for (int i = 2; i <= 4000; i++) {
    if (b[i] == 0)
      for (long long j = i * i; j <= 1e7; j += i) {
        if (b[j] == 0) b[j] = i;
      }
  }
  for (int i = 1; i <= n; i++) {
    cin >> d[i];
    p[i].first = 1;
    p[i].second = 1;
    x = d[i];
    sum = 0;
    while (d[i] != 1) {
      if (b[d[i]] == 0) b[d[i]] = d[i];
      if (a[b[d[i]]] == 0) {
        p[i].first *= b[d[i]];
        sum++;
      }
      mn = b[d[i]];
      a[b[d[i]]] = 1;
      d[i] /= b[d[i]];
    }
    while (x != 1) {
      a[b[x]] = 0;
      x /= b[x];
    }
    if (sum == 1) {
      p[i].first = -1;
      p[i].second = -1;
    } else {
      p[i].first /= mn;
      p[i].second = mn;
    }
  }
  for (int i = 1; i <= n; i++) {
    cout << p[i].first << " ";
  }
  cout << endl;
  for (int i = 1; i <= n; i++) {
    cout << p[i].second << " ";
  }
}
