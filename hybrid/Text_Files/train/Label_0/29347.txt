#include<bits/stdc++.h>
using namespace std;

int main(){
  cin.tie(0); ios::sync_with_stdio(0);

  int n,a,d;
  cin >> n >> a >> d;

  int m;
  cin >> m;
  vector<int> x(m),y(m),z(m);
  for(int i=0;i<m;i++){
    cin >> x[i] >> y[i] >> z[i];
  }

  int k;
  cin >> k;

  stack<int> task;
  for(int i=m-1;i>=0;i--){
    if(y[i] <= k && k <= z[i]){
      if(x[i] == 0){
	int dif = z[i] - k;
	k = y[i] + dif;
      }else{
	task.push(x[i]);
      }
    }
  }

  int val = a + d*(k-1);
  while(!task.empty()){
    if(task.top() == 1){
      val++;
    }else{
      val /= 2;
    }
    task.pop();
  }
  cout << val << endl;
}