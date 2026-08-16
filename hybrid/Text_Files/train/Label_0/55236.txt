
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}

	Scanner sc = new Scanner(System.in);

	void run() {
		for (;;) {

			int n = sc.nextInt();
			int m = sc.nextInt();
			if (n == 0 && m == 0) {
				break;
			}
			String b[] = new String[n];

			for (int i = 0; i < n; i++) {
				b[i] = sc.next();
			}

			Map<String, Integer> map = new HashMap<String, Integer>();
			map.put(zero(m), 0);

			for (int i = 0; i < n; i++) {
				Map<String, Integer> next = new HashMap<String, Integer>();

				next.putAll(map);
				for (Entry<String, Integer> e : map.entrySet()) {
					String str = xor(e.getKey(), b[i]);
					int value = e.getValue()+1;
					if(!next.containsKey(str) || value > next.get(str) ){
						next.put(str, e.getValue()+1);
					}
				}
				
				map = next;
			}
			System.out.println(map.get(zero(m)));
		}
	}

	String zero(int m) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < m; i++) {
			sb.append("0");
		}
		return sb.toString();
	}

	String xor(String a, String b){
		StringBuilder sb =new StringBuilder();
		for(int i =0 ; i< a.length() ;i++){
			if(a.charAt(i) == b.charAt(i)){
				sb.append("0");
			}else{
				sb.append("1");
			}
		}
		return sb.toString();
		
	}
}

