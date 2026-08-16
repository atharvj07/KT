#include <bits/stdc++.h>
using namespace std;
char ax[200005];
int dp[200005];
int len;
map<int,int> m;

int main()
{
    scanf("%s",ax);
    int i,j,a,b,now=0;
    len = strlen(ax);
    m[0]=len;
    for(i=len-1;i>=0;i--){
        now ^= (1<<(ax[i]-'a'));
        dp[i]=len-i;
        if(m.count(now))dp[i]=min(dp[i],dp[m[now]]+1);
        for(j=0;j<26;j++){
            a = now^(1<<j);
            if(!m.count(a))continue;
            dp[i]=min(dp[i],dp[m[a]]+1);
        }
       if(!m.count(now))m[now]=i;
       else if(dp[i]<dp[m[now]])m[now]=i;
    }
    printf("%d",dp[0]);
    return 0;
}
