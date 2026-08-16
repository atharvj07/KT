#include <bits/stdc++.h>
using namespace std;

const int INF = 1e+9;

using P = pair<int,int>;
int n,k,t,ans;
set<int> st[200010];
vector<P> on[200010],off[200010];

int calc(int x){
	return (st[x].size() == 2 && *(st[x - 1].begin()) < *(st[x].begin()))
	+ (st[x + 1].size() == 2 && *(st[x].begin()) < *(st[x + 1].begin()));
}

signed main(){
	cin >> n >> k >> t;
	for(int i = 0;i < t;i++){
		int l,r,x;
		cin >> l >> r >> x; l--;r--;
		on[l].emplace_back(i,x);
		off[r].emplace_back(i,x);
	}
	st[0].insert(-1);
	for(int i = 0;i <= k + 1;i++) st[i].insert(INF);
	int cnt = 0;
	for(int i = 0;i < n;i++){
		for(P p : on[i]){
			cnt -= calc(p.second);
			st[p.second].insert(p.first);
			cnt += calc(p.second);
		}
		if(cnt == k) ans++;
		for(P p : off[i]){
			cnt -= calc(p.second);
			st[p.second].erase(p.first);
			cnt += calc(p.second);
		}
	}
	cout << ans << endl;
}
