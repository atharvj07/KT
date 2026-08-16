#include <stdio.h>

typedef long long lli;

int a[200000], b[200000], n;

int main() {
	scanf("%d",&n);
	bool found=false;
	lli sum=0, mn=(1<<30);
	for(int i=0;i<n;i++) {
		scanf("%d %d",&a[i],&b[i]);
		if(a[i]!=b[i]) found=true;
		sum+=a[i];
		if(a[i]>b[i] && b[i]<mn) mn=b[i];
	}
	if(!found) {
		puts("0");
		return 0;
	}
	printf("%lld\n",sum-mn);
	return 0;
}