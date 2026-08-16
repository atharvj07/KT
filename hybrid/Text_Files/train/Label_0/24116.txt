#include <cstdio>
#include <algorithm>
using namespace std;
long long int knapsack[51][3000]={};
long long int ans=0;
int main(){
	int n,a,t;
	knapsack[0][0]=1;
	scanf("%d %d",&n,&a);
	for(int i=1;i<=n;i++){
		scanf("%d",&t);
		for(int k=i-1;k>=0;k--){
			for(int j=2500;j>=t;j--){
				knapsack[k+1][j]+=knapsack[k][j-t];
			}
		}
	}
	for(int i=1;i<=n;i++)
		ans+=knapsack[i][a*i];
	printf("%lld",ans);
}