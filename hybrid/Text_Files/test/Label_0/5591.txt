#include <bits/stdc++.h>
#include<string.h>
#include<utility>
#define ll long long int 
#include<fstream>
#define pb push_back
#include<vector>
#include<stack>
#define INF INT_MAX
#include <deque>
#define modulo  1000000007
using namespace std;
//Fuck ratings 
//Get charasi...Have some ganja
ll checkpalindrome(ll c)
{ 
    string p=to_string(c); 
       int j = p.size() - 1;

    for (int i = 0; i < j; i++, j--)
    {
        if (p[i] != p[j])
        {
            return 0;
        }
    }

    return 1;
}
ll  isSubsetSum(ll a[], ll n, ll sum) 
{ 
    
    bool  t[n + 1][sum + 1]; 
  
    for (int i = 0; i <= n; i++) 
        t[i][0] = true; 
  
    for (int i = 1; i <= sum; i++) 
        t[0][i] = false; 
  

    for (int i = 1; i <= n; i++) { 
        for (int j = 1; j <= sum; j++) { 
            if (j < a[i - 1]) 
                t[i][j] = t[i - 1][j]; 
            if (j >= a[i - 1]) 
                t[i][j] = t[i-1 ][j] 
                               ||t[i - 1][j - a[i - 1]]; 
        } 
    } 
  
  ll j;
     ll diff = INT_MAX,p;
     for ( j=sum/2; j>=0; j--)
    {
         
        if (t[n][j] == true)
        {
            diff=sum-j;
            
            break;
        } 
    }
    return diff;

}
int max(int a, int b) 
{  
    return (a > b) ? a : b;  
} 
ll  KnapSack(ll W, ll  wt[], ll  val[], ll n) 
{ 
    int i, j; 
    int t[n + 1][W + 1]; 
  
    // Build table K[][] in bottom up manner 
    for (i = 0; i <= n; i++)  
    { 
        for (j= 0;  j<= W; j++)  
        { 
            if (i == 0 || j == 0) 
                t[i][j] = 0; 
            else if (wt[i - 1] <= j) 
                t[i][j] = max(val[i - 1] 
                          + t[i - 1][j - wt[i - 1]], 
                          t[i - 1][j]); 
            else
                t[i][j] = t[i - 1][j]; 
        } 
    } 
  
    return t[n][W]; 
} 
ll tle(ll a[],ll n, ll m)
{
    ll i,j,t[n+1][m+1];
    for(i=0;i<=n;i++)
    {
        for(j=0;j<=m;j++)
        {
            if(i==0 || j==0) t[i][j]=0;
            else if(a[i-1]<=j)
            {
                t[i][j]=max(1+t[i-1][j-a[i-1]],t[i-1][j]);
            }
            else 
            t[i][j]= t[i-1][j];
        }
    }
    return t[n][m];
}
bool isSubSequence(string s, string p, ll n, ll m) 
{ 
   int j = 0; // For index of str1 (or subsequence 
  
   // Traverse str2 and str1, and compare current character  
   // of str2 with first unmatched char of str1, if matched  
   // then move ahead in str1 
   for (int i=0; i<n&&j<m; i++) 
       if (p[j] == s[i])
       {  cout<<i<<" ";
         j++; 
       }
   // If all characters of str1 were found in str2 
   return (j==m); 
} 
void track(vector<ll>&a,vector<vector<ll>> &res ,vector<ll>& v,ll idx)
{
    res.pb(v);
    for(int i=idx;i<a.size();i++)
    {
        v.pb(a[i]);
        track(a,res,v,i+1);
        v.pop_back();
    }
    return ;
}
vector<vector<ll>> call(vector<ll>&a ,ll n)
{
    vector<vector<ll>>res;
    vector<ll >v;
    ll idx=0;
     track(a,res,v,idx);
     return res;
}



int main()
{     ios_base::sync_with_stdio(false);
      cin.tie(NULL);
      ll t,n;
      cin>>t;
      while(t--)
      {  cin>>n;
          int a[n],b[n];
          for(int i=0;i<n;i++){
               cin>>a[i];
               b[i]=a[i];
          }
          sort(b,b+n);
          int ans=0;
          for(int i=0;i<n;i++){
               if(i==0&&b[i]!=b[i+1]){
                    ans=b[i];
                    break;
                    
               }
               else if(i==n-1&&b[i]!=b[i-1]){
                    ans=b[i];
                    break;
               }
               else if(b[i]!=b[i-1]&&b[i]!=b[i+1]){
                    ans=b[i];
                    break;
               }
               
          }
          if(ans>0){
          for(int i=0;i<n;i++){
               if(ans==a[i]){
                    cout<<i+1<<endl;
                    break;
               }
          }
          }
          else
          cout<<-1<<endl;
     }
    
}
