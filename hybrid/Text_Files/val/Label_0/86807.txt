import java.util.*;

class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		List<Integer> list = new ArrayList<Integer>();

		for (int i = 0; i < 10; i++)
			list.add(sc.nextInt());

		Collections.sort(list);
		Collections.reverse(list);
		for (int i = 0; i < 3; i++)
			System.out.println(list.get(i));
	}
}