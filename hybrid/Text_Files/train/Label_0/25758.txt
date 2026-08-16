#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 7;
int n, k;
char s[N];
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n >> k;
  for (int i = 0; i < n; ++i) {
    cin >> s[i];
  }
  vector<int> arr;
  for (int i = 0; i < n; ++i) {
    if (s[i] == s[(i - 1 + n) % n] || s[i] == s[(i + 1) % n]) {
      arr.push_back(i - n);
      arr.push_back(i);
      arr.push_back(i + n);
    }
  }
  sort(arr.begin(), arr.end());
  if (arr.empty()) {
    for (int i = 0; i < n; ++i) {
      cout << (s[i] == 'B' ^ k % 2 ? 'B' : 'W');
    }
    cout << '\n';
  } else {
    for (int i = 0; i < n; ++i) {
      auto it = lower_bound(arr.begin(), arr.end(), i);
      int r = *it;
      int l = *--it;
      if (i - l > k && r - i > k) {
        cout << (s[i] == 'B' ^ k % 2 ? 'B' : 'W');
      } else if (i - l < r - i) {
        cout << s[(l + n) % n];
      } else {
        cout << s[(r + n) % n];
      }
    }
    cout << '\n';
  }
  return 0;
}
