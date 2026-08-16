#include<bits/stdc++.h>
using namespace std;

long long int A[2000][1009],B[2000];

int main()
{
    long long int N,M,F,Z,e,i,j,k,a,b,c,f,x,y,z,m,n,p,s,mx;
    string S;
    cin>>F;
    for(f=0;f<F;f++)
    {
        cin>>N;
        Z=1;
        while(1)
        {
            if((N%11)==0)
            {
                break;
            }
            else
            {
                N=N-111;
                if(N<0)
                {
                    Z=0;
                    break;
                }
            }
        }
        if(Z==1)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}