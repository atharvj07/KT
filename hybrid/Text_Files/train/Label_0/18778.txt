#include <bits/stdc++.h>
const long long mod = 1000000007L;
using namespace std;
string s;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> s;
  int n = s.size();
  int ans = n + 1;
  int low = 1, high = n + 1;
  while (low <= high) {
    int mid = (low + high) / 2;
    int last = -1, val = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' ||
          s[i] == 'U' || s[i] == 'Y') {
        val = max(val, i - last);
        last = i;
      }
    }
    val = max(val, n - last);
    if (val <= mid) {
      ans = mid;
      high = mid - 1;
    } else
      low = mid + 1;
  }
  cout << ans << endl;
  return 0;
}
