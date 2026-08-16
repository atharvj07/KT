#include<bits/stdc++.h>
using namespace std;
int main(){
	int n,m;scanf("%d%d",&n,&m);
	int l=n/2,r=l+1;
	if(n&1)for(int i=0;i<m;i++)printf("%d %d\n",l--,r++);
	else{
		for(int i=0;i<(m+1)/2;i++)printf("%d %d\n",l--,r++);
		l=2,r=n;
		for(int i=(m+1)/2;i<m;i++)printf("%d %d\n",l++,r--);
	}
	return 0;
}
