#include <iostream>
using namespace std;
int main(){
    int a,b,c;
    int ans=0;
    int sum=0;
    cin>>a>>b>>c;
    while(sum<c){
        ans+=1;
        sum+=a;
        if(ans%7==0){
            sum+=b;
        }
    }
    cout<<ans<<endl;
}
