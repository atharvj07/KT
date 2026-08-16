import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		while (n != 0) {
			char[] step = sc.next().toCharArray();
			char on = ' ';
			boolean flag = true;
			for (int i = 0; i < step.length; i++) {
				if (step[i] == on) {
					flag = false;
					break;
				}
				on = step[i];
			}
			System.out.println(flag ? "Yes" : "No");
			n--;
		}
	}
}