#include<bits/stdc++.h>
using namespace std;
const int N=2005;
int n,a[N],sum;
bitset<N*N> dp;
int main(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++)scanf("%d",&a[i]),sum+=a[i];
	dp[0]=1;
	for (int i=1;i<=n;i++)dp|=dp<<a[i];
	for (int i=(sum+1)/2;i;i++)
		if (dp[i]){
			printf("%d\n",i);
			return 0;
		}
}