import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		double money = 0.;
		for (int i = 0; i < n; i++) {
			String str = sc.next();
			if(sc.next().equals("JPY")) {
				money += Integer.parseInt(str);
			} else {
				money += Double.parseDouble(str) * 380000;
			}
		}
		System.out.println(money);
	}
}
