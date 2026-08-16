#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,n) for(int i=1;i<=n;i++)
typedef long long ll;

int main(){
	ll h,w,m;
	cin >> h >> w >> m;
	map<pair<int,int>, int> bomb;
	vector<ll> r(h);
	vector<ll> c(w);
	rep(i,m){
		int a,b;
		cin >> a >> b;
		a--;b--;
		bomb[make_pair(a,b)]++;
		r[a]++;
		c[b]++;
	}
	vector<int> r_index, c_index;
	ll r_max = *max_element(r.begin(), r.end());
	ll c_max = *max_element(c.begin(), c.end());
	rep(i,h) if(r_max == r[i]) r_index.push_back(i);
	rep(i,w) if(c_max == c[i]) c_index.push_back(i);
	ll ans = r_max + c_max;
	rep(i,r_index.size()){
		rep(j,c_index.size()){
			if(bomb[make_pair(r_index[i], c_index[j])] == 0){
				cout << ans << endl;
				return 0;
			}
		}
	}
	cout << ans - 1 << endl;
    return 0;
}

