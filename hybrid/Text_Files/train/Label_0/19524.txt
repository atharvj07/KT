#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n,ans=0,r=10;
    cin>>n;
    if(!(n%2)){
        while(n>=r){
            ans+=n/r;
            r*=5;
        }
    }
    cout<<ans<<endl;
}