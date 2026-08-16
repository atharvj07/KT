#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
int main(void){
    int a,b;
    int n,s,f;
    int tim[1010]={0};
    cin>>a>>b;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>s>>f;
        for(int j=s;j<f;j++){
            tim[j]=1;
        }
    }
    int ans=0;
    for(int i=a;i<b;i++){
        if(tim[i]==1){
            ans=1;
            break;
        }
    }
    cout<<ans<<endl;
}
