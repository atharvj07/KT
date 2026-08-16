import java.util.Scanner;

public class Main {
	private Scanner sc;
	
	public static void main(String[] args) {
		new Main();
	}
	
	public Main() {
		sc = new Scanner(System.in);
		
		String[] nico = sc.nextLine().split(" ");
		int n = Integer.parseInt(nico[0]);
		int q = Integer.parseInt(nico[1]);

		int[] list = new int[n + 1];
		for (int i = 0; i < list.length; i++) {
			list[i] = 0;
		}
		
		int max = 0;
		int no = 1;
		for (int i = 0; i < q; i++) {
			String[] set = sc.nextLine().split(" ");
			int[] data = new int[set.length];
			
			for (int j = 0; j < set.length; j++) {
				data[j] = Integer.parseInt(set[j]);
			}

			list[data[0]] = list[data[0]] + data[1];
			
			if ((no == data[0]) && (data[1] < 0)) {
				int tmp = list[data[0]];
				int newno = data[0];
				
				for (int j = 1; j < list.length; j++) {
					if (tmp <= list[j]) {
						if (tmp == list[j]) {
							if (newno > j) newno = j;
						} else {
							tmp = list[j];
							newno = j;
						}
					}
				}
				
				max = tmp;
				no = newno;
			}
			
			if (max <= list[data[0]]) {
				if (max == list[data[0]]) {
					if (no > data[0]) no = data[0];
				} else {
					max = list[data[0]];
					no = data[0];
				}
			}
			System.out.println(no + " " + max);
		}
	}
}