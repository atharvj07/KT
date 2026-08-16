#include <bits/stdc++.h>
using namespace std;
long long n, m, k, h;
long long a, b, c;
long long x, y;
long long mn = 1005;
set<long long> st;
long double ans;
int main() {
  for (int i = 0; i < 4; i++) {
    cin >> x;
    st.insert(x);
  }
  cout << 4 - st.size();
}
