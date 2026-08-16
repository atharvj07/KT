#include <cstdio>
#include <cstring>
using namespace std;

int a[200005],f[200005],n,t,p,x,k,minx;

int main(){
	scanf("%d",&t);
	for (int i=0; i<t; i++){
		scanf("%d",&n);
		memset(f,0,sizeof(f));
		p=0;
		k=0;
		for (int j=0; j<n; j++){
			scanf("%d",&x);
			if (j==0) f[x]--;
			if (j==n-1) f[x]--;
			if (x!=p){
				f[x]++;
				a[++k]=x;
			}
			p=x;
		}
		minx=f[a[1]];
		for (int j=2; j<=k; j++)
			if (f[a[j]]<minx) minx=f[a[j]];
		printf("%d\n",minx+1);
	}
	return 0;
}
