import java.util.Scanner;

//Highway Toll
public class Main{

	public static void main(String[] args) {
		int[][] p = {
				{0,300,500,600,700,1350,1650},
				{300,0,350,450,600,1150,1500},
				{500,350,0,250,400,1000,1350},
				{600,450,250,0,250,850,1300},
				{700,600,400,250,0,600,1150},
				{1350,1150,1000,850,600,0,500},
				{1650,1500,1350,1300,1150,500,0}
		};
		int[][] d = {
				{0,6,13,18,23,43,58},
				{6,0,7,12,17,37,52},
				{13,7,0,5,10,30,45},
				{18,12,5,0,5,25,40},
				{23,17,10,5,0,20,35},
				{43,37,30,25,20,0,15},
				{58,52,45,40,35,15,0}
		};
		Scanner sc = new Scanner(System.in);
		while(true){
			int s = sc.nextInt();
			if(s==0)break;
			s--;
			int sh = sc.nextInt()*60+sc.nextInt();
			int t = sc.nextInt()-1;
			int th = sc.nextInt()*60+sc.nextInt();
			int x = p[s][t]/50;
			if(d[s][t]<=40&&(17*60+30<=sh&&sh<=19*60+30 || 17*60+30<=th&&th<=19*60+30)){
				if(x%2==1)x=x/2+1;
				else x/=2;
			}
			System.out.println(x*50);
		}
	}
}