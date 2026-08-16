#include <iostream>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int n,a,c[100009];
ll ans=1ll;
int main(){
    cin>>n;
    c[0]=3;
    for(int i=0;i<n;i++){
        cin>>a;
        (ans*=c[a])%=1000000007;
        c[a]--;
        c[a+1]++;
    }
    cout<<ans<<endl;
}
