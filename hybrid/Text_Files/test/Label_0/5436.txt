#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll t,k,num,a1,b1,a2,b2;
    cin>>t;
    while(t--)
    {
        cin>>k;
        num=a1=a2=100;
        for(int i=1;i<=100;i++)
        {
            if(((k%i)==0)&&((100%i)==0))
            {
                a1 = 100/i;
               
            }
        }
        for(int i=1;i<=100;i++)
        {
            if((((100-k)%i)==0)&&((100%i)==0))
            {
                a2= 100/i;
            }
        }
        cout<<min({(ll)100,a1,a2})<<'\n';
    }
    return 0;
}