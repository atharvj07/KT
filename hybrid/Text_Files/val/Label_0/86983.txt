
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		new Main().run();
	}

	private void run() {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int e = scanner.nextInt();
			if (e == 0)
				break;
			int ans = e;
			for (int z = 0; z * z * z <= e; z++) {
				int k = e - z * z * z;
				int y = (int) Math.sqrt(k);
				int x = k - y * y;
				ans = Math.min(ans, x + y + z);
			}
			System.out.println(ans);
		}
	}
}