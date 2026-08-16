#include <bits/stdc++.h>
using namespace std;
int check(vector<int> m, vector<int> r, int d) {
  int flag = 0;
  for (int i = 0; i < m.size(); i++) {
    if ((d % m[i] == r[i])) {
      flag = 1;
      break;
    }
  }
  if (flag == 1)
    return 1;
  else
    return 0;
}
int main() {
  int n, k, l;
  double c = 0.0;
  cin >> n;
  vector<int> m, r;
  for (int i = 0; i < n; i++) {
    cin >> k;
    m.push_back(k);
  }
  for (int i = 0; i < n; i++) {
    cin >> k;
    r.push_back(k);
  }
  for (int i = 0; i < 1000000; i++) {
    c += (double)check(m, r, i);
  }
  cout << (c / 1000000);
}
