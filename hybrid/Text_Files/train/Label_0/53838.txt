import java.util.Scanner;

//Card Game II
public class Main{

	int[] res, t;
	
	void add(int D){
		t[0] = 1/D;
		int R = 1%D, id = 1;
		while(id<t.length){
			R*=10;
			t[id++] = R/D;
			R%=D;
		}
		for(int i=t.length-1;i>0;i--){
			res[i]+=t[i];
			res[i-1]+=res[i]/10;
			res[i]%=10;
		}
		res[0]+=t[0];
	}
	
	void div(int n){
		t[0] = res[0]/n;
		int R = res[0]%n, id = 1;
		while(id<t.length){
			R = R*10 + res[id];
			t[id++] = R/n;
			R%=n;
		}
		for(int i=0;i<t.length;i++)res[i] = t[i];
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt(), k = sc.nextInt(), m = sc.nextInt(), r = sc.nextInt();
			if((n|k|m|r)==0)break;
			res = new int[r+10];
			t = new int[r+10];
			if(m==0){
				add(n);
			}
			else{
				for(int i=1;i<n;i++)add(i);
				div(n);
				add(n);
			}
			System.out.print(res[0]+".");
			for(int i=1;i<=r;i++)System.out.print(res[i]+(i==r?"\n":""));
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}