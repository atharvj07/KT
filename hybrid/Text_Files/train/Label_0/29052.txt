#include<cstdio>
#include<iostream>
using namespace std;
int a[200001],b[200001],c[200001];
int main(void){
	int n,m,k,root[100001],size[100001],bu[100001],i,j,gyo,x,y;
	cin>>n>>m>>k;
	for(i=1;i<=n;i++){
		root[i]=i; size[i]=1; bu[i]=0;
	}
	for(i=1;i<=k;i++) cin>>a[i]>>b[i]>>c[i];
	gyo=0;
	for(i=1;i<=k;i++){
		if(a[i]==1){
			x=root[b[i]]; y=root[c[i]];
			while(root[x]!=x) x=root[x];
			while(root[y]!=y) y=root[y];
			if(bu[x]!=bu[y]&&bu[x]!=0&&bu[y]!=0){
//				cout<<"1 "<<i<<endl;
				gyo=i;
				break;
			}
			else if(x!=y){
				if(size[x]>size[y]){
					root[y]=x;
					if(bu[y]!=0) bu[x]=bu[y];
				}
				else if(size[x]<size[y]){
					root[x]=y;
					if(bu[x]!=0) bu[y]=bu[x];
				}
				else {
					root[x]=y;
					size[y]++;
					if(bu[x]!=0) bu[y]=bu[x];
				}
			}
		}
		if(a[i]==2){
			x=root[b[i]];
			while(root[x]!=x) x=root[x];
			if(bu[x]==0) bu[x]=c[i];
			else if(bu[x]!=c[i]){
//				cout<<"2 "<<i<<endl;
				gyo=i;
				break;
			}
		}
	}
	cout<<gyo<<endl;
	return 0;
}