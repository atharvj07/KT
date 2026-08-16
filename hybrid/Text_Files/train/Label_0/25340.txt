#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
const int maxn = 1e5+7,mod = 1e9+7;
char s[333][333];
int n,ans;
bool jude(int k){
    for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
            if(s[(i+k)%n][j] != s[(j+k)%n][i])
                return false;
    return true;
}
int main(){
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%s",s[i]);
    for(int k=0;k<n;k++){
        if(jude(k))
            ans += n;
    }
    printf("%d\n",ans);
    return 0;
}
