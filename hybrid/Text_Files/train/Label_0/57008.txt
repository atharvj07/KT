import java.util.ArrayList;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

class Main {

	public static void main(String[] args) {
		Set<Long> set = new TreeSet<Long>();
		try (Scanner sc = new Scanner(System.in)){
			int times = sc.nextInt();
			for (int i=0; i<times; i++) set.add(sc.nextLong());
			times = sc.nextInt();
			for (int i=0; i<times; i++) set.add(sc.nextLong());
			ArrayList<Long>  a = new ArrayList<Long>(set);
			for (int i=0; i<a.size(); i++) System.out.println(a.get(i));
		}
	}
}
