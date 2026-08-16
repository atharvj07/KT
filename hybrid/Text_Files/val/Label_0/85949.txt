#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

#define ll long long
using namespace std;
ll bit[400010],a[200010],b[200010],p[100010],x[100010],y[100010],n,q,inv[300010],m;
vector<ll> v;
map<ll,ll> mp;
ll sum(ll i){
	ll s = 0;
	while(i>0){
		s += bit[i];
		i -= i&-i;
	}
	return s;
}

void add(ll i, ll x){
	while(i<=m){
		bit[i] += x;
		i += i&-i;
	}
}
int main(){
	ll z,ans=0,i;
	cin >> n >> q;
	for(i=0;i<2*n;i++){
		cin >> a[i];
	}
	for(i=0;i<2*n;i++){
		cin >> b[i];
	}
	for(i=1;i<2*n-1;i++){
		v.push_back(a[i]-b[i]);
	}
	for(i=0;i<q;i++){
		cin >> p[i] ;
		p[i]--;
		cin>> x[i] >> y[i];
		if(p[i]!=0 && p[i]!=2*n-1){
			v.push_back(x[i]-y[i]);
		}
	}
	v.push_back(0);
	sort(v.begin(),v.end());
	m = v.size()+1;
	int now = 1;
	mp[v[0]] = 1;
	inv[1] = v[0];
	if(v[0]==0){
		z = 1;
	}
	for(i=1;i<v.size();i++){
		if(v[i]>v[i-1]){
			now++;
		}
		mp[v[i]] = now;
		inv[now] = v[i];
		if(v[i]==0){
			z = now;
		}
	}
	now++;
	ll cnt = 0;
	for(i=1;i<2*n-1;i++){
		add(mp[a[i]-b[i]],1);
		if(a[i]>=b[i]){
			ans += a[i];
			cnt += 1;
		}else{
			ans += b[i];
		}
	}
	ans += a[0]+a[2*n-1];
	for(i=0;i<q;i++){
		if(p[i]==0 || p[i]==2*n-1){
			ans -= a[p[i]];
			ans += x[i];
			a[p[i]] = x[i];
			b[p[i]] = y[i];
		}else{
			ans -= max(a[p[i]],b[p[i]]);
			ans += max(x[i],y[i]);
			add(mp[a[p[i]] - b[p[i]]],-1);
			add(mp[x[i] - y[i]],1);
			if(a[p[i]]-b[p[i]]>0 ^ x[i]-y[i]>0){
				cnt++;
			}
			a[p[i]] = x[i];
			b[p[i]] = y[i];
		}
		if(cnt%2==0){
			cout << ans << endl;
		}else{
			long long l=0,r=now,mid;
			int s = sum(z);
			while(r - l>1){
				mid = (l+r)/2;
				if(sum(mid)>=s+1){
					r = mid;
				}else{
					l = mid;
				}
			}
			long long m1 = inv[r];
			l=0,r=now;
			while(r - l>1){
				mid = (l+r)/2;
				if(sum(mid)<s){
					l = mid;
				}else{
					r = mid;
				}
			}
			long long m2 = inv[r];
			cout << max(ans - m1,ans + m2) << endl;
		}
	}
}
