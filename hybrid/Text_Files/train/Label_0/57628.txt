import java.util.*;

class Main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i = 0; i < n; i++){
			a[i] = sc.nextInt();
		}
		int cou = 0;
		for(int i = 0; i < n-1; i++){
			int min = i;
			for(int j = i+1; j < n; j++){
				if(a[j] < a[min]){
					min = j;
				}
			}
			if(min != i){
				cou++;
				int work = a[min];
				a[min] = a[i];
				a[i] = work;
			}
		}
		for(int i = 0; i < n-1; i++){
			System.out.print(a[i] + " ");
		}
		System.out.println(a[n-1]);
		System.out.println(cou);
	}
}

