#include<bits/stdc++.h>
#define MOD 1000000007LL
using namespace std;

typedef long long ll;
typedef pair<int,int> P;

int n,w,h;
int x[101];
int xi[101];

int main(void){
	scanf("%d%d%d",&n,&h,&w);
	for(int i=0;i<n;i++){
		scanf("%d",&x[i]);
	}
	for(int i=0;i<n;i++){
		xi[i]=i*w;
		if(i%2==0){
			xi[i]+=x[i];
		}else{
			xi[i]-=x[i];
		}
	}
	int ans=0;
	xi[n]=(n*w);
	sort(xi,xi+n);
	for(int i=0;i<n;i++){
		ans+=max(0,xi[i+1]-xi[i]-w);
	}
	ans+=xi[0];
	printf("%d\n",ans*h);
	return 0;
}