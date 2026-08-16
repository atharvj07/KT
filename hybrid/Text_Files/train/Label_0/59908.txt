import java.util.Scanner;
public class Main{
	public static void main(String[]args){
		int ban;
		int su;
		int kin;
		int s=6000,a=4000,b=3000,c=2000;
		Scanner sc = new Scanner(System.in);
		
		for(int i=0;i<4;i++){
			ban = sc.nextInt();
		    su = sc.nextInt();
			switch(ban){
				case 1:
				kin = s*su;
				System.out.println(kin);
				break;
				case 2:
				kin = a*su;
				System.out.println(kin);
				break;
				case 3:
				kin = b*su;
				System.out.println(kin);
				break;
				case 4:
				kin = c*su;
				System.out.println(kin);
				break;
			}
		}
	}
}