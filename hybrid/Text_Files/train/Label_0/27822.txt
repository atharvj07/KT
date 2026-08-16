#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i=0;i<n;i++){
    cin >> a[i];
  }
  sort(a.begin(),a.end());
  long long sum=0;
  for(int i=0;i<n/2;i++){
    sum-=a[i]*2;
  }
  for(int i=0;i<n/2;i++){
    sum+=a[n-1-i]*2;
  }
  long long sum2=sum;
  if(n%2==1){
    sum-=a[n-1-n/2+1];
    sum+=a[n/2];
    sum2+=a[n/2-1];
    sum2-=a[n/2];
  }
  else{
    sum-=a[n/2];
    sum+=a[n/2-1];
    sum2=0;
  }
  cout << max(sum,sum2) << endl;
}