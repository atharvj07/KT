#include <bits/stdc++.h>
using namespace std;
int T, N;
signed main() {
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> N;
    vector<int> P(N);
    for (int n = 0; n < N; n++) cin >> P[n];
    int found = false;
    for (int n = 0; n < N - 1; n++)
      if (P[n + 1] > P[n] && P[n + 1] - P[n] > 1) {
        found = true;
        break;
      }
    cout << (found ? "No" : "Yes") << endl;
  }
}
