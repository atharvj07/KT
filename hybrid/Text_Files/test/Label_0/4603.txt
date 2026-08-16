#include <bits/stdc++.h>
using namespace std;
int n;
int main() {
  ios_base::sync_with_stdio(0);
  cin >> n;
  vector<int> ans;
  if (n == 1) {
    cout << "2\n1 1";
    return 0;
  }
  for (int i = 2; i <= n; i += 2) ans.push_back(i);
  for (int i = 1; i <= n; i += 2) ans.push_back(i);
  for (int i = 2; i <= n; i += 2) ans.push_back(i);
  cout << ans.size() << endl;
  for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
  return 0;
}
