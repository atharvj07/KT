import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] lst = new int[n];
		for (int i=0;i<n;i++) {
			lst[i] = sc.nextInt();
		}
		HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
		ArrayList<Integer> ans = new ArrayList<Integer>();
		for (int k=0;k<n;k++) {
			if (dict.get(lst[k]) == null) {
				dict.put(lst[k], 1);
			} else {
				dict.put(lst[k], dict.get(lst[k]) + 1);
				if (dict.get(lst[k]) == 0) dict.remove(lst[k]);
			}
			if (dict.get(lst[n - 1 - k]) == null) {
				dict.put(lst[n - 1 - k], -1);
			} else {
				dict.put(lst[n - 1 - k], dict.get(lst[n - 1 - k]) - 1);
				if (dict.get(lst[n - 1 - k]) == 0) dict.remove(lst[n - 1 - k]);
			}
			if (dict.isEmpty()) ans.add(k + 1);	
		}
		for (int i=0;i<ans.size();i++) {
			if (i > 0) System.out.print(" ");
			System.out.print(ans.get(i));
		}
		System.out.println();
	}
}

