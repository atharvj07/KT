#include<bits/stdc++.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
typedef long long int int64;

typedef struct sushi{
  int t,d;
} node;

int cmpSushi(const void *a,const void *b){
  return -(((node *)a)->d-((node *)b)->d);
}

void run(void){
  int n,k;
  scanf("%d%d",&n,&k);
  node *a=(node *)calloc(n,sizeof(node));
  int i;
  for(i=0;i<n;i++) cin >> a[i].t >> a[i].d;
  qsort(a,n,sizeof(node),cmpSushi);
  int *used=(int *)calloc(n+1,sizeof(int));
  int *stack=(int *)calloc(n,sizeof(int));
  int top=0;
  int cnt=0;
  int64 sum=0;
  for(i=0;i<k;i++){
    sum+=a[i].d;
    if(used[a[i].t]){
      stack[top++]=a[i].d;
    } else {
      used[a[i].t]=1;
      cnt++;
    }
  }
  int64 max=sum+(int64)cnt*cnt;
  for(i=k;i<n && top>0;i++){
    if(used[a[i].t]) continue;
    used[a[i].t]=1;
    sum+=a[i].d-stack[--top];
    cnt++;
    if(max<sum+(int64)cnt*cnt) max=sum+(int64)cnt*cnt;
  }
  cout << max << endl;
}
int main(){
  run();
  return 0;
}