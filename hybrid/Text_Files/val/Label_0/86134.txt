#include <iostream>
#include <cmath>
using namespace std;

int N,K,H[100010],dp[200010] = {0};

int main(){
	cin >> N >> K;
	for(int i=1;i<=N;i++){
		cin >> H[i];
		dp[i] = 2e9;
	}
	dp[1] = 0;
	for(int i=1;i<N;i++){
		for(int j=1;j<=K;j++){
			dp[i+j] = min(dp[i+j],dp[i]+abs(H[i]-H[i+j]));
		}
	}
	cout << dp[N] << endl;
}