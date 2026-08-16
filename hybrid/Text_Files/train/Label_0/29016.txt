#include <bits/stdc++.h>
using namespace std;
int dp[1000005][2];
int main() {
  string s;
  int l, c, i;
  cin >> s;
  stack<int> st;
  for (i = 0; s[i]; i++) {
    if (s[i] == '(') {
      st.push(i);
      dp[i][0] = dp[i][1] = -1;
    } else if (st.empty())
      dp[i][0] = dp[i][1] = -1;
    else {
      dp[i][0] = dp[i][1] = st.top();
      st.pop();
      if (dp[i][0] > 0 && dp[dp[i][0] - 1][1] >= 0)
        dp[i][1] = dp[dp[i][0] - 1][1];
    }
  }
  for (i = l = 0; s[i]; i++)
    if (dp[i][1] >= 0) l = max(l, i - dp[i][1] + 1);
  if (l == 0)
    cout << "0 1";
  else {
    for (i = c = 0; s[i]; i++)
      if (dp[i][1] >= 0 && i - dp[i][1] + 1 == l) c++;
    cout << l << " " << c;
  }
  return 0;
}
