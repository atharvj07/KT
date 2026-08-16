import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.close();
		int r = 0;
		for(int i = 1; i <= N; i++) {
			int l = String.valueOf(i).length();
			if(l % 2 != 0) r++;
		}
		System.out.println(r);
	}
}
