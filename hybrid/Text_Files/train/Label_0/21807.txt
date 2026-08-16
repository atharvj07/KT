#include<bits/stdc++.h>
#define ll long long
#define fio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
using namespace std;
 
int main()
{
   fio;
   ll t=0;
   cin>>t;
   for(ll z=0; z<t; z++){  
      ll n,k,temp;
      cin>>n>>k;
      vector<ll> v;
      for(int i = 0; i < n; i++){
         cin>>temp;
         v.push_back(temp);
      }
      if(k == 0){
         cout<<n<<"\n";
         continue;
      }
      if(n == 1){
         if(v[0] == 1){
            cout<<1<<"\n";
            continue;
         }
         else if(v[0] == 0){
            cout<<n+k<<"\n";
            continue;
         }
         else{
            cout<<2<<"\n";
            continue;
         }
      }
      sort(v.begin(), v.end());
      ll a = -1;
      ll b = v[n-1];
      bool done = false;
      if(v[0] != 0){
         a = 0;
      }
      else{
         ll iter = 0;
         for(int i = 0; i < n; i++){
            if(v[i] != iter){
               a = iter;
               break;
            }
            iter++;
         }
         if(a == -1){
            cout<<n+k<<"\n";
            done = true;
         }
      }
      if(done){
         continue;
      }
      ll val = 0;
      if((a + b) % 2 == 0){
         val = (a + b) / 2;
      }
      else{
         val = ((a + b) / 2) + 1;
      }
      ll sizeset = 0;
      for(int i = 0; i < n; i++){
         if(v[i] == val){
            sizeset = n;
            break;
         }
         if(v[i] > val){
            break;
         }
      }
      if(sizeset == 0){
         sizeset = n + 1;
      }
      cout<<sizeset<<"\n";
   }
   return 0;
}