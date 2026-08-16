#include <bits/stdc++.h>
using namespace std;

int main()
{ 
   int n;
   cin>>n;
   pair<int,int> a[n],b[n];
   for(int i=0;i<n;i++){
       int x,y;
       cin>>x>>y;
       a[i]=make_pair(x,y);
   }
   for(int i=0;i<n;i++){
       int x,y;
       cin>>x>>y;
       b[i]=make_pair(y,x);
   }
   sort(a,a+n);
   reverse(a,a+n);
   sort(b,b+n);
   int ans=0;
   int used[n];
   for(int i=0;i<n;i++){
       used[i]=0;
   }
   for(int i=0;i<n;i++){
       for(int j=0;j<n;j++){
           if(a[i].first<b[j].second && a[i].second<b[j].first && used[j]==0){
               used[j]=1;
               ans++;
               break;
           }
       }
   }
   cout<<ans<<endl;
}