#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  int n;
  string s;
  cin >> s;
  n = s.size();
  vector<int> C(n, -1), D(n, -1);
  stack<int> S;
  for (int i = 0; i < n; i++) {
    if (s[i] == '(')
      S.push(i);
    else {
      if (!S.empty()) {
        int p = S.top();
        S.pop();
        C[i] = p;
        D[i] = i - p + 1;
        if (p - 1 >= 0 && D[p - 1] != -1) D[i] += D[p - 1];
      }
    }
  }
  int maxi = -1, am = 0;
  for (int i = 0; i < n; i++)
    if (D[i] > maxi)
      maxi = D[i], am = 1;
    else if (D[i] == maxi)
      am++;
  if (maxi == -1)
    cout << "0 1" << endl;
  else
    cout << maxi << " " << am << endl;
  return 0;
}
