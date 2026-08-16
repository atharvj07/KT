#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long n, ans;
  cin >> n;
  ans = (n * (n - 1)) >> 1;
  string s;
  cin >> s;
  vector<int> A, B;
  for (int i = 0; i < int(n); i++) {
    if (s[i] == 'A')
      A.push_back(i);
    else
      B.push_back(i);
  }
  for (int i = 0; i < int(n - 1); i++) {
    if (s[i] == 'A') {
      if (s[i + 1] == 'A') {
        auto it = lower_bound(B.begin(), B.end(), i + 1);
        if (it != B.end()) ans--;
      } else {
        for (int j = i + 1; j < n && s[j] == 'B'; j++) ans--;
      }
    } else {
      if (s[i + 1] == 'A') {
        for (int j = i + 1; j < n && s[j] == 'A'; j++) ans--;
      } else {
        auto it = lower_bound(A.begin(), A.end(), i + 1);
        if (it != A.end()) ans--;
      }
    }
  }
  cout << ans << endl;
}
