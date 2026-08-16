#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const long long MAXN = 1e18 + 7;
const int maxn = 500000 + 10;
stack<char> st;
int main() {
  ios::sync_with_stdio(false);
  string s;
  cin >> s;
  st.push(s[0]);
  int n = s.size();
  for (int i = 1; i < n; i++) {
    if (st.empty()) {
      st.push(s[i]);
      continue;
    }
    if (st.top() == s[i])
      st.pop();
    else
      st.push(s[i]);
  }
  if (st.size() < 1)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  return 0;
}
