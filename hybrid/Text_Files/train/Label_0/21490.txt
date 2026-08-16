#include<bits/stdc++.h>
using namespace std;
#define MAX_N 200005

typedef unsigned long long ull;
ull B=5575777;
ull C[(1<<19)];
ull po[(1<<19)];
char s[(1<<19)];
ull t[(1<<19)];


int calc(int a,int b,int l,int r){
  int L=max(a,l);
  int R=min(b,r);
  return max(0,R-L);
}

void delay(int k,int l,int r){
  if(s[k]=='\0')return;
  char ch=s[k];
  s[k]='\0';
  t[k]=C[r-l]*ch;
  if(r-l==1)return;
  s[k*2+1]=ch;
  s[k*2+2]=ch;
}

void Set(int a,int b,char ch,int k=0,int l=0,int r=(1<<18)){
  delay(k,l,r);
  if(b<=l || r<=a)return;
  if(a<=l && r<=b){
    s[k]=ch;
    t[k]=C[r-l]*ch;
    return;
  }
  if(r-l>1){
    int m=(l+r)/2;
    Set(a,b,ch,k*2+1,l,m);
    Set(a,b,ch,k*2+2,m,r);
    t[k]=t[k*2+1]*po[r-m]+t[k*2+2];
  }
}

ull Get(int a,int b,int k=0,int l=0,int r=(1<<18)){
  delay(k,l,r);
  if(b<=l || r<=a)return 0;
  if(a<=l && r<=b)return t[k];
  int m=(l+r)/2;
  ull vl=Get(a,b,k*2+1,l,m);
  ull vr=Get(a,b,k*2+2,m,r);
  return vl*po[calc(a,b,m,r)]+vr;
}

int n;
char str[MAX_N];

int main(){
  po[0]=1;
  for(int i=1;i<(1<<19);i++)po[i]=po[i-1]*B;
  C[1]=1;
  for(int i=1;i<(1<<19);i++)C[i]=C[i-1]*B+1;

  scanf("%d %s",&n,str);
  for(int i=0;i<n;i++){
    Set(i,i+1,str[i]);
  }

  int q,ax,bx,cx,dx;
  scanf("%d",&q);
  char tmp[10];
  while(q--){
    scanf("%s",tmp);
    if(tmp[0]=='s'){
      scanf("%d %d %s",&ax,&bx,tmp);
      ax--;
      Set(ax,bx,tmp[0]);
    }else if(tmp[0]=='c'){
      scanf("%d %d %d %d",&ax,&bx,&cx,&dx);
      ax--,cx--;

      int lenS=bx-ax;
      int lenT=dx-cx;

      int l=0,r=min(lenS,lenT)+1,m;
      while(r-l>1){
        m=(l+r)/2;
        if( Get(ax,ax+m) == Get(cx,cx+m) )l=m;
        else r=m;
      }
      if(l==min(lenS,lenT)){
        if(lenS<lenT)printf("s\n");
        else if(lenS>lenT)printf("t\n");
        else printf("e\n");
      }else{
        ull lastS=Get(ax+l,ax+l+1);
        ull lastT=Get(cx+l,cx+l+1);
        if(lastS<lastT)printf("s\n");
        else if(lastS>lastT)printf("t\n");
        else assert(0);
      }

    }
  }
  return 0;
}