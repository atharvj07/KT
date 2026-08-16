#include <bits/stdc++.h>
using namespace std;
void icchhipadey() {
  long long t;
  cin >> t;
  while (t--) {
    long long n, k;
    cin >> n >> k;
    long long l = 1;
    long long r = n;
    long long ans = n - 2;
    while (l <= r) {
      long long mid = l + (r - l) / 2;
      long long xx = mid * (mid + 1);
      xx /= 2;
      if (xx >= k) {
        ans = mid;
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
    long long yy = ans - 1;
    yy = yy * (yy + 1);
    yy /= 2;
    yy = k - yy;
    ans++;
    string s = "";
    for (int i = 1; i <= n; i++) {
      if (i == ans || i == yy) {
        s += "b";
      } else {
        s += "a";
      }
    }
    reverse(s.begin(), s.end());
    cout << s << endl;
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  icchhipadey();
}
