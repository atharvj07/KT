#include<iostream>
#include<algorithm>
#include<vector>
#include<stdio.h>
#include<math.h>
using namespace std;
int main(){
    int a,b,c,ans=0,s=0;
    cin>>a>>b>>c;
    while(s<c){
        s=s+a;
        ans++;
        if(ans%7==0)s=s+b;
    }
    cout<<ans<<endl;
}
