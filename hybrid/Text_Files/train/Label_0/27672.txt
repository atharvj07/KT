#include <iostream>
using namespace std;
typedef long long ll;
int main(void){
    // Your code here!
    ll n,k;
    cin>>n>>k;
    int s[n];
    for(int i=0;i<n;i++){
        cin>>s[i];
    }
    ll ans=s[k-1]-s[0]+min(abs(s[0]),abs(s[k-1]));
    for(int i=0;i<n-k+1;i++){
        ll p=s[i+k-1]-s[i]+min(abs(s[i+k-1]),abs(s[i]));
        ans=min(ans,p);
    }
    cout<<ans<<endl;
}
