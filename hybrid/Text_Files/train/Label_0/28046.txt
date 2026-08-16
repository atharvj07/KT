#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<n;i++)
#define repn(i,n) for(int i=1;i<=n;i++)
#define fi first
#define sc second
vector<int>vec;
int n,m,x;
int main(){
	cin >> n >> m >> x;
	rep(i,x){
		int a,b; cin >> a >> b;
		a = n+1-a;
		if(b <= m) a += m+1-b;
		else a += b-m;
		vec.pb(a);
	}
	sort(vec.begin(),vec.end());
	int ans = 0;
	rep(i,vec.size()) ans = max(ans,vec[i]+(int)(vec.size())-1-i);
	cout << ans << endl;
}

