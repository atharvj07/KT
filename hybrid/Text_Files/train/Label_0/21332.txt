#include <bits/stdc++.h>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define ar array

using namespace std;
typedef long long ll;
typedef pair<int, int> ii;

const int maxn = 2e5 + 5;

int N, M, suf, pref;
vector<int> add[maxn];

signed main(void)
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  #ifdef LOCAL
    freopen("A.INP", "r", stdin);
    freopen("A.OUT", "w", stdout);
  #endif // LOCAL
  cin >> N >> M;
  for(int i = 1; i <= N; ++i){
    int l, r; cin >> l >> r;
    add[l].eb(r);
  }
  priority_queue<int> pq;
  for(int i = M; i >= 1; --i){
    for(int j : add[i])
      pq.push(j);
    if(pq.size()){
      pq.pop();
      ++pref;
    }
  }
  for(int i : add[0]) pq.push(i);
  int ans = pref; suf = M;
  while(pq.size()){
    int now = pq.top(); pq.pop();
    if(now <= suf && suf > pref){
      ++ans;
      --suf;
    }
  }
  cout << N - ans;
}
