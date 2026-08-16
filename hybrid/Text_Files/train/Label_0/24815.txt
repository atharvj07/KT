#include <bits/stdc++.h>
using namespace std;
long long pwr(long long base, long long p, long long mod = (1000000007LL)) {
  long long ans = 1;
  while (p) {
    if (p & 1) ans = (ans * base) % mod;
    base = (base * base) % mod;
    p /= 2;
  }
  return ans;
}
long long gcd(long long a, long long b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int n, arr[100005];
bool done[100005];
vector<int> cycle;
vector<vector<int> > ans1, ans2, pending[5];
void dfs(int v) {
  if (done[v]) return;
  done[v] = true;
  cycle.push_back(v);
  dfs(arr[v]);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> arr[i];
  for (int i = 1; i <= n; i++)
    if (!done[i]) {
      cycle.clear();
      dfs(i);
      int sz = (int)cycle.size();
      if (sz == 1) continue;
      if (sz % 4 <= 1) {
        for (int s = 1; s < (int)cycle.size(); s += 4) {
          vector<int> now1, now2;
          now1.push_back(cycle[0]);
          for (int j = s; j < s + 4 && j < (int)cycle.size(); j++) {
            now1.push_back(cycle[j]);
            now2.push_back(cycle[j]);
          }
          now2.push_back(cycle[0]);
          ans1.push_back(now1);
          ans2.push_back(now2);
        }
      } else {
        int steps = sz / 4;
        for (int s = 1; s < (int)cycle.size() && steps > 0; s += 4, steps--) {
          vector<int> now1, now2;
          now1.push_back(cycle[0]);
          for (int j = s; j < s + 4 && j < (int)cycle.size(); j++) {
            now1.push_back(cycle[j]);
            now2.push_back(cycle[j]);
          }
          now2.push_back(cycle[0]);
          ans1.push_back(now1);
          ans2.push_back(now2);
        }
        vector<int> now;
        if (sz % 4 == 3) now.push_back(cycle[sz - 2]);
        now.push_back(cycle[sz - 1]);
        now.push_back(cycle[0]);
        pending[sz % 4].push_back(now);
      }
    }
  while (!pending[2].empty() && !pending[3].empty()) {
    vector<int> v2 = pending[2].back();
    pending[2].pop_back();
    vector<int> v3 = pending[3].back();
    pending[3].pop_back();
    v2.push_back(v3[0]);
    v2.push_back(v3[1]);
    v2.push_back(v3[2]);
    ans1.push_back(v2);
    v2.pop_back();
    v2.pop_back();
    v2.pop_back();
    reverse(v2.begin(), v2.end());
    v2.push_back(v3[1]);
    v2.push_back(v3[2]);
    v2.push_back(v3[0]);
    ans2.push_back(v2);
  }
  while (!pending[2].empty()) {
    vector<int> v21 = pending[2].back();
    pending[2].pop_back();
    if (pending[2].empty()) {
      ans1.push_back(v21);
      reverse(v21.begin(), v21.end());
      ans2.push_back(v21);
      break;
    }
    vector<int> v22 = pending[2].back();
    pending[2].pop_back();
    v21.push_back(v22[0]);
    v21.push_back(v22[1]);
    ans1.push_back(v21);
    v21.pop_back();
    v21.pop_back();
    reverse(v21.begin(), v21.end());
    v21.push_back(v22[1]);
    v21.push_back(v22[0]);
    ans2.push_back(v21);
  }
  while (!pending[3].empty()) {
    vector<int> v31 = pending[3].back();
    pending[3].pop_back();
    if ((int)pending[3].size() <= 1) {
      ans1.push_back(v31);
      rotate(v31.begin(), v31.begin() + 1, v31.end());
      ans2.push_back(v31);
      continue;
    }
    vector<int> v32 = pending[3].back();
    pending[3].pop_back();
    vector<int> v33 = pending[3].back();
    pending[3].pop_back();
    v31.push_back(v33[0]);
    v31.push_back(v33[1]);
    ans1.push_back(v31);
    v31.pop_back();
    v31.pop_back();
    rotate(v31.begin(), v31.begin() + 1, v31.end());
    v31.push_back(v33[1]);
    v31.push_back(v33[0]);
    ans2.push_back(v31);
    v32.push_back(v33[0]);
    v32.push_back(v33[2]);
    ans1.push_back(v32);
    v32.pop_back();
    v32.pop_back();
    rotate(v32.begin(), v32.begin() + 1, v32.end());
    v32.push_back(v33[2]);
    v32.push_back(v33[0]);
    ans2.push_back(v32);
  }
  cout << (int)ans1.size() << endl;
  for (int i = 0; i < (int)ans1.size(); i++) {
    cout << (int)ans1[i].size() << endl;
    for (auto it : ans1[i]) cout << it << " ";
    cout << endl;
    for (auto it : ans2[i]) cout << it << " ";
    cout << endl;
  }
  return 0;
}
