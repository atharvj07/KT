#include<iostream>
#include<vector>
using namespace std;

int main(){
  int n,k=0;
  vector<int> A,B,C;

  cin >> n;
  A.resize(n);
  B.resize(n);
  for(int i=0;i<n;i++){
    cin >> A[i];
    k > A[i] ? : k = A[i];
  }
  C.resize(k+1);

  for(int i=0;i<n;i++){
    C[A[i]]++;
  }
  for(int i=1;i<k+1;i++){
    C[i] += C[i-1];
  }
  for(int i=n-1;i>=0;i--){
    B[C[A[i]] - 1] = A[i];
    C[A[i]]--;
  }

  cout << B[0];
  for(int i=1;i<n;i++){
    cout << " " << B[i];
  }
  cout << endl;
}
