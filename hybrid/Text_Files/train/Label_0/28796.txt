#include <bits/stdc++.h>
using namespace std;
int genre[20], sum[20];
int main() {
  int n, m, i, j;
  cin >> n >> m;
  for (i = 0; i < n; i++) {
    cin >> j;
    genre[j]++;
  }
  int s = 0;
  sum[1] = genre[1];
  for (i = 2; i <= m; i++) {
    sum[i] += (sum[i - 1] + genre[i]);
  }
  for (i = 1; i < m; i++) {
    s = s + genre[i] * (sum[m] - sum[i]);
  }
  cout << s << endl;
  return 0;
}
