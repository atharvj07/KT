import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		int R = a.nextInt();
		if(R < 1200) {
			System.out.println("ABC");
		}else if(R < 2800) {
			System.out.println("ARC");
		}else {
			System.out.println("AGC");
		}
   }
}