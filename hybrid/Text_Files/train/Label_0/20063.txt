#include<stdio.h>

int BubbleSort(int [],int n);

int main()
{
  int n;
  int i;
  int A[110];
  int cnt=0;

  while(scanf("%d",&n),n)
    {
      for(i=0;i < n;i++){
	scanf("%d",&A[i]);
      }
      
      cnt = BubbleSort(A,n);
      printf("%d\n",cnt);
    }
  return 0;
}

int BubbleSort(int A[],int n)
{
  int i,j;
  int cnt = 0;
  int temp;
  
  for(i=0;i < n;i++){
    for(j=n-1;j > i;j--){
      if(A[j-1] > A[j]){
	temp = A[j-1];
	A[j-1] = A[j];
	A[j] = temp;
	cnt++;
      }
    }
  }
  
  /*for(i=0;i < n;i++){
    if(i) printf(" ");
    printf("%d",A[i]);
  }
  printf("\n");
  */
  return cnt; 
}
