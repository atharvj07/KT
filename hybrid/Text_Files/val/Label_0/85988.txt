#include <bits/stdc++.h>
using namespace std;
int T,n,m,k,q,a[100010];
int gcd(int x,int y){
	return y?gcd(y,x%y):x;
}
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++) scanf("%d",&a[i]);
	int cur=0,o_cnt,e_cnt,pos;
	bool flag;
	while(true){
		o_cnt=e_cnt=flag=0,pos=-1;
		for(int i=1;i<=n;i++){
			if(a[i]%2==0) o_cnt++;
			else pos=i,e_cnt++;
			if(a[i]==1) flag=true;
		}
		if(flag) return puts((o_cnt&1)^cur?"First":"Second"),0;
		if(o_cnt&1) return puts(cur?"Second":"First"),0;
		if(e_cnt>1&&!(o_cnt&1)) return puts(cur?"First":"Second"),0;
		cur^=1;
		a[pos]--;
		int g=a[1];
		for(int i=2;i<=n;i++) g=gcd(a[i],g);
		for(int i=1;i<=n;i++) a[i]/=g;
	}
}
