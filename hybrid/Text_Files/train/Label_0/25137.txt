#include <bits/stdc++.h>
using namespace std;
int main() {
  int tes, n, m;
  cin >> tes;
  while (tes--) {
    cin >> n >> m;
    vector<vector<int>> dp(n, vector<int>(m));
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++) {
        cin >> dp[i][j];
        if ((i + j) % 2 == 0 and dp[i][j] % 2 != 0)
          dp[i][j]++;
        else if ((i + j) % 2 != 0 and dp[i][j] % 2 == 0)
          dp[i][j]++;
      }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) cout << dp[i][j] << " ";
      cout << endl;
    }
  }
}
