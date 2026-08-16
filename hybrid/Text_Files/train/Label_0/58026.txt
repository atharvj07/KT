import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n;
		n = scanner.nextInt();
		scanner.nextLine();
		String ss = scanner.nextLine();
		char bf = '\0';
		int same = 0;
		for (int i = 0; i < ss.length(); i++) {
			if (bf == ss.charAt(i) && (bf == 'a' || bf == 'e' || bf == 'i' || bf == 'o' || bf == 'u' || bf == 'y')) {
				same++;
			} else {
				if ((bf == 'e' || bf == 'o') && same == 1)
					System.out.print(bf);
				System.out.print(ss.charAt(i));
				same = 0;

				bf = ss.charAt(i);
			}
		}
		if ((bf == 'e' || bf == 'o') && same == 1)
			System.out.print(bf);
		System.out.println();
	}

}
