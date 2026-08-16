#include <bits/stdc++.h>
using namespace std;
using ll = long long;
template <class T, class U>
using Pa = pair<T, U>;
template <class T>
using vec = vector<T>;
template <class T>
using vvec = vector<vec<T>>;
int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  int N;
  cin >> N;
  vec<ll> A(N);
  for (int i = 0; i < N; i++) cin >> A[i];
  stack<Pa<ll, ll>> st;
  st.push({A[0], 1});
  for (int i = 1; i < N; i++) {
    Pa<ll, ll> now = {A[i], 1};
    while (!st.empty()) {
      Pa<ll, ll> pre = st.top();
      if (pre.first * now.second > now.first * pre.second) {
        st.pop();
        now = {pre.first + now.first, pre.second + now.second};
      } else
        break;
    }
    st.push(now);
  }
  vec<double> ans;
  while (!st.empty()) {
    Pa<ll, ll> now = st.top();
    st.pop();
    for (int i = 0; i < now.second; i++)
      ans.push_back(1.0 * now.first / now.second);
  }
  reverse(ans.begin(), ans.end());
  for (auto& x : ans) cout << fixed << setprecision(10) << x << "\n";
}
