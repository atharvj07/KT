#include<bits/stdc++.h>
using namespace std;
int w,h,dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
string a[51];
bool used[51][51];
int dfs(int y,int x){
  if(y==-1||y==h||x==-1||x==w||used[y][x])return 0;
  if(a[y][x]=='B')return 1;
  if(a[y][x]=='W')return 2;
  used[y][x]=1;
  int pr=0;
  for(int t,i=0;i<4;i++){
    t=dfs(y+dy[i],x+dx[i]);
    if(!pr)pr=t;
    else if(t&&pr!=t)pr=3;
  }
  return pr;
}

int main(){
  while(cin>>w>>h,w){
    for(int i=0;i<h;i++)cin>>a[i];
    int ans[5]={};
    for(int i=0;i<h;i++)
      for(int j=0;j<w;j++){  
	memset(used,0,sizeof(used));
	if(a[i][j]=='.')ans[dfs(i,j)]++;
      }
    cout<<ans[1]<<" "<<ans[2]<<endl;
  }
  return 0;
}