#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e6 + 9;
set<int> ist;
map<string, int> msi;
map<string, string> mss;
map<int, string> mis;
map<int, int> mii;
pair<int, int> pii;
vector<int> v;
vector<pair<int, int> > vv;
int cc[] = {1, -1, 0, 0};
int rr[] = {0, 0, 1, -1};
void SUNRISE() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    char dp[n][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        cin >> dp[i][j];
      }
    }
    if ((dp[0][1] == dp[1][0]) && (dp[n - 1][n - 2] == dp[n - 2][n - 1]) &&
        (dp[0][1] != dp[n - 1][n - 2])) {
      cout << 0 << endl;
    } else if ((dp[0][1] == dp[1][0]) &&
               (dp[n - 1][n - 2] == dp[n - 2][n - 1]) &&
               (dp[0][1] == dp[n - 1][n - 2])) {
      cout << 2 << endl;
      cout << 1 << " " << 2 << endl;
      cout << 2 << " " << 1 << endl;
    } else if ((dp[0][1] != dp[1][0]) &&
               (dp[n - 1][n - 2] != dp[n - 2][n - 1])) {
      cout << 2 << endl;
      if (dp[0][1] == '0') {
        cout << 1 << " " << 2 << endl;
      } else {
        cout << 2 << " " << 1 << endl;
      }
      if (dp[n - 1][n - 2] == '1') {
        cout << n << " " << n - 1 << endl;
      } else {
        cout << n - 1 << " " << n << endl;
      }
    } else {
      if (dp[0][1] == dp[1][0]) {
        if (dp[n - 1][n - 2] == dp[0][1]) {
          cout << 1 << endl;
          cout << n << " " << n - 1 << endl;
        } else {
          cout << 1 << endl;
          cout << n - 1 << " " << n << endl;
        }
      } else {
        if (dp[n - 1][n - 2] == dp[0][1]) {
          cout << 1 << endl;
          cout << 1 << " " << 2 << endl;
        } else {
          cout << 1 << endl;
          cout << 2 << " " << 1 << endl;
        }
      }
    }
  }
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  SUNRISE();
  return 0;
}
