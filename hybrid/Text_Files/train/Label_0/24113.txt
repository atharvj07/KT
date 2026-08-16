#include<bits/stdc++.h>
using namespace std;
const int MAXN = 50;
int n, avg, a[MAXN+5];
long long memo[MAXN+5][MAXN*MAXN+5];
int main()
{
	scanf("%d%d", &n, &avg);  
	for(int i=1; i<=n; i++)
		scanf("%d", &a[i]);
	memo[0][0] = 1;
	for(int i=1; i<=n; i++)
		for(int j=i-1; j>=0; j--)
			for(int k=0; k<=j*MAXN; k++)
				memo[j+1][k+a[i]] += memo[j][k];
	long long ans = 0;
	for(int i=1; i<=n; i++)
		ans += memo[i][i*avg];
	printf("%lld", ans);
}