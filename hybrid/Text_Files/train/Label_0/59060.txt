import java.util.Scanner;

public class Main {

	static final int INF=Integer.MAX_VALUE;			// 2147483647
	static final long LINF=Long.MAX_VALUE;			// 9223372036854775807

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int as[] = new int[n]; 
		for (int i=0; i<n; i++) {
			as[i] = sc.nextInt();
		}
		sc.close();
		
		int pair = 0;
		for (int i=0; i<n; i++) {
			if (as[as[i]-1] == i+1) {
				pair++;
			}
		}
		
		p(pair/2);
		
		
	}
	
	
	
	
	public static void p(Number a) {
		System.out.println(a);		
	}
	public static void p(String a) {
		System.out.println(a);		
	}
	public static void pn(Number a) {
		System.out.print(a);		
	}
	public static void pn(String a) {
		System.out.print(a);		
	}
	
	public static int powerInt(int a, int b) {
		return (int) Math.pow(a, b);
	}

	public static int max(int arr[]) {
		int max = arr[0];
		
		for (int i=0; i<arr.length; i++) {
			if (max < arr[i]) {
				max = arr[i];
			}
		}
		
		return max;
	}
	public static double max(double arr[]) {
		double max = arr[0];
		
		for (int i=0; i<arr.length; i++) {
			if (max < arr[i]) {
				max = arr[i];
			}
		}
		
		return max;
	}	
	public static int min(int arr[]) {
		int max = arr[0];
		
		for (int i=0; i<arr.length; i++) {
			if (max > arr[i]) {
				max = arr[i];
			}
		}
		
		return max;
	}
	public static double min(double arr[]) {
		double max = arr[0];
		
		for (int i=0; i<arr.length; i++) {
			if (max > arr[i]) {
				max = arr[i];
			}
		}
		
		return max;
	}	

}
