#include <iostream>
using namespace std;
int main(void){
    long long N,P,i,j,k,ans=1;
    cin>>N>>P;
    if(N==1){
        cout<<P<<endl;
        return 0;
    }
    for(i=2;P>1&&i*i<P+1;i++){
        k=0;
        while(P%i==0){
            k++;
            P/=i;
        }
        for(j=0;j<k/N;j++){
            ans*=i;
        }
    }
    cout<<ans<<endl;
}