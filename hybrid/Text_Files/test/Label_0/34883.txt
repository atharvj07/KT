import java.util.*;
public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}

	public Main(){
		new AOJ0257().doIt();
	}
	
	class AOJ0257{
		void doIt(){
			HashMap<String, String> map = new HashMap<String, String>();
			map.put("1 0 0", "Close");map.put("0 1 0", "Close");map.put("1 1 0", "Open");map.put("0 0 1", "Open");
			map.put("0 0 0", "Close");
			while(in.hasNext()){
				System.out.println(map.get(in.nextLine()));
			}
		}
	}
	
}