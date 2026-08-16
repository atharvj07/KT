#include <bits/stdc++.h>

#define fast_inp_out() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define ll long long
using namespace std;

ll dp[1001][1001];
ll mod = pow(10,9)+7;

ll madd(ll a,ll b) {
	return ((a%mod)+(b%mod))%mod;
}

ll msub(ll a,ll b){
	return ((a%mod) - (b%mod) + mod)%mod;
}

// ll solve(int i,int k) {
    
//         if(i==0) {
// 			dp[i][k] = 1;
// 			return 1;
// 		}
		
// 		if(k==1) {
// 			dp[i][k] = 1;
// 			return 1;
// 		}

// 		if(dp[i][k]!=-1) {
// 			return dp[i][k];
// 		}
		
// 		ll ans = 0;
		
// 		for(int x=0;x<=i-1;x++) {
// 			ans = madd(ans,solve(n-i+x,k-1));
// 		}
		
// 		ans = madd(ans,1);
		
// 		dp[i][k] = ans;
// 		return ans;
// }

void solve_bottom_up(int n,int k){

	for(int x=0;x<=k;x++){
		dp[0][x] = 1;
	}

	for(int x=0;x<=n;x++){
		dp[x][1] = 1;
	}

	for(int x=2;x<=k;x++){
		
		ll pre[n+2];
		pre[0] = 0;

		for(int i=1;i<=n+1;i++){
			pre[i] = madd(pre[i-1], dp[i-1][x-1]);
		}
		

		for(int y=1;y<=n;y++){
			dp[y][x] = madd(1,dp[y][x]);
			
			int end = n-1;
			int start = n-y;

			dp[y][x] = madd(dp[y][x],msub(pre[end+1],pre[start]));
		}
	}

}

// int N;

// ll solve(int n,int k,int d){

// 	if(k==1){
// 		return 1;
// 	}

// 	if(n==0 && d==0){
// 		dp[n][k][d] = 1;
// 		return 1;
// 	}

// 	if(n==N+1 && d==1){
// 		return 1;
// 	}

// 	if(dp[n][k][d]!=-1){
// 		return dp[n][k][d];
// 	}

// 	ll ans = madd(solve(n-1,k-1,1-d), solve(n+1,k,d)); 	

// 	dp[n][k][d] = ans;

// 	return ans;

// }

signed main(){

    fast_inp_out();

    int t;

    cin >> t;

    for(int i=0;i<t;i++){
        int n,k;
        cin >> n >> k;

        memset(dp,0,sizeof(dp));

        solve_bottom_up(n,k);

        cout << dp[n][k] << "\n";

    }

    return 0;
}
