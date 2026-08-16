import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		List<Double> list = new ArrayList<Double>();
		while (in.hasNext())
			list.add(in.nextDouble());
		Collections.sort(list);
		System.out.println(list.get(list.size()-1)-list.get(0));
	}
}