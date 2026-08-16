#include<iostream>
#include<algorithm>
using namespace std;
int a[300010];
int b[300010];
int sum[300010];
int ans[300010];
int main(){
    int n;cin>>n;
    for(int i=1;i<=n;i++){
        int tmp;cin>>tmp;a[tmp]++;
    }
    int m=0;
    for(int i=1;i<=n;i++) if(a[i])b[++m]=a[i];
    sort(b+1,b+m+1);
    for(int i=1;i<=m;i++) sum[i]=sum[i-1]+b[i];
    b[m+1]=1e9;
    for(int i=1;i<=m;i++){
        int l=i+1,r=m+1;
        while(l<=r){
            int m1=l+r>>1;
            int tmp=sum[m1-1]/(m1-i);
            if(tmp<=b[m1]) ans[m+1-i]=tmp,r=m1-1;
            else l=m1+1;
        }
    }
    for(int i=1;i<=n;i++)cout<<ans[i]<<endl;
}