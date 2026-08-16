import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		List<Integer> D = new ArrayList<>();
		for(int i = 0;i < K;i++) {
			D.add(sc.nextInt());
		}
		sc.close();
		int res = 0;
		while(N > 0) {
			if(checkNum(N, D)){
				res = N;
				break;
			}
			N++;
		}
		System.out.println(res);
	}

	private static boolean checkNum(int n, List<Integer> array) {
		boolean flag = true;
		while(n > 0) {
			if(array.contains(n%10)) {
				flag = false;
				break;
			}
			n /= 10;
		}
		return flag;
	}
}