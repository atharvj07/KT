#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<int> > vec(n, vector<int>(m));
  vector<int> sum(m);
  string s;
  for (int i = 0; i < n; i++) {
    cin >> s;
    for (int j = 0; j < m; j++) {
      if (s[j] == '1')
        vec[i][j] = 1;
      else
        vec[i][j] = 0;
      sum[j] += vec[i][j];
    }
  }
  int count, flag = 0;
  for (int i = 0; i < n; i++) {
    count = 0;
    for (int j = 0; j < m; j++) {
      sum[j] -= vec[i][j];
      if (sum[j] >= 1) count++;
      sum[j] += vec[i][j];
    }
    if (count == m) {
      cout << "Yes\n";
      flag = 1;
      break;
    }
  }
  if (flag == 0) cout << "No\n";
}
