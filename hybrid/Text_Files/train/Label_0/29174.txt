#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    char c1,c2;
    cin>>c1;
    char ans;
    for (int i = 1; i < n; ++i) {
        cin>>c2;
        if(c1=='T'&&c2=='T')ans='T';
        else if(c1=='T'&&c2=='F')ans='F';
        else if(c1=='F'&&c2=='T')ans='T';
        else if(c1=='F'&&c2=='F')ans='T';
        c1=ans;
    }
    cout<<ans<<endl;

    return 0;
}
