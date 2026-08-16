import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

	static char[] ch;
	static int id;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int T = sc.nextInt(); T-- > 0; ) {
			ch = sc.next().toCharArray();
			id = 0;
			
			System.out.println(exp());
		}

		sc.close();
	}

	static int exp() {
		id++;
		if(Character.isDigit(ch[id])) {
			int num = num();
			id++;
			return num;
		}
		
		List<Integer> list = new ArrayList<Integer>();

		for(;;) {
			if(ch[id] == '[') {
				list.add(exp());
			} else {
				break;
			}
		}

		id++;
		Collections.sort(list);
		int num = 0;
		for(int i = 0; i < (list.size() + 1) / 2; i++) {
			num += list.get(i);
		}
		
		return num;
	}

	static int num() {
		int x = 0;
		while(Character.isDigit(ch[id])) {
			x *= 10;
			x += ch[id++] - '0';
		}
		
		x++;
		return x / 2;
	}
}