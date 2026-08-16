#include <bits/stdc++.h>
using namespace std;
vector<int> s[110][110], answer[110];
long long dp[110][110];
long long val[110];
int arr[110];
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> arr[i];
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      dp[i][j] = arr[j];
      s[i][j].push_back(arr[j]);
    }
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = i; j <= n; ++j) {
      for (int k = 1; k <= j - 1; ++k) {
        if (dp[i - 1][k] + arr[j] > dp[i][j]) {
          dp[i][j] = dp[i - 1][k] + arr[j];
          s[i][j] = s[i - 1][k];
          s[i][j].push_back(arr[j]);
        } else if (dp[i - 1][k] + arr[j] == dp[i][j]) {
          for (int l = 0; l < s[i - 1][k].size(); ++l) {
            if (s[i - 1][k][l] < s[i][j][l]) {
              s[i][j] = s[i - 1][k];
              s[i][j].push_back(arr[j]);
              break;
            } else if (s[i - 1][k][l] > s[i][j][l]) {
              break;
            }
          }
        }
      }
      if (dp[i][j] > val[i]) {
        val[i] = dp[i][j];
        answer[i] = s[i][j];
      } else if (dp[i][j] == val[i]) {
        for (int l = 0; l < s[i][j].size(); ++l) {
          if (s[i][j][l] < answer[i][l]) {
            answer[i] = s[i][j];
            break;
          } else if (s[i][j][l] > answer[i][l]) {
            break;
          }
        }
      }
    }
  }
  int q;
  cin >> q;
  while (--q > -1) {
    int k, pos;
    cin >> k >> pos;
    cout << answer[k][pos - 1] << '\n';
  }
}
