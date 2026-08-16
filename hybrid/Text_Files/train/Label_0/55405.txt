import java.util.*;

public class Archer {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		//MAC 2312
		double a = scan.nextDouble();
		double b = scan.nextDouble();
		double c = scan.nextDouble();
		double d = scan.nextDouble();
		double ans = (a/b)/(1-((b-a)/b*(d-c)/d));
		System.out.println(ans);
	}
}
