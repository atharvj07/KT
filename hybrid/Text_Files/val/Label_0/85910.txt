#include <bits/stdc++.h>
using namespace std;
int32_t main() {
  int t;
  cin >> t;
  set<string> st;
  st.insert("ABSINTH");
  st.insert("BEER");
  st.insert("BRANDY");
  st.insert("CHAMPAGNE");
  st.insert("GIN");
  st.insert("RUM");
  st.insert("SAKE");
  st.insert("TEQUILA");
  st.insert("VODKA");
  st.insert("WHISKEY");
  st.insert("WINE");
  string a;
  int n, count = 0;
  while (t--) {
    cin >> a;
    if (a[0] >= '0' && a[0] <= '9') {
      n = stoi(a);
      if (n <= 17) count++;
    } else {
      if (st.find(a) != st.end()) {
        count++;
      }
    }
  }
  cout << count << "\n";
  return 0;
}
