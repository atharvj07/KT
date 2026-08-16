#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=1,j=m+1;i<j;i++,j--){
        cout<<i<<" "<<j<<endl;
    }
    
    for(int i=m+2,j=m*2+1;i<j;i++,j--){
        cout<<i<<" "<<j<<endl;
    }
    return 0;
}