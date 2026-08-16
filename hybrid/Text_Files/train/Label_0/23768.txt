#include <bits/stdc++.h>
using namespace std;
 
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using ll = long long;
using P = pair<ll, int>;
 
#define INF 1001001001
#define MAX 1000005

int main() {
  int h, w;
  cin >> h >> w;

  map<int,int> sp;
  multiset<int> diff;
  rep(i,w) sp[i]=i,diff.insert(0);

  vector<int> ans;
  rep(i,h) {
    int a, b; cin >> a >> b; a--, b--;
    int m = -1;
    auto itr = sp.lower_bound(a);
    while (itr != sp.end() && itr->first <= b+1) {
      m = max(m,itr->second);
      diff.erase(diff.find(itr->first-itr->second));
      itr = sp.erase(itr);
    }
    if (m != -1 && b < w-1) {
      sp[b+1] = m;
      diff.insert(b+1-sp[b+1]);
    }
    ans.push_back(diff.empty()?-1:*diff.begin()+i+1);
  }
  for (auto a : ans) cout << a << endl;

  return 0;
}