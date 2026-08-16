#include<bitset>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 2005
using namespace std;
bitset<N*N>f;
int main(){
	int n,x,sum=0;
	scanf("%d",&n);
	f[0]=1;
	for(int i=1;i<=n;++i){
		scanf("%d",&x);
		f|=(f<<x),sum+=x;
	}
	for(int i=(sum+1)/2;i<=sum;++i)
		if(f[i])  return printf("%d",i),0;
	return 0;
}