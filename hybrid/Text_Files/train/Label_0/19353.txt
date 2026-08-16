#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;

int N,prime[10010],k,f;

int main(){
  for(int i=1;i<=10000;i++){
    prime[i]=0;
  }///初期化
  prime[2]=1;
  for(int i=3;i<=10000;i++){
    f=2;
    while(i % f != 0){f++;};
    if(f==i){prime[i]=1;}
  };///素数判定
  while(scanf("%d",&N)==1){
    k=0;
    for(int i=1;i<=N;i++)
      {
	if(prime[i]==1&&prime[N-i+1]==1){
	  k++;}
      };
    printf("%d\n",k);
  }

}