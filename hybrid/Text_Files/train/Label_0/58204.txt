import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		String[] inputSplit = input.split("");
		int num0 = 0;
		for (int i = 0; i < inputSplit.length; i++) {
			if (inputSplit[i].equals("0")) {
				num0++;
			}
		}
		System.out.print(Math.min(num0, inputSplit.length - num0) * 2);
	}
}