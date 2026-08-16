#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	int n,a[100000],i,p[5001],cnt=0,x,c=0,flg,y;
	scanf("%d",&n);
	for(i=0;i<n;i++) scanf("%d",&a[i]);
	sort(a,a+n);
	for(i=1;i<=a[n-1];i++){
		if(a[n-1]%i==0) p[c]=i,c++;
	}
	//for(i=0;i<c;i++) printf("%d\n",p[i]);
	y=0; i=0;
	while(1){
		if(i==n) break;
		if(a[i]>p[y]) y++;
		else {
			cnt+=p[y]-a[i];
			i++;
		}
	}
	printf("%d\n",cnt);
	return 0;
}
