#include<bits/stdc++.h>
using namespace std;
int main(){
    int N,K;scanf("%d%d",&N,&K);
    long long a[N];
    for(int i=0;i<N;i++)scanf("%lld",&a[i]);
    long long ans=1000000000000000;
    for(long long bit=0;bit<(1<<N);bit++){
        if(__builtin_popcount(bit)<K)continue;
        long long height=0,now=0;
        for(long long i=0;i<N;i++){
            if(bit&(1<<i)){
                if(height>=a[i]){
                    now+=height+1-a[i];
                    height++;
                }
                else height=a[i];
            }
            height=max(height,a[i]);
        }
        ans=min(ans,now);
    }
    printf("%lld\n",ans);
    return 0;
}