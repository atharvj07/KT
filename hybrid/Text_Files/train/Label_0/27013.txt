#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll ans;
int main() {
    int n,k,R,P,S;
    cin >> n >> k >> R >> S >> P;
    string s;
    cin >> s;
    for(int i = 0;i<n;i++)
    {
        if(i >= k && s[i]==s[i-k]){
            s[i] = ' ';
            continue;
        }
        if(s[i] == 'r')
            ans += P;
        if(s[i] == 'p')
            ans += S;
        if(s[i] == 's')
            ans += R;
    }
    cout << ans;
}
