#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for(long long int i=0;i<n;++i)
typedef long long int ll;

int dfs(vector<string> a,int id){
    int ret;
    if(a[id].back()=='*'){
        ret=1;
        for(int i=id+1;i<a.size();i++){
            if(a[id].size()+1==a[i].size()){
                if(a[i].back()=='+'||a[i].back()=='*'){
                    ret*=dfs(a,i);
                }else{
                    ret*=a[i].back()-'0';
                }
            }else if(a[i].size()<=a[id].size()){
                break;
            }
        }
    }else if(a[id].back()=='+'){
        ret=0;
        for(int i=id+1;i<a.size();i++){
            if(a[id].size()+1==a[i].size()){
                if(a[i].back()=='+'||a[i].back()=='*'){
                    ret+=dfs(a,i);
                }else{
                    ret+=a[i].back()-'0';
                }
            }else if(a[i].size()<=a[id].size()){
                break;
            }
        }
    }else{
        return a[id].back()-'0';
    }
    return ret;
}

int main(){

    while(1){
        int n;
        cin >> n;
        if(n==0)break;
        vector<string> a(n);
        for(int i=0;i<n;i++){
            cin >> a[i];
        }
        int ans=dfs(a,0);
        cout << ans << endl;
    }

    return 0;
}
