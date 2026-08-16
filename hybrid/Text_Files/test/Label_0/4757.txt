#include <bits/stdc++.h>
using namespace std;
vector<long long> b;
void solve() {
  b.push_back(1);
  b.push_back(2);
  long long val = 4;
  for (int i = 2; i < 33; i++) {
    b.push_back(val);
    val = val * 2;
  }
  return;
}
int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  solve();
  map<int, int> mp;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    mp[a[i]]++;
  }
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    int val = a[i];
    int flag = 0;
    for (int j = 1; j < 33; j++) {
      if (val > b[j])
        continue;
      else {
        int temp = b[j] - val;
        if (val == temp && mp[temp] > 1) {
          flag = 1;
          break;
        } else if (val != temp && mp[temp] > 0) {
          flag = 1;
          break;
        }
      }
    }
    if (flag)
      continue;
    else
      cnt++;
  }
  cout << cnt << endl;
  return 0;
}
