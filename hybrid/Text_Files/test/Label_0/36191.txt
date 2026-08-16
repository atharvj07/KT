import java.util.*;
import java.awt.geom.*;
public class Main {

	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = Integer.parseInt(sc.nextLine());
			if(n == 0) break;
			HashMap<String, Integer> log = new HashMap<String, Integer>();
			HashMap<String, Integer> record = new HashMap<String, Integer>();
			for(int i = 0 ; i < n; i++){
				String s = sc.nextLine();
				String [] ss = s.split(" ");
				String [] time = ss[1].split(":");
				int h = Integer.parseInt(time[0]);
				int m = Integer.parseInt(time[1]);
				int value = h * 60 + m;
				if(ss[2].equals("I")){
					record.put(ss[3], value);
				}
				else{
					if(ss[3].equals("000")){
						for(String key: record.keySet()){
							if(key.equals("000")) continue;
							int diff = value - Math.max(record.get(key), record.get("000"));
							//System.out.println("diff = " + diff);
							if(log.containsKey(key)){
								log.put(key, log.get(key) + diff);
							}
							else{
								log.put(key, diff);
							}
						}
						record.remove(ss[3]);
					}
					else{
						if(record.containsKey("000")){
							int diff = value - Math.max(record.get(ss[3]), record.get("000"));
							record.remove(ss[3]);
							if(log.containsKey(ss[3])){
								log.put(ss[3], log.get(ss[3]) + diff);
							}
							else{
								log.put(ss[3], diff);
							}
						}
						else{
							record.remove(ss[3]);
						}
					}
				}
//				System.out.println("i = " + i);
//				for(String key: record.keySet()){
//					System.out.println("key = " + key + " value = " + record.get(key));
//				}
//				System.out.println();
//				for(String key : log.keySet()){
//					System.out.println("ley = " + key + "value = " + log.get(key));
//				}
//				System.out.println("---");
			}
			int max = 0;
			for(String key: log.keySet()){
				//System.out.println("key = " + key + " value = " + log.get(key));
				if(key.equals("000")) continue;
				max = Math.max(max, log.get(key));
			}
			System.out.println(max);
		}
	}

	public static void main(String [] args){
		new Main().doit();
	}
}