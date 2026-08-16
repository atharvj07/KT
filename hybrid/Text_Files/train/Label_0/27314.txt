#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
typedef double real;

real dp[2][17][1 << 16];
int n, m;
real p[17][17];

int main(){
	cin >> m >> n;
	for(int i = 0;i < m;i++)
		for(int j = 0;j < n;j++)
			cin >> p[i][j];
	
	
	for(int j = 0;j < 17;j++)
		for(int k = 0;k < (1<<16);k++)
			dp[n%2][j][k] = 1;

	for(int i = n-1;i >= 0;i--){
		int id = i % 2;
		for(int k = (1<<m)-1;k >= 0;k--){
			for(int j = 0;j < m;j++){
				dp[id][j][k] = 0;
				if((1<<j) & k)continue;
				dp[id][j][k] = dp[!id][j][k] * p[j][i] + dp[id][16][k | (1<<j)] * (1-p[j][i]);
			}
			dp[id][16][k] = 0;
			for(int j = 0;j < m;j++){
				dp[id][16][k] = max(dp[id][16][k], dp[id][j][k]);
			}
		}
	}

	printf("%.10lf\n", dp[0][16][0]);
	return 0;
}
