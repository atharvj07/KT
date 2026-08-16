import java.util.Scanner;

//Make Purse Light
public class Main {

	public static int minCoin;
	public static int[] coins;
	public static int[] used;
	public static int[] ans;

	public static int returnCoin(int x){
		int s = 0;
		s += x/500;
		x %= 500;
		s += x/100;
		x %= 100;
		s += x/50;
		x %= 50;
		s += x/10;
		return s;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean first = true;
		while(true){
			int x = sc.nextInt();
			if(x==0)break;
			if(!first)System.out.println();
			first = false;
			minCoin = Integer.MAX_VALUE;
			coins = new int[4];
			int num = 0;
			for(int i=0;i<4;i++){
				coins[i] = sc.nextInt();
				num += coins[i];
			}
			used = new int[4];
			ans = new int[4];
			for(used[0]=0;used[0]<=coins[0];used[0]++){
				for(used[1]=0;used[1]<=coins[1];used[1]++){
					for(used[2]=0;used[2]<=coins[2];used[2]++){
						for(used[3]=0;used[3]<=coins[3];used[3]++){
							int sum = used[0]*10 + used[1]*50 + used[2]*100 + used[3]*500;
							if(sum >= x && num-(used[0]+used[1]+used[2]+used[3])+returnCoin(sum-x)<minCoin){
								minCoin = num-(used[0]+used[1]+used[2]+used[3])+returnCoin(sum-x);
								for(int i=0;i<4;i++)ans[i]=used[i];
							}
						}
					}
				}
			}
			for(int i=0;i<4;i++){
				if(ans[i]!=0){
					System.out.println((i==0?10:i==1?50:i==2?100:500) + " " + ans[i]);
				}
			}
		}
	}
}