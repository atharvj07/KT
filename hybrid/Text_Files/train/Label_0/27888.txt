#include <bits/stdc++.h>
using namespace std ;
#define time cerr<<"time taken : "<<(float)clock()/CLOCKS_PER_SEC<<" secs"<<endl;
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL);
typedef long long ll ; 
typedef unsigned long long int ull ;
ll MOD = 100000007 ;

ll gcd(ll a, ll b){
  if(b==0)
    return a ;  
  return gcd ( b , a % b) ; 
}

ll lcm (ll a ,ll b ){
  return (a*b)/gcd(a,b) ; 
}
 
 
void solve(){
   
  int n ; 
  cin >> n ; 

  vector<int>arr(n);  

  for(int i=0;i<n;i++) cin >> arr[i]  ;  
  
  int mini =  *min_element(arr.begin() , arr.end())  ;  
  
  int same = 0  ; 
  for(int i = 0 ; i<n; i++){
    if(arr[i] == mini){
      same++ ;  
    }
  }
  
  cout << n - same <<"\n"  ;  

}
int32_t main()
{
  fast ;   time ;
  #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif

  ll t;
  cin >> t; 

  while(t--){
    solve()  ; 
  } 
  return 0; 
}