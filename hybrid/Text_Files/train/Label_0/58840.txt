import java.util.ArrayList;
import java.util.OptionalInt;
import java.util.Scanner;

public class Main {
public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int K = sc.nextInt(),N =sc.nextInt();
	ArrayList<Integer> list = new ArrayList<>();
	for(int i=0;i<N;i++) {
		list.add(sc.nextInt());
	}
	ArrayList<Integer> sa = new ArrayList<>();
	for(int i=1;i<N;i++) {
		sa.add(list.get(i)-list.get(i-1));
	}
	sa.add(list.get(0)+K-list.get(N-1));
	OptionalInt max = sa.stream().mapToInt(v -> v).max();
	int ans = K-max.getAsInt();
	System.out.println(ans);
}
}
