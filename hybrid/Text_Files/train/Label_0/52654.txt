
import java.util.*;

public class Main {

	private void doIt() {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			String str = sc.next();
			int pre = sc.nextInt();
			int after = sc.nextInt();
			long money = pre * 200 + after * 300;
			int sum = pre + after;
			System.out.println(str + " " + sum + " " + money);
		}
		
	}
	public static void main(String[] args) {
		Main obj = new Main();
		obj.doIt();

	}

}