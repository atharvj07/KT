#include <iostream>

using namespace std;

int main()
{
    long int t;
    cin>>t;
    while(t--){
        long int n,coun=0;
        cin>>n;
        long int *p = new long int[2*n];
        for(long int i=0;i<2*n;++i){
            cin>>*(p+i);
            if(*(p+i)%2==0)
                ++coun;
        }
        if(coun!=n)
            cout<<"No\n";
        else
            cout<<"Yes\n";
    }
    return 0;
}
