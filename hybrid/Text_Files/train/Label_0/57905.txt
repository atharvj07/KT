import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] num = new int[85715];
		int[] sosu = new int[35813];
		int[] tansaku = new int[300001];
		for(int i=6;i<=300000;++i){
			if(i%7==6 || i%7==1){
				tansaku[i]=1;
			}
		}
		int end=(int)Math.sqrt((double)300000);
		for(int i=6;i<=end;i++){
			if(tansaku[i]==1){
				for(int j=i+i;j<=300000;j+=i){  // 素数の定数倍は素数とならないので排除するループ
					if(tansaku[j]==1){
						tansaku[j]=0;
					}
				}
			}
		}
		int m=0;
		for(int i=6;i<=300000;++i){
			if(tansaku[i]==1){
				sosu[m]=i;
				++m;
			}
		}
		
		while(true){
			int n = sc.nextInt();
			if(n==1) break;
			Queue<Packet> que = new LinkedList<Packet>();
			HashSet<Integer> ans = new HashSet<Integer>();
			for(int i=0;i<sosu.length;++i){
				if(n%sosu[i]==0)
					if(n/sosu[i]==1) ans.add(sosu[i]);
					else que.add(new Packet(n/sosu[i],sosu[i]));
			}
			while(!que.isEmpty()){
				Packet pa = que.remove();
				for(int i=0;i<sosu.length;++i){
					if(pa.n%sosu[i]==0){
						if(pa.n/sosu[i]==1) ans.addAll(pa.set);
						else que.add(new Packet(pa.n/sosu[i],sosu[i]));
					}
				}
			}
			Iterator iterator = ans.iterator();
			int[] anss = new int[ans.size()];
			System.out.print(n+":");
			for(int i=0;i<ans.size();++i){
				anss[i]=(int) iterator.next();
			}
			Arrays.sort(anss);
			for(int i=0;i<anss.length-1;++i){
				System.out.print(" "+anss[i]);
			}
			System.out.println(" "+anss[anss.length-1]);
		}
	}
	
	public static class Packet{
		int n;
		HashSet<Integer> set = new HashSet<Integer>();
		Packet(int n,int sosu){
			this.n=n;
			set.add(sosu);
		}
	}
}

