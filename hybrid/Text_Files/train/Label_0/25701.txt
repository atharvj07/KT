#include <bits/stdc++.h>
using namespace std;
long long i, j, k;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  long long n;
  cin >> n;
  vector<long long> count(n + 1, 0);
  for (i = (0); i < (n - 1); i++) {
    long long a, b;
    cin >> a >> b;
    if (b != n) {
      cout << "NO" << '\n';
      return 0;
    }
    count[a]++;
  }
  long long curr = 0;
  for (i = (1); i < (n + 1); i++) {
    curr += count[i];
    if (curr > i) {
      cout << "NO" << '\n';
      return 0;
    }
  }
  vector<long long> ans(n, -1);
  curr = 0;
  vector<bool> visited(n + 1, false);
  for (i = (1); i < (n); i++) {
    if (count[i] != 0) {
      visited[i] = true;
      ans[curr] = i;
      curr += count[i];
    }
  }
  curr = 1;
  for (i = (0); i < (n); i++) {
    if (ans[i] == -1) {
      while (visited[curr] && curr <= n) {
        curr++;
      }
      visited[curr] = true;
      ans[i] = curr;
    }
  }
  cout << "YES" << '\n';
  for (j = (0); j < (n - 1); j++) cout << ans[j] << " " << ans[j + 1] << '\n';
  return 0;
}
