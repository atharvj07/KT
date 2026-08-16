#include<bits/stdc++.h>
#define ll long long
using namespace std;
struct Info{ll nu;int we;}a[1000010];
struct edg{int x,y;}an[1000010];
bool c=true;
int n,si[1000010];
ll su;
bool comp(const Info &a,const Info &b){return a.nu>b.nu;}
bool comp1(const Info &a,const Info &b){return a.we<b.we;}
int find(ll x){
	int l=1,r=n,mid;
	while (l+1<r){
		mid=(l+r)/2;
		if (a[mid].nu<x) r=mid;else l=mid;
	}
	if (a[r].nu==x) return r;
	if (a[l].nu==x) return l;
	return 0;
}
int main(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++){cin>>a[i].nu;a[i].we=i;}
	sort(a+1,a+n+1,comp);
	for (int i=1;i<=n;i++) si[i]=1;
	for (int i=1;i<n;i++){
		int x=find(a[i].nu-n+si[i]*2);
		if (x==0) c=false;
		else{
			si[x]+=si[i];
			an[i].x=a[i].we;an[i].y=a[x].we;
		}
		su+=si[i];
	}
	if (su!=a[n].nu)c=false;
	sort(a+1,a+n+1,comp1);
	if (c){
		for (int i=1;i<n;i++) cout<<an[i].x<<' '<<an[i].y<<endl;
	}else{
		cout<<"-1"<<endl;
	}
	return 0;
}