#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
struct Pr{
	ll x,y;
}l_r[210000],r_l[210000];
 
struct Te{
	int ls,rs,lv,rv;
}t[210000];
 
int n;
ll mid;
vector<Pr>V[210000];
 
void insert(int x,Pr y){
	//x sorted
	//compare y is ok
	int i=V[x].size()-1;
	if(V[x].empty()){V[x].push_back(y);return;}
	if(V[x][i].y<=y.y)return;
	while(!V[x].empty()&&V[x][i].x>=y.x)V[x].pop_back();
	V[x].push_back(y);
}
 
int dfs(int u){
	V[u].clear();
	int i,j,ltor=0,rtol=0,dt=t[u].lv+t[u].rv;
	int ls=t[u].ls,rs=t[u].rs,lv=t[u].lv,rv=t[u].rv;
	if(t[u].ls==0){
		insert(u,(Pr){0,0});
		return 1;
	}int jud=dfs(t[u].ls)&&dfs(t[u].rs);
	if(jud==0)return 0;
	//stay x/ y\
	//using combine
	for(i=V[ls].size()-1,j=V[rs].size()-1;i>=0;i--)
	{
		while(j>=0&&V[ls][i].y+V[rs][j].x+dt>mid) j--;
		if(j>=0) l_r[++ltor]=(Pr){V[ls][i].x+lv,V[rs][j].y+rv};
	}
	for(i=V[ls].size()-1,j=V[rs].size()-1;j>=0;j--)
	{
		while(i>=0&&V[ls][i].x+V[rs][j].y+dt>mid) i--;
		if(i>=0) r_l[++rtol]=(Pr){V[rs][j].x+rv,V[ls][i].y+lv};
	}
	reverse(l_r+1,l_r+ltor+1);
	reverse(r_l+1,r_l+rtol+1);
	i=1;j=1;
	while(i<=ltor&&j<=rtol){
		if(l_r[i].x<r_l[j].x){insert(u,l_r[i]);i++;}
		else {insert(u,r_l[j]);j++;}
	}while(i<=ltor){insert(u,l_r[i]);i++;}
	while(j<=rtol){insert(u,r_l[j]);j++;}
	return !V[u].empty();
}
 
int main(){
	int x,y;
	scanf("%d",&n);
	ll L=-1,R=17179869184ll;
	for(int i=2;i<=n;i++){
		scanf("%d %d",&x,&y);
		if(t[x].ls==0)t[x].ls=i,t[x].lv=y;
		else t[x].rs=i,t[x].rv=y;
	}while(L+1<R){
		mid=(L+R)>>1;
		if(dfs(1)){
			R=mid;
		}else L=mid;
	}printf("%lld\n",R);
	return 0;
}