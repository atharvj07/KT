#include <bits/stdc++.h>
using namespace std;
struct node {
  long long x, y;
  bool operator<(const node &a) const { return x < a.x; }
} T[200005];
signed main() {
  long long n;
  cin >> n;
  for (long long i = 0; i < n; i++) {
    node &a = T[i];
    cin >> a.x;
  }
  for (long long i = 0; i < n; i++) {
    node &a = T[i];
    cin >> a.y;
  }
  sort(T, T + n);
  multiset<long long> st;
  long long now = -1, ans = 0, sum = 0;
  long long mx;
  for (long long i = 0; i < n; i++) {
    while (st.size() && now < T[i].x) {
      mx = *st.rbegin();
      ans += sum - mx;
      sum -= mx;
      now++;
      st.erase(st.find(mx));
    }
    sum += T[i].y;
    st.insert(T[i].y);
    now = T[i].x;
  }
  while (st.size()) {
    mx = *st.rbegin();
    ans += sum - mx;
    sum -= mx;
    st.erase(st.find(mx));
  }
  cout << ans << endl;
}
