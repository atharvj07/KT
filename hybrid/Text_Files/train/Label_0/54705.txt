import java.util.Arrays;
import java.util.Scanner;

//Headstrong Student
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int x = sc.nextInt(), y = sc.nextInt();
			if((x|y)==0)break;
			int[] a = new int[y];
			Arrays.fill(a, -1);
			a[x] = 0;
			int p = 0, q = 0, r = 1;
			for(;;){
				x = (x*10)%y;
				if(x==0){
					p = r; break;
				}
				if(a[x]==-1){
					a[x] = r++;
				}
				else{
					p = a[x]; q = r-a[x]; break;
				}
			}
			System.out.println(p+" "+q);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}