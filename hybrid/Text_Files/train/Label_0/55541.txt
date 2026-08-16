import java.util.*;
import java.awt.geom.*;
public class Main {
	int res;
	boolean [] data;
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		int dataset = sc.nextInt();
		while(dataset-- > 0){
			data = new boolean[3];
			res = 0;
			int outcount = 0;
			while(outcount!= 3){
				String s = sc.next();
				if(s.charAt(0) == 'O') outcount++;
				else solve(s);
			}
			System.out.println(res);
		}
	}

	private void solve(String s) {
		if(s.charAt(1) == 'I'){
			//hit
			if(data[2]){
				res++;
			}
			data[2] = data[1];
			data[1] = data[0];
			data[0] = true;
		}
		else{
			//homeran
			for(int i = 0; i < 3; i++){
				if(data[i]){
					res++;
					data[i] = false;
				}
			}
			res++;
		}
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}