import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long a = sc.nextLong();
		long b = sc.nextLong();
		List<Long> l1 = insu(a);
		List<Long> l2 = insu(b);
		HashSet<Long> h = new HashSet<Long>(l1);
		l1.clear();
		l1.addAll(h);
		h = new HashSet<Long>(l2);
		l2.clear();
		l2.addAll(h);
		int ans = 0;
		for(long i: l1){
			if(l2.contains(i)) {
				ans++;
			}
		}
		System.out.println(ans+1);
	}

	public static List<Long> insu(long n){
		List<Long> list = new ArrayList<>();
		if(n==1) return list;
		for(int i=2; i<=Math.sqrt(n); i++){
			if(n%i == 0){
				list.add((long)i);
				n = n/i;
				i = 1;
			}
		}
		list.add(n);
		return list;
	}
}
