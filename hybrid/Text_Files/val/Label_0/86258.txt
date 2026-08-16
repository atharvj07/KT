#include <bits/stdc++.h>
#define int long long
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
template<class S,class T> ostream& operator<<(ostream& o,const pair<S,T> &p){return o<<"("<<p.fs<<","<<p.sc<<")";}
template<class T> ostream& operator<<(ostream& o,const vector<T> &vc){o<<"sz = "<<vc.size()<<endl<<"[";for(const T& v:vc) o<<v<<",";o<<"]";return o;}
using ll = long long;
const int K = 7;
vector<ll> ps = {2,3,5,7,11,13,17};
int Q;
ll m[299],mp[299];
ll x[299];

ll q[K];

ll ans;

void dfs(int t){
	if(t==K){
		ll tmp = 0;
		ll LCM = 1;
		vector<int> xx(301);
		rep(i,K) LCM *= q[i];
		rep(i,Q){
			if(LCM%m[i]!=0){
				//exclude
			}else{
				if(mp[i]==1){
					//include
					tmp += x[i];
				}else{
					xx[mp[i]] += x[i];
				}
			}
		}
		rep(i,301) tmp +=max(0LL,xx[i]);
		chmax(ans,tmp);
		return;
	}
	for(ll a=1;a<=300;a*=ps[t]){
		q[t] = a;
		dfs(t+1);
	}
}

signed main(){
	cin>>Q;
	rep(i,Q){
		cin>>m[i]>>x[i];
		mp[i] = 1;
		rep(j,K){
			int p = ps[j];
			while(m[i]%p==0){
				m[i]/=p;
				mp[i]*=p;
			}
		}
		swap(m[i],mp[i]);
	}
	dfs(0);
	cout<<ans<<endl;
}
