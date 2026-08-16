#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,m,arr[1000]={0},c=0;
        cin>>n>>m;
        int a[n],b[m];
        for(int j=0;j<n;j++)
        {
            cin>>a[j];
            arr[a[j]]++;
        }
        for(int j=0;j<m;j++)
        {
            cin>>b[j];
            if(arr[b[j]]==1)
                c++;
        }
        cout<<c<<endl;




    }



}
