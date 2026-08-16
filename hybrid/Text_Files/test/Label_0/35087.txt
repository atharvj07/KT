import java.util.*;

class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int A[] = new int[n];
		for(int i=0; i<n; i++){
			A[i] = sc.nextInt();
		}
		int part = partition(A, 0, n-1);
		int work=0;
		for(int i=0; i<n; i++){
			if(work == 0){
				work = 1;
			} else{
				System.out.print(" ");
			}
			if(part == i){
				System.out.print("["+A[i]+"]");
			} else{
				System.out.print(A[i]);
			}
		}
		System.out.println();
	}
	static int partition(int A[], int p, int r){
		int work;
		int i = p-1;
		for(int j=p; j<=r-1; j++){
			if(A[j] <= A[r]){
				i++;
				work = A[i];
				A[i] = A[j];
				A[j] = work;
			}
		}
		work   = A[i+1];
		A[i+1] = A[r];
		A[r]   = work;
		return i+1;
	}
}