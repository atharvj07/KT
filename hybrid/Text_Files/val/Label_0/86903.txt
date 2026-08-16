import java.util.Scanner;
import java.util.Vector;

public class Main {

	public static void main(String[] args) {
		doIt();
	}
	
	public static void doIt(){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		while(n + m > 0){
			Vector<Integer> v = new Vector<Integer>(n);
			for(int i = 0; i < n; i++){
				v.add(i + 1);
			}
			int point = 0;
			for(int i = n; i > 1; i--){
				point = (point + m - 1) % i;
				//System.out.println("point = " + point + ", v[point] = " + v.elementAt(point));
				v.remove(point);
			}
			System.out.println(v.get(0));
			n = sc.nextInt();
			m = sc.nextInt();
		}
	}
}