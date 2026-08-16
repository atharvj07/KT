#include<cstdio>
#include<iostream>
using namespace std;
int q;long long sum,a,b,m=100000000000;bool flag;
int main()
{
    cin>>q;
    while(q--)
    {
        cin>>a>>b;
        sum+=b;
        if(m>b&&b<a)
            m=b;
        if(a!=b)
            flag=1;
    }
    if(flag)
        cout<<sum-m;
    else cout<<0;
}