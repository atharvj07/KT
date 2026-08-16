import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String S = sc.next();
		sc.close();
		int[]c = new int[26];
		for(int i = 0; i < S.length(); i++) {
			int k = S.charAt(i) - 'a';
			c[k]++;
		}
		for(int i = 0; i < 26; i++) {
			if(c[i] > 1) {
				System.out.println("no");
				System.exit(0);
			}
		}
		System.out.println("yes");
	}
}