import java.util.Arrays;
import java.util.Scanner;

public class Main {
	private Scanner sc;
	
	public static void main(String[] args) {
		new Main();
	}
	
	public Main() {
		sc = new Scanner(System.in);

		while (sc.hasNextLine() == true) {
			int nico = Integer.parseInt(sc.nextLine());
			long ans = 1;
			
			for (int i = 0; i < nico; i++) {
				ans = ans * (i + 1);
			}
			System.out.println(ans);
		}
	}
}