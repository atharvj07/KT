#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(void){
    string s;
    cin>>s;
    int n=s.size();
    int a[100010];
    for(int i=0;i<n;i++) a[i]=1;
    for(int i=0;i+2<n;i++){
        if(s[i]=='R'&&s[i+1]=='R'){
            a[i+2]+=a[i];
            a[i]=0;
        }
    }
    for(int i=n-1;i-2>=0;i--){
        if(s[i]=='L'&&s[i-1]=='L'){
            a[i-2]+=a[i];
            a[i]=0;
        }
    }
    for(int i=0;i<n;i++) cout<<a[i]<<" ";
}