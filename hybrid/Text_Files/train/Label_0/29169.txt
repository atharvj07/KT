#include <bits/stdc++.h>
using namespace std;
const int INF = ~(1 << 31);
const double eps = 1e-6;
const long double PI = 3.1415926535;
const int MOD = 1e9 + 7;
int n, m;
int main() {
  string s;
  cin >> s;
  stack<int> st;
  for (int(i) = 0; (i) < (s.size()); ++(i)) {
    int g = s[i] == '+';
    if (st.size() && st.top() == g)
      st.pop();
    else
      st.push(g);
  }
  if (st.size() == 0)
    puts("Yes");
  else
    puts("No");
  return 0;
}
