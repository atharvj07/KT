import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		
		boolean[] visits = new boolean[100000];
		Arrays.fill(visits, false);
	
		int[] buttons = new int[n];
		for (int i = 0; i < buttons.length; i++) {
			buttons[i] = scanner.nextInt();
		}
		
		int now = 0;
		int ans = 0;
		while(true){
			ans++;
			if (visits[now]) {
				ans = -1;
				break;
			}else {
				visits[now] = true;
			}
			now = buttons[now]-1;
			if (now==1) {
				break;
			}
		}
		
		System.out.println(ans);
		
		
		
		
		scanner.close();
	}
}