#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

#define P 10007
#define modp(x) ((((x)%P)+P)%P)

int fac[40];

int calc2(int n,int a,int b,int c,int d){
	vector<int> hoge(n+1);
	hoge[0]=1;
	for(int t=0;t<a;t++){
		for(int i=n;i>=0;i--){
			if(i>=1)hoge[i]=modp(hoge[i]+4*hoge[i-1]);
			if(i>=2)hoge[i]=modp(hoge[i]+2*hoge[i-2]);
		}
	}
	for(int t=0;t<b;t++){
		for(int i=n;i>=0;i--){
			if(i>=1)hoge[i]=modp(hoge[i]+2*hoge[i-1]);
		}
	}
	for(int t=0;t<c;t++){
		for(int i=n;i>=0;i--){
			if(i>=1)hoge[i]=modp(hoge[i]+2*hoge[i-1]);
		}
	}
	for(int t=0;t<d;t++){
		for(int i=n;i>=0;i--){
			if(i>=1)hoge[i]=modp(hoge[i]+hoge[i-1]);
		}
	}
	int ret=0;
	for(int i=0;i<=n;i++){
		ret=modp(ret+fac[n-i]*hoge[i]*(i%2==0?1:-1));
	}
	return ret;
}

int calc(int n,vector<pair<int,int> > ng){
	int k=ng.size();
	int ret=0;
	for(int b=0;b<(1<<k);b++){
		bool collide=false;
		for(int i=0;i<k;i++)for(int j=0;j<k;j++)if(i!=j && (b&(1<<i))!=0 && (b&(1<<j))!=0 && (ng[i].first==ng[j].first || ng[i].second==ng[j].second))collide=true;
		if(collide)continue;
		for(int d=0;d<4;d++){
			int sn=((__builtin_popcount(b)+__builtin_popcount(d))%2==0)?1:-1;
			bool ok=true;
			if(d&1){
				for(int i=0;i<k;i++)if((b&(1<<i))!=0 && ng[i].first==ng[i].second)ok=false;
			}
			if(d&2){
				for(int i=0;i<k;i++)if((b&(1<<i))!=0 && ng[i].first==n-1-ng[i].second)ok=false;
			}
			if(ok){
				vector<int> row(n),col(n);
				for(int i=0;i<k;i++)if((b&(1<<i))!=0)row[ng[i].first]=col[ng[i].second]=1;
				//calculate parameters
				int m=n-__builtin_popcount(b),p=0,q=0,r=0,s=0;
				if(d==1){
					for(int i=0;i<n;i++)if(row[i]==0&&col[i]==0)s++;
				}
				if(d==2){
					for(int i=0;i<n;i++)if(row[i]==0&&col[n-1-i]==0)s++;
				}
				if(d==3){
					for(int i=0;i<n-1-i;i++){
						if(row[i]+row[n-1-i]==0 && col[i]+col[n-1-i]==0)p++;
						if(row[i]+row[n-1-i]==0 && col[i]+col[n-1-i]==1)q++;
						if(row[i]+row[n-1-i]==1 && col[i]+col[n-1-i]==0)r++;
						if(row[i]+row[n-1-i]==1 && col[i]+col[n-1-i]==1)s++;
						
					}
					if((n-1)%2==0 && row[(n-1)/2]==0 && col[(n-1)/2]==0)s++;
				}
				ret=modp(ret+sn*calc2(m,p,q,r,s));
			}
		}
	}
	return ret;
}

int main(){
	fac[0]=1;for(int i=1;i<40;i++)fac[i]=modp(fac[i-1]*i);
	int n,k;
	scanf("%d%d",&n,&k);
	vector<pair<int,int> > ng(k);
	for(int i=0;i<k;i++)scanf("%d%d",&ng[i].first,&ng[i].second);
	printf("%d\n",calc(n,ng));
}