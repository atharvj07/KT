#include<iostream>
using namespace std;
int fa[2000005];
int find(int x){
	if(fa[x]==x) return x;
	else return fa[x]=find(fa[x]);
}
void uni(int x,int y){
	int f1=find(x),f2=find(y);
	if(f1!=f2) fa[f1]=f2;
}
int n,q;
int main(){
	cin>>n>>q;
	for(int i=1;i<=n;i++) fa[i]=i;
	for(int i=1,x,u,v;i<=q;i++){
		cin>>x>>u>>v;
		if(x==0){
			uni(u,v);
		}
		else{
			if(find(u)==find(v)) cout<<1<<endl;
			else cout<<0<<endl;
		}
	}
}