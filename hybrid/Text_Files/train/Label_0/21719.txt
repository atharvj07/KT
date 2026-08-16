#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  int ip[m];
  int a = 0;
  long long suffix_sum[m];
  long long sum = 0;
  for (auto i = 0; i < m; i++) {
    cin >> ip[i];
    if (n - ip[i] < i) a = 1;
    sum += ip[i];
  }
  if (sum < n || a == 1) {
    cout << -1 << endl;
    return 0;
  }
  suffix_sum[m - 1] = ip[m - 1];
  for (int i = m - 2; i >= 0; i--) {
    suffix_sum[i] = suffix_sum[i + 1] + ip[i];
  }
  for (long long int i = 0; i < m; i++) {
    a = max(i + 1, n - suffix_sum[i] + 1);
    cout << a << " ";
  }
  cout << endl;
}
