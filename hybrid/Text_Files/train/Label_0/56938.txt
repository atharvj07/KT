import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

//Transparent Mahjong
public class Main{

	int[] c, use;
	int free = 0;
	
	boolean f(int k, int u){
		if(free < u)return false;
		if(k==13){
			for(int i=1;i<=12;i++){
				if(use[i]<c[i] || 4<use[i])return false;
			}
			return true;
		}
		if(4<use[k])return false;
		if(use[k]<=1){
			int d = Math.max(0, 3-(c[k]-use[k]));
			use[k]+=3;
			if(f(k, u+d))return true;
			use[k]-=3;
		}
		if(c[k]<=use[k] && f(k+1, u))return true;
		if(k<=10){
			for(int i=1;i<=4;i++){
				int d = 0;
				for(int j=k;j<k+3;j++){
					d += Math.max(0, i-(c[j]-use[j]));
					use[j]+=i;
				}
				if(f(k+1, u+d))return true;
				for(int j=k;j<k+3;j++)use[j]-=i;
			}
		}
		return false;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		c = new int[13];
		use = new int[13];
		for(int i=0;i<3*n+1;i++){
			String s = sc.next();
			if("*".equals(s))free++;
			else c[Integer.parseInt(s)]++;
		}
		List<Integer> res = new ArrayList<Integer>();
		for(int i=1;i<=12;i++){
			if(c[i]<4){
				c[i]++;
				for(int j=1;j<=12;j++){
					Arrays.fill(use, 0);
					use[j] = 2;
					if(f(1, 0)){
						res.add(i);
						break;
					}
				}
				c[i]--;
			}
		}
		if(res.isEmpty())System.out.println(-1);
		else for(int x:res)System.out.println(x);
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}