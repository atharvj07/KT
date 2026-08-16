import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.TreeMap;

class Main {

	public static void main(String[] args) {

		Scanner sc = null;
		Map<Integer, Integer> nums = new TreeMap<Integer, Integer>();
		try {
			sc = new Scanner(System.in);
			int maxValue = 0;
			while (sc.hasNextInt()) {
				int num = sc.nextInt();
				int count = 0;
				nums.put(num, nums.containsKey(num) ? count = nums.get(num) + 1
						: 1);
				if (maxValue < count) {
					maxValue = count;
				}
			}
			for (Entry<Integer, Integer> entry : nums.entrySet()) {
				if (maxValue == entry.getValue()) {
					System.out.println(entry.getKey());
				}
			}

		} finally {
			sc.close();
		}
	}
}