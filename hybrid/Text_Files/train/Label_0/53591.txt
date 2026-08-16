import java.util.Scanner;
import java.util.TreeMap;
import java.util.Map;

public class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);

		TreeMap<String,Integer> map = new TreeMap<>();

		int n = scan.nextInt();

		for(int i=0; i<n; i++) {

			int query = scan.nextInt();
			String key = scan.next();

			switch(query) {

			case 0:	//insert
				int value = scan.nextInt();
				map.put(key, value);
				break;

			case 1:	//get
				if(map.containsKey(key)) {
					System.out.println(map.get(key));
				}else
				System.out.println("0");
				break;

			case 2:	//delete
				map.remove(key);
				break;

			case 3:	//dump
				String limit = scan.next();
				for(Map.Entry<String, Integer> entry : map.subMap(key,true, limit,true).entrySet()){
					System.out.println(entry.getKey() + " " + entry.getValue());
				}

//				map.subMap(key,true, limit,true).forEach(Map.Entry<String, Integer> entry -> System.out.println(entry.getKey() + " " + entry.getValue()));
				break;
			}
		}
	}
}
