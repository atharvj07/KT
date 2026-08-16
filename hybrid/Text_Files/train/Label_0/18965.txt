#include <bits/stdc++.h>
using namespace std;
const int N = 100009;
int n;
bool is[N];
vector<int> odd, ans;
int main() {
  while (cin >> n) {
    memset(is, true, sizeof(is));
    odd.clear();
    ans.clear();
    for (int i = 2; i <= n / 2 + 1; ++i) {
      if (is[i]) {
        odd.push_back(i);
        for (int j = i + i; j <= n; j += i) is[j] = false;
      }
    }
    memset(is, true, sizeof(is));
    for (int i = odd.size() - 1; i >= 0; --i) {
      int cnt = 0;
      for (int j = odd[i]; j <= n; j += odd[i]) {
        if (is[j]) cnt++;
      }
      if (cnt == 0 || cnt == 1) continue;
      if (cnt % 2 == 0) {
        for (int j = odd[i]; j <= n; j += odd[i]) {
          if (!is[j]) continue;
          is[j] = false;
          ans.push_back(j);
        }
      } else {
        for (int j = odd[i]; j <= n; j += odd[i]) {
          if (j == odd[i] * 2 || !is[j]) continue;
          is[j] = false;
          ans.push_back(j);
        }
      }
    }
    cout << ans.size() / 2 << endl;
    for (int i = 0; i < ans.size(); ++i) {
      if (i % 2 == 0)
        cout << ans[i] << " ";
      else
        cout << ans[i] << endl;
    }
  }
  return 0;
}
