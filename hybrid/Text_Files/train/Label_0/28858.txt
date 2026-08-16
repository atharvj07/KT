#include <bits/stdc++.h>
#define rep(i,a,n) for(int i=a;i<n;i++)
#define all(a) a.begin(),a.end()
#define o(a) cout<<a<<endl
#define int long long
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

void out(int st,int now,int &cnt){
	if(cnt!=0) cout<<" ";
	if(st!=now) cout<<st<<"-"<<now;
	else cout<<st;
	cnt++;
	//cout<<" "<<cnt;
}

signed main(){
	int n;
	while(cin>>n && n!=0){
		vi d(n+1);
		rep(i,0,n) cin>>d[i];
		d[n]=1e9;
		int cnt=0,st=d[0];
		rep(i,1,n+1){
			if(d[i]!=d[i-1]+1){
				out(st,d[i-1],cnt);
				st=d[i];
				//cnt++;
			}
		}
		cout<<endl;
	}
}