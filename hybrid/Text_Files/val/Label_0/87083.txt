
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int a[] = new int[n];
		int count[] = new int[n + 1];
		
		for(int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
			count[a[i]]++;
		}
		
		//まずはすべての組み合わせの合計を出す
		long total = 0;
		for(int i = 1; i <= n; i++) {
			total += (long)count[i]*(count[i] - 1)/2;
		}
		
		for(int i = 0; i < n; i++) {
			System.out.println(total - (count[a[i]] - 1));
		}
	}

}
