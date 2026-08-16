import java.util.Scanner;
import java.util.TreeSet;

public class Main {
	public static void main(String args[]) {

		Scanner scan = new Scanner (System.in);
		
		//list作成
		TreeSet<Integer> set = new TreeSet<>();
		
		int a = scan.nextInt();
		for(int i=0; i<a; i++) {
			int num = scan.nextInt();
			set.add(num);
		}
		
		//list2作成
		TreeSet<Integer> set2 = new TreeSet<>();
		
		int b = scan.nextInt();
		for(int i=0; i<b; i++) {
			int num = scan.nextInt();
			set2.add(num);
		}
		
		//積集合
		TreeSet<Integer> intersection = new TreeSet<>(set);
		intersection.retainAll(set2);
		
//		System.out.println("dubug");
//		System.out.println(intersection.size());
		
		for(int i : intersection) {
			System.out.println(i);
		}

	}
}

