import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;


public class B {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		for(int i=0; i<n; i++){
			a[i] = sc.nextInt();
		}
		for(int i=0; i<n; i++){
			b[i] = sc.nextInt();
		}
		int m = sc.nextInt();
		Map<Integer, Integer> c = new TreeMap<Integer, Integer>();
		Map<Integer, Integer> d = new TreeMap<Integer, Integer>();
		for(int i=0; i<n; i++){
			if(c.containsKey(a[i])){
				c.put(a[i], c.get(a[i])+1);
			}else{
				c.put(a[i], 1);
			}
			if(c.containsKey(b[i])){
				c.put(b[i], c.get(b[i])+1);
			}else{
				c.put(b[i], 1);
			}
			if(a[i] == b[i]){
				if(d.containsKey(a[i])){
					d.put(a[i], d.get(a[i])+1);
				}else{
					d.put(a[i], 1);
				}
			}
		}
		long ans = 1;
		
		for(Map.Entry<Integer, Integer> e : c.entrySet()) {
			int tmp = e.getValue();
			int tmp2 = (d.containsKey(e.getKey()))? d.get(e.getKey()) : 0;
			while(tmp > 0){
				if(tmp2>0 && tmp%2 == 0){
					ans = (ans * tmp/2)%m;
					tmp2--;
				}else{
					ans = (ans * tmp)%m;
				}
				tmp--;
			}
		}
		System.out.println(ans);
	}

}
