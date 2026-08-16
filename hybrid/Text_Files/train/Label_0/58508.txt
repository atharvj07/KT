import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// 入力
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		List<Vector2d> p = new ArrayList<>();
		for (int i=0; i<n; i++) {
			double x = sc.nextDouble();
			double y = sc.nextDouble();
			p.add(new Vector2d(x, y));
		}
		sc.close();
		System.out.println(String.format("%1$.1f", solve(p)));
	}

	static class Vector2d {
		Vector2d(Double x, Double y){
			this.x = x;
			this.y = y;
		}
		Double x;
		Double y;
		public String toString() {
			return String.format("%1$.10f %2$.10f", x, y);
		}
	}

	public static Double solve(List<Vector2d> p) {
		Double v2times = 0.0;
		int s = p.size();
		for (int i=0; i<s; i++) {
			v2times += (p.get(i).x * p.get((i+1)%s).y - p.get(i).y * p.get((i+1)%s).x);
		}
		return v2times / 2;
	}
}

