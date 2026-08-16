import java.util.*;

public class Main{
	public static void main(String[] args){

		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int T = 0;
		int H = 0;
		for(int i = 0; i < n; i++){
			String sT = scan.next();
			String sH = scan.next();
			if(sT.compareTo(sH) < 0){
				H += 3;
			} else if(sT.compareTo(sH) > 0){
				T += 3;
			} else{
				T++;
				H++;
			}
		}
		System.out.printf("%d %d\n", T, H);
	}
}