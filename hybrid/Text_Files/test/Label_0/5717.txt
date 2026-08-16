#include <bits/stdc++.h>
using namespace std;
const int N=100005;
int n,a[N];
int Ha[N];
int main(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
		scanf("%d",&a[i]),Ha[i]=a[i];
	sort(Ha+1,Ha+n+1);
	int tot=0;
	for (int i=1;i<=n;i++){
		a[i]=lower_bound(Ha+1,Ha+n+1,a[i])-Ha;
		if ((a[i]^i)&1)
			tot++;
	}
	printf("%d",tot/2);
	return 0;
}