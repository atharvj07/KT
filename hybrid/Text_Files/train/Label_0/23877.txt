#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cstring>
#include <functional>
#include <cmath>
#include <complex>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define rep1(i,n) for(int i=1;i<=(n);++i)
#define all(c) (c).begin(),(c).end()
#define fs first
#define sc second
#define pb push_back
#define show(x) cout << #x << " " << x << endl
#define chmax(x,y) x=max(x,y)
#define chmin(x,y) x=min(x,y)
typedef pair<int,int> P;
int A,B,W,N;
int dp[2][10001];
vector<P> vc;
int dm(){
	int a=1,b=1,ret=2e9;
	while(a<=W&&dp[0][a]<0) a++;
	while(b<=W&&dp[1][b]<0) b++;
	while(a<=W&&b<=W){
		chmin(ret,abs(a-b));
		if(a<=b){
			a++;
			while(a<=W&&dp[0][a]<0) a++;
		}else{
			b++;
			while(b<=W&&dp[1][b]<0) b++;
		}
	}
	return ret;
}
int dc(int l,int r){
	return vc[r].fs-vc[l].fs;
}
int main(){
	cin>>A>>B>>W;
	rep(i,A){
		int a,b;
		cin>>a>>b;
		vc.pb(P(b,a));
	}
	rep(i,B){
		int a,b;
		cin>>a>>b;
		vc.pb(P(b,-a));
	}
	sort(all(vc));
	rep(j,2) rep(i,W+1) dp[j][i]=-1;
	int N=A+B,ans=2e9,n[2]={},l=0,r=0;
	for(;l<N;l++){
		for(;r<N;r++){
			if(n[0]==0||n[1]==0||dm()>=dc(l,r-1)){
				int id=0,c=vc[r].fs,w=vc[r].sc;
				if(w<0) id=1,w=-w;
				n[id]++;
				for(int i=W;i>w;i--){
					if(dp[id][i-w]>=0) chmax(dp[id][i],dp[id][i-w]);
				}
				dp[id][w]=r;
				if(n[0]&&n[1]){
					chmin(ans,max(dm(),dc(l,r)));
//					printf("(l,r)=%d,%d\n",l,r);
//					show(ans);
				}
			}else{
				break;
			}
		}
		int id=0,c=vc[l].fs,w=vc[l].sc;
		if(w<0) id=1,w=-w;
		n[id]--;
		rep(i,W+1){
			if(dp[id][i]==l) dp[id][i]=-1;
		}
//		printf("l,r,n0,n1= %d,%d,%d,%d\n",l,r,n[0],n[1]);
		if(n[0]&&n[1]){
			chmin(ans,max(dm(),dc(l+1,r-1)));
//			printf("(l,r)=%d,%d\n",l+1,r-1);
//			show(ans);
		}
	}
	cout<<ans<<endl;
}