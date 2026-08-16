#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    stack<char> st;
    string s;
    cin >> s;
    for (int i = 0; i < s.length(); i++) {
      if (!st.empty() && st.top() == 'B' && s[i] == 'B')
        st.pop();
      else if (!st.empty() && st.top() == 'A' && s[i] == 'B')
        st.pop();
      else {
        st.push(s[i]);
      }
    }
    cout << st.size() << endl;
  }
}
