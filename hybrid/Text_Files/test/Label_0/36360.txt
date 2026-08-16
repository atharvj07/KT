import java.util.*;

public class Main {
	void solve() {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		for(int i = 1; i <= 100000; i++) {
			if((int)(i * 0.08) == a && (int)(i * 0.1) == b) {
				System.out.println(i);
				return;
			}
		}
		System.out.println(-1);
		scan.close();
	}
	
	public static void main(String[] args) {
		new Main().solve();
	}
}
