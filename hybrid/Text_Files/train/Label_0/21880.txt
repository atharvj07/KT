#include <bits/stdc++.h>
using namespace std;
int t,c[19],a[19];
string ans="Yes";
int main()
{
    cin>>t;
    for(int i=0;i<t;i++)
    {
         for(int i=0;i<3;i++)
            cin>>c[i];
         for(int i=0;i<5;i++)
            cin>>a[i];
         if(a[0]<=c[0])
         {
             c[0]-=a[0];
             a[0]=0;
    }
    else if(c[0]<a[0])
    {
        a[0]-=c[0];
        c[0]=0;
    }
    if(a[1]<=c[1])
    {
        c[1]-=a[1];
        a[1]=0;
    }
    else if(c[1]<a[1])
    {
        a[1]-=c[1];
        c[1]=0;
    }
    if(a[2]<=c[2])
    {
        c[2]-=a[2];
        a[2]=0;
    }
    else if(c[2]<a[2])
    {
       a[2]-=c[2];
       c[2]=0;
    }
    if(a[3]<=c[0])
    {
        c[0]-=a[3];
        a[3]=0;
    }
    else if(c[0]<a[3])
    {
        a[3]-=c[0];
        c[0]=0;
    }
    if(a[3]<=c[2])
    {
        c[2]-=a[3];
        a[3]=0;
    }
    else if(a[3]>c[2])
    {
        a[3]-=c[2];
        c[2]=0;
    }
    if(a[4]<=c[1])
    {
        c[1]-=a[4];
        a[4]=0;
    }
    else if(a[4]>c[1])
    {
        a[4]-=c[1];
        c[1]=0;
    }
    if(a[4]<=c[2])
    {
        c[2]-=a[4];
        a[4]=0;
    }
    else if(a[4]>c[2])
    {
        a[4]-=c[2];
        c[2]=0;
    }
    if(a[0]==0&&a[1]==0&&a[2]==0&&a[3]==0&&a[4]==0)
        cout<<"Yes"<<endl;
    else
        cout<<"No"<<endl;
    }
}
