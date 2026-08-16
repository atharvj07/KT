import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int ans = 0;
		
		ans = n % 1000;
		
		if(ans != 0) {
			ans = 1000 - ans;
		}
		System.out.println(ans);

	}

}
