import java.util.Scanner;
public class BinaryNumber {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String binary = scan.next();
		// Even
		int count = 0;
		int carry = 0;
		for(int i = binary.length() - 1; i >= 0; i--) {
			int current = Character.getNumericValue(binary.charAt(i));
			if (i != 0) {
				if (current == 0 && carry == 0) {
					count += 1;
//					System.out.println(current + " first");
				} else if (current == 1 && carry == 0) {
					count += 2;
					carry = 1;
//					System.out.println(current + " second");
				} else if (current == 0 && carry == 1) {
					count += 2;
//					System.out.println(current + " third");
				} else {
					count += 1;
//					System.out.println(current + " fourth");
				}
				
			} else {
				if (current == 0 && carry == 0) {
				} else if (current == 1 && carry == 0) {
				} else if (current == 0 && carry == 1) {
				} else {
					count += 1;
				}
			}
		}
		System.out.println(count);
	}
}