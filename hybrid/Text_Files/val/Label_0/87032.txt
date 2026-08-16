import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long t1 = sc.nextLong();
		long t2 = sc.nextLong();
		long a1 = sc.nextLong();
		long a2 = sc.nextLong();
		long b1 = sc.nextLong();
		long b2 = sc.nextLong();

		long sub1 = (a1 - b1) * t1;
		long sub2 = (a2 - b2) * t2;

		if (sub1 + sub2 == 0) {
			System.out.println("infinity");
			return;
		} else if (sub1 > 0 && sub2 > 0) {
			System.out.println(0);
			return;
		} else if (sub1 < 0 && sub2 < 0) {
			System.out.println(0);
			return;
		}

		if (sub1 < 0) {
			sub1 = -sub1;
			sub2 = -sub2;
		}

		long dist = sub1 + sub2;

		if (dist < 0) {
			if ((sub1 % (-dist) == 0)) {
				System.out.println((sub1 / (-dist)) * 2);
				return;
			}
			System.out.println((sub1 / (-dist)) * 2 + 1);
			return;
		}
		System.out.println(0);
	}

}