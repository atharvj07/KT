#define _USE_MATH_DEFINES
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<climits>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<stack>
#include<functional>
using namespace std;
typedef long long ll;
const ll MOD = 1e9+7;

ll dp[2][5000];

int main(){
	int N,L,X[5000],A[5000];
	cin>>N>>L;
	for(int i=0;i<N;i++) cin>>X[i];
	for(int i=0;i<N;i++){
		cin>>A[i];
	}
	for(int i=0;i<N;i++){
		for(int j=0;X[i]+A[i]*j<L;j++){
			dp[i&1][X[i]+A[i]*j] = 1;
			if(A[i]==0) break;
		}
		if(i==0) continue;
		ll sum = 0;
		for(int j=0;j<L;j++){
			dp[i&1][j] = (dp[i&1][j]*sum)%MOD;
			sum += dp[(i-1)&1][j]%MOD;
			dp[(i-1)&1][j] = 0;
		}
	}
	ll ans = 0;
	for(int i=0;i<L;i++) ans += dp[(N-1)&1][i]%MOD;
	printf("%lld\n",ans%MOD);
	return 0;
}