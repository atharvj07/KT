#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
const string space=" ";
int main(){
	while(1){
		int n,l,r;
		cin>>n>>l>>r;
		if(!n)break;
		int a[n];
		rep(i,n)cin>>a[i];
		int ans=0;
		REP(i,l,r){
			int j;
			for(j=0;j<n;j++){
				if(i%a[j]==0){
					if(j%2==0)ans++;
					break;
				}
			}
			if(j==n&&n%2==0)ans++;
		}
		cout<<ans<<endl;
	}
	return 0;
}
