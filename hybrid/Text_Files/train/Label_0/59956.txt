import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int a = sc.nextInt();
		int b = sc.nextInt();
		ArrayList<Integer> list = new ArrayList<>();
		for (int i = 0; i < n; i++) {
		    int x = sc.nextInt();
		    if (x >= a) {
		        list.add(x);
		    } else {
		        break;
		    }
		}
		int count = 0;
		if (n - list.size() < m) {
		    for (int i = list.size() - 1; i >= 0; i--) {
		        if (list.get(i) <= b) {
		            count++;
		        } else {
		            break;
		        }
		    }
		}
		System.out.println(list.size() - count);
	}
}

