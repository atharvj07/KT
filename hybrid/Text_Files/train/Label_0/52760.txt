import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
	static String s = "";
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			s = br.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		HashMap<Integer, String> map = new HashMap<>();
		
		System.out.println(search(map,"", 0, 1));
}
	static int search(HashMap<Integer, String> map, String prev, int begin, int len) {
		if(begin+len > s.length())return map.size();
		String sub = s.substring(begin, begin+len);
		if(sub.equals(prev)) {
			return search(map,prev, begin, len+1);
		}else {
			map.put(begin, sub);
			return search(map, sub,begin+len, 1);
		}
		
	}
}
