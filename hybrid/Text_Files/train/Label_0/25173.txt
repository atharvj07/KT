#include<iostream>
using namespace std;
const int Maxv=100005;
int fa[Maxv];

int find(int x){
	if(fa[x]!=x) fa[x]=find(fa[x]);
	return fa[x];
}

bool visited[Maxv];
int main()
{
	int n,m,i,j,x,y,z;
	cin>>n>>m;
	
	for(i=1;i<=n;i++) fa[i]=i;
	
	for(i=1;i<=m;i++){
		cin>>x>>y>>z;
		if(find(x)!=find(y))
			fa[find(y)]=find(x);
	}
	
	int ans=0;
	for(i=1;i<=n;i++)
		if(!visited[find(i)]){
			ans++;visited[find(i)]=true;
		}
	cout<<ans;
	return 0;
}