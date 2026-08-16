#include <bits/stdc++.h>
using namespace std;
const long long N = 1e5 + 5;
long long arr[N], A[N], ARR[N];
bool visited[N] = {};
long long cnt[N] = {};
bool f;
int main() {
  int n, ans = 0;
  string s;
  set<char> st;
  cin >> n >> s;
  for (int i = 0; i < n; ++i) {
    if (s[i] < 'a') {
      ans = max(ans, (int)st.size());
      st.clear();
    } else
      st.insert(s[i]);
  }
  cout << max(ans, (int)st.size());
  return 0;
}
