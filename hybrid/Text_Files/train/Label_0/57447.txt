
import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) {
		try {
			String packageName = new Main().getClass().getPackage().getName();
			System.setIn(new FileInputStream("src/" + packageName + "/input.txt"));
			// System.setOut(new PrintStream(new FileOutputStream("src/" + packageName + "/result.txt")));
		} catch (FileNotFoundException e) {
		} catch (NullPointerException e) {
		}
		new Main().run();
	}

	void tr(Object... os) {
		System.err.println(deepToString(os));
	}

	Scanner sc;
	void run() {
		sc = new Scanner(System.in);
		int n = sc.nextInt();

		ArrayList< ArrayList<Integer> > es = new ArrayList<ArrayList<Integer> >();
		for (int i = 0; i < n; i++)
			es.add(new ArrayList<Integer>());

		System.out.println(n - 1);
		for (int i = 0; i < n - 1; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			System.out.println("2 " + a + " " + b);
			a--;
			b--;
			es.get(a).add(i);
			es.get(b).add(i);

		}
		for (int j = 0; j < n; j++) {
			for (int k = 1; k < es.get(j).size(); k++) {
				int a = (es.get(j).get(0) + 1);
				int b = (es.get(j).get(k) + 1);
				System.out.println( a + " " + b );
			}

		}
	}


}
