#include<stdio.h>
#include<algorithm>
#include<cmath>
#define rep(i,j) for(int i=0;i<(j);i++)
#define reps(i,j,k) for(int i=j;i<=k;i++)

using namespace std;

typedef pair<int,int> pii;

int main(){
	int n,d,m,s[100002],k[10000];
	for(;;){
		scanf("%d",&d);
		if(d==0)break;
		scanf("%d%d",&n,&m);
		s[0]=0;
		rep(i,n-1)scanf("%d",s+i+1);
		rep(i,m)scanf("%d",k+i);
		sort(s,s+n);
		s[n]=d;
		s[n+1]=d+1;
		sort(k,k+m);
		int cnt=0,p=0,t=2000000000,temp;
		rep(i,m){
			temp=t;
			for(;p<n+2;p++){
				int x=abs(k[i]-s[p]);
				if(temp>x)temp=x;
				if(temp!=x){
					cnt += temp;
					p--;
					break;
				}
			}
		}
		printf("%d\n",cnt);
	}
	return 0;
}