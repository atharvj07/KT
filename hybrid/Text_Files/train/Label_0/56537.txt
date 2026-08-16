import java.util.Scanner;

public class ProblemD {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextInt();
		sc.nextLine();
		String input = sc.nextLine();
		int last = input.length();
		long res = 0;
		long power = 1;
		int max_length = String.valueOf(n).length();
		while (last > 0) {
			// System.out.println("Last=" + last);
			int first = last - 1;
			while (first > 0 && last-first <= max_length) {
				String temp = input.substring(first - 1, last);
				long value = Long.parseLong(temp);
				if (value < n) {
					first--;
				} else {

					break;
				}
			}
			while (first < last - 1 && input.charAt(first) == '0')
				first++;
			// System.out.println("Cal + " + cal);
			res += Long.parseLong(input.substring(first, last)) * power;
			// System.out.println(res);
			power *= n;
			last = first;
		}
		System.out.println(res);

	}

}
