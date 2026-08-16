import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int[] leaf;

	public static void main(String[] args) throws Exception {
		double EPS = 1e-9;
		while (true) {
			double D = sc.nextDouble();
			if (D == 0) break;
			double px = sc.nextDouble();
			double py = sc.nextDouble();
			double vx = sc.nextDouble();
			double vy = sc.nextDouble();
			if (Math.abs(px * vy - py * vx) > EPS) {
				System.out.println("impossible");
				continue;
			}
			double dist = Math.sqrt(px * px + py * py);
			double v = Math.sqrt(vx * vx + vy * vy);
			if (px * vx >= 0 && py * vy >= 0) {
				dist = (2 - dist);
			}
			double time = dist / v;
			if (time < D) {
				System.out.println(dist);
			} else {
				System.out.println("impossible");
			}
		}
	}

}