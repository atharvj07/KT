#include <bits/stdc++.h>
#define INF 1e9
using namespace std;
int n,arr[101];
int cal(int a,int b){return (arr[a]+arr[b])*(abs(a-b));}
void Min(int &a,int b){a=min(a,b);}

int mem[3][101][101][101];
int dfs(int f,int num,int l,int r){
  if(l>r)return 0;
  if(l==r)return (arr[l]==l+1) ? INF:0;
  if(r-l==1)return (arr[l]==l+1||arr[r]==r+1)? cal(l,r):0;
  if(mem[f][num][l][r]!=-1)return mem[f][num][l][r];

  int res=INF;  
  for(int i=l+1;i<r;i++){
    if((f==0||f==1)&&arr[i]!=l+1){
      swap(arr[l],arr[i]);
      Min(res,cal(l,i)+dfs(0,0,l+1,i-1)+dfs(1,arr[i],i,r));
      swap(arr[l],arr[i]);
      }

    if((f==0||f==2)&&arr[i]!=r+1){
      swap(arr[i],arr[r]);
      Min(res,cal(i,r)+dfs(2,arr[i],l,i)+dfs(0,0,i+1,r-1));
      swap(arr[i],arr[r]);
    }
  }

  for(int i=l;i<r;i++){
    if(f==1)Min(res,dfs(1,num,l,i)+dfs(0,0,i+1,r));
    else if(f==2)Min(res,dfs(0,0,l,i)+dfs(2,num,i+1,r));
    else Min(res,dfs(0,0,l,i)+dfs(0,0,i+1,r));
  }

  return mem[f][num][l][r]=res;
}

int main(){
  cin>>n;
  for(int i=0;i<n;i++)cin>>arr[i];
  memset(mem,-1,sizeof(mem));
  cout<<dfs(0,0,0,n-1)<<endl;
}