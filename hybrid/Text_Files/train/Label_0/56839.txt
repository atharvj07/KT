import java.util.*;

public class Main{
	Scanner sc = new Scanner(System.in);
	
	private void doit(){
		
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			int [] data = new int[5];
			data[0] = n;
			for(int i = 1; i < 5; i++){
				data[i] = sc.nextInt();
			}
			int [] freq = new int[4];
			for(int i = 0; i < 5; i++){
				freq[data[i]]++;
			}
			int count = 0;
			for(int i = 0; i < 4; i++){
				if(freq[i] > 0){
					count++;
				}
			}
			if(count == 3 || count == 1){
				for(int i = 0; i < 5; i++){
					System.out.println(3);
				}
			}
			else{
				if(freq[3] == 0){
					for(int i = 0; i < 5; i++){
						if(data[i] == 1){
							System.out.println(1);
						}
						else{
							System.out.println(2);
						}
					}
				}
				else if(freq[2] == 0){
					for(int i = 0; i < 5; i++){
						if(data[i] == 1){
							System.out.println(2);
						}
						else{
							System.out.println(1);
						}
					}
				}
				else{
					for(int i = 0; i < 5; i++){
						if(data[i] == 2){
							System.out.println(1);
						}
						else{
							System.out.println(2);
						}
					}
				}
			}
		}
		
	}
	
	//Stringの配列。データセットの間は空行を入れる
	private String[] toStrArr() {
		StringBuilder sb = new StringBuilder();
		while(sc.hasNext()){
			String s = sc.nextLine().trim();
			if(s.equals("")) break;
			sb.append(s);
		}
		String s = sb.toString().replaceAll("[{}\" ]", "");
		String [] t = s.split(",");
		return t;
	}

	//String
	private String toStr() {
		String s = sc.next().replaceAll("\"", "");
		return s;
	}
	
	//intの配列
	private int[] toIntArr() {
		String [] t = toStrArr();
		int [] res = new int[t.length];
		for(int i = 0; i < t.length; i++){
			res[i] = Integer.parseInt(t[i]);
		}
		return res;
	}

	private void debug(Object... o) { System.out.println("debug = " + Arrays.deepToString(o)); }

	public static void main(String[] args) {
		new Main().doit();
	}
}