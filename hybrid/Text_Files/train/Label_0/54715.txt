import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int D = s.nextInt();
		int L = s.nextInt();
		int ans = D/L + D%L;
		
		System.out.println(ans);
		
		
	}
}