#include<cstdio>
 
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
int main(){
    for(int n,m;scanf("%d%d",&n,&m),n;){
        int a[1000];
        rep(i,n) scanf("%d",a+i);
 
        bool ok;
        int b[1012];
        rep(S,1<<m){
            int sum=0;
            rep(i,m) sum+=b[i]=S>>i&1;
            rep(i,n-1) b[m+i]=a[i+1]-a[i]+b[i];
 
            ok=(sum==a[0]);
            rep(i,n+m-1) if(b[i]!=0 && b[i]!=1) ok=false;
            if(ok) break;
        }
 
        if(ok){ rep(i,n+m-1) printf("%d",b[i]); puts(""); } else puts("Goofy");
    }
 
    return 0;
}