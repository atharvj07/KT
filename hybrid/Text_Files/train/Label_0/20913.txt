#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n;
  cin >> n;
  string a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  map<string, long long> D;
  vector<string> ans;
  for (long long i = n - 1; i >= 0; i--) {
    D[a[i]]++;
    if (D[a[i]] == 1) {
      ans.push_back(a[i]);
    }
  }
  long long b = ans.size();
  for (long long i = 0; i < b; i++) {
    cout << ans[i];
    if (i != b - 1) {
      cout << endl;
    }
  }
  return 0;
}
