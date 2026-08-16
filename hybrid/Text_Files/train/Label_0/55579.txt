import java.util.*;
public class Main {
	Scanner sc = new Scanner(System.in);
	public int pasta() {
		int ans = 0;
		for(int i = 0; i < 3; i++) {
			int input = sc.nextInt();
			if(i == 0 || ans > input) ans = input;
		}
		return ans;
	}
	public int juice() {
		int ans = 0;
		for(int i = 0; i < 2; i++) {
			int input = sc.nextInt();
			if(i == 0 || ans > input) ans = input;
		}
		return ans;
	}
	public void set() {
		int p = pasta();
		int j = juice();
		int ans = p+j-50;
		System.out.println(ans);
	}
	public static void main(String[] args) {
		new Main().set();
	}

}