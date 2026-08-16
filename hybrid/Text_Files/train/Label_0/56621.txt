import java.math.BigInteger;
import java.util.*;

public class Main {
	
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			char [] data = sc.next().toCharArray();
			long count = 0;
			long sum = 0;
			for(int i = data.length-1; i >= 0; i--){
				if(data[i] =='W'){
					count++;
				}
				else {
					sum += count;
				}
			}
			System.out.println(sum);
		}
	}

	private void debug(Object... o) {
		System.out.println("debug = " + Arrays.deepToString(o));
	}

	public static void main(String[] args) {
		new Main().doit();
	}

}
