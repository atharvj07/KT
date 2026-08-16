import java.util.Arrays;
import java.util.Scanner;

public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}
	public Main() {
		new C().doIt();
	}
	
	class C{
		boolean[][] stick_table;
		boolean[][] broken_table;
		void doIt(){
			stick_table = new boolean[10][8];
			broken_table = new boolean[14][8];
			initTable();
			for(int i=0;i<14;i++)for(int s=0;s<7;s++)broken_table[i][s] = true;
			int n = in.nextInt();
			int k = in.nextInt();
			long result = 0;
			for(int i=0;i<k;i++){
				int a = in.nextInt();
				int b = in.nextInt();
				broken_table[a][b] = false;
			}
			int[] timeCount = new int[100];
			for(int h=0;h<24;h++)for(int m=0;m<60;m++)for(int s=0;s<60;s++){
				int[] num = {h/10,h%10,m/10,m%10,s/10,s%10};
				int sum = 0;
				for(int i=0;i<6;i++){
					sum += countNum(num[i], i+8);
				}
				timeCount[sum]++;
			}
			
//			System.out.println(Arrays.toString(timeCount));
//			if(true)return ;
			for(int year=0;year<10000;year++)for(int month = 1;month < 13; month ++){
				int limitDay = days(year, month);
				for(int day=1;day<=limitDay;day++){
					int num[] = {year/1000,(year/100)%10,(year/10)%10,year%10,month/10,month%10,day/10,day%10};
					int sum = 0;
					for(int i=0;i<8;i++){
						int sticks = countNum(num[i], i);
						sum += sticks;
					}
					int index = n-sum;
					if(index < 0 || index >= 100)continue;
//					if(timeCount[index] > 0)System.out.println(Arrays.toString(num));
					result += timeCount[index];
				}
			}
			System.out.println(result);
		}
		
		int days(int year,int month){
			if(isPrimeYear(year) && month == 2)return 29;
			int[] day = {31,28,31,30,31,30,31,31,30,31,30,31};
			return day[month-1];
		}
		
		boolean isPrimeYear(int year){
			if(year%400 == 0)return true;
			if(year%100 == 0)return false;
			if(year%4 == 0)return true;
			return false;
		}
		
		int countNum(int target,int id){
			int cnt = 0;
			for(int i=0;i<7;i++)if(broken_table[id][i] && stick_table[target][i])cnt++;
			return cnt;
		}
		
		void initTable(){
			boolean[][] a = {{true,true,true,false,true,true,true},
							{false,false,true,false,false,true,false},
							{true,false,true,true,true,false,true},
							{true,false,true,true,false,true,true},
							{false,true,true,true,false,true,false},
							{true,true,false,true,false,true,true},
							{true,true,false,true,true,true,true},
							{true,false,true,false,false,true,false},
							{true,true,true,true,true,true,true},
							{true,true,true,true,false,true,true}};
			for(int i=0;i<10;i++)for(int s=0;s<7;s++)stick_table[i][s] = a[i][s];
		}
		
	}
	
}