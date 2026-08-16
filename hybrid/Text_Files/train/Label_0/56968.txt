import java.util.Scanner;

public class p1009A {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int ctr = 0;
		int[] games = new int[n];
		for(int i = 0; i < n; i++) {
			games[i] = sc.nextInt();
		}
		
		int j = 0;
		for(int i = 0; i < m && j < n; i++) {
			int k = sc.nextInt();
			while(j < n && games[j] > k) {
				j++;
			}
			if(j < n)
				ctr++;
			j++;
		}
		
		System.out.println(ctr);
	}
}
