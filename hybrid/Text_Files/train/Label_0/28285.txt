#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1e9+7;
int main() {
    string s;
    cin >> s;
    ll n=s.size();
    vector<ll>num(n,0);
    for(ll i=0;i<n-1;i++){
        if(s[i]=='R'&&s[i+1]=='L'){
            for(ll j=i;j>=0&&s[j]=='R';j--){
                num[i+((i-j)%2)]++;
            }
            for(ll j=i+1;j<n&&s[j]=='L';j++){
                num[i+((j-i)%2)]++;
            }
        }
    }
    for(ll i=0;i<n;i++){
        cout << num[i] << " ";
    }
}